from Core.Interfaces import *
from Core.Keys import *
import json
import datetime
import uuid
from Core import Form


class FormExecutor(IFormExecutor):
    def __init__(self, form_getter, form_commincator, user_commincator, hr_data_manager, hr_hirarchy_manager):
        self.form_getter = form_getter  # type: IFormGetter
        self.form_commincator = form_commincator  # type: IFormCommunicator
        self.user_commincator = user_commincator  # type: IUsersCommunicator
        self.hr_data_manager = hr_data_manager  # type: IHRSoldiersDataManager
        self.hr_hirarchy_manager = hr_hirarchy_manager  # type: IHRDataHierarchyManager

    def create_form(self, user_id, form_data):
        # type (str, dict) -> None
        form_data = json.loads(form_data)
        form_schema = json.loads(self.form_getter.get_form_type(form_data['id']))
        form_data['data'] = self.__get_full_form_data(form_schema, form_data)
        form_data['uuid'] = uuid.uuid4()
        self.__generate_metadata(form_data, form_schema, user_id)
        form_object = Form.create_from_dictionary(form_data)
        self.__generate_step_approvers(user_id, form_object.form_metadata.steps)
        self.__save_new_form(form_object)

    def update_step(self, user_id, form_id, data):
        raise NotImplementedError

    def __get_full_form_data(self, form_schema, form_data):
        form_schema_keys = self.__get_default_dictionary_by_schema(form_schema['schema']['properties'])
        partial_form_data = form_data['data']
        full_form_data = self.__complete_dictionary_by_schema_dictionary(partial_form_data, form_schema_keys)
        return full_form_data

    def __get_default_dictionary_by_schema(self, dictionary):
        result = {}
        for key in dictionary:
            if dictionary[key]['type'] != 'object':
                result[key] = ""
            else:
                result[key] = self.__get_default_dictionary_by_schema(dictionary[key]['properties'])
        return result

    def __complete_dictionary_by_schema_dictionary(self, dictionary, schema_dictionary):
        for key in schema_dictionary:
            if key not in dictionary:
                dictionary[key] = schema_dictionary[key]
            elif type(schema_dictionary[key]) is type(dict):
                dictionary[key] = self.__complete_dictionary_by_schema_dictionary(dictionary[key],
                                                                                  schema_dictionary[key])
        return dictionary

    def __generate_metadata(self, form_data, form_type_data, user_id):
        form_data['form_metadata'] = {key: value for (key, value) in form_type_data.items() if key != 'shcema'}
        time = str(datetime.datetime.now())
        form_data['form_metadata']['creation_time'] = time
        form_data['form_metadata']['last_update_time'] = time
        form_data['form_metadata']['creator_id'] = user_id


    def __generate_step_approvers(self, user_id, steps):
        user_data = self.hr_data_manager.get_hr_soldier_data_by_id(user_id)
        hirarchy = self.__get_user_hirarchy_list(user_data)
        for step in steps:
            step.approver = self.hr_hirarchy_manager.get_corresponding_organizational_role(hirarchy,
                                                                                              step.approver)
            if len(step.next_steps) != 0:
                self.__generate_step_approvers(user_id, step.next_steps)

    def __get_user_hirarchy_list(self, user_data):
        keys = [DIVISION_KEY, UNIT_KEY, BRANCH_KEY, DEPARTMENT_KEY, TEAM_KEY]
        return [user_data[key] for key in keys]

    def __save_new_form(self, form_object):
        changes = {ADDED_KEY: [form_object.uuid]}
        self.form_commincator.create_form(form_object)
        self.user_commincator.update_user_active_forms_file(form_object.form_metadata.creator_id,
                                                            changes)
        for approver in self.__get_all_awaiting_approvers(form_object.form_metadata.steps):
            self.user_commincator.update_user_awaiting_forms_file(approver, changes)

    def __get_all_awaiting_approvers(self, steps):
        approvers = []
        for step in steps:
            if step.status == WAITING:
                approvers.append(step.approver_id)
            elif step.status == APPROVED:
                approvers = approvers + self.__get_all_awaiting_approvers(steps.steps)
        return approvers
