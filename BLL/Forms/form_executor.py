from Core.Interfaces import *
from Core.Keys import *
import json
import datetime
import uuid
from Core import Form
from PDF.pdf_generator import PdfGenerator


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
        form_data['uuid'] = uuid.uuid4().urn[9:]
        self.__generate_metadata(form_data, form_schema, user_id)
        form_object = Form.create_from_dictionary(form_data)
        self.__generate_step_approvers(user_id, form_object.metadata.next_steps)
        self.__save_new_form(form_object)
        PdfGenerator.create_pdf(form_object)
        return True

    def update_step(self, user_id, form_id, data):
        form = self.form_commincator.get_form(form_id)
        if data['status'] in [APPROVED, REJECTED]:
            self.form_commincator.update_form(form)
            self.user_commincator.update_user_awaiting_forms_file(user_id, {REMOVED_KEY: [form_id]})
            PdfGenerator.create_pdf(form)
        elif data['status'] in [WAITING]:
            for approver in self.__get_all_awaiting_approvers(form.form_metadata.next_steps):
                self.user_commincator.update_user_awaiting_forms_file(approver, {ADDED_KEY: [form_id]})

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
        form_data['metadata'] = {key: value for (key, value) in form_type_data.items() if key != 'shcema'}
        time = str(datetime.datetime.now())
        form_data['metadata']['creation_time'] = time
        form_data['metadata']['last_update_time'] = time
        form_data['metadata']['creator_id'] = user_id

    def __generate_step_approvers(self, user_id, steps):
        user_data = self.hr_data_manager.get_hr_soldier_data_by_id(user_id)
        hierarchy = self.__get_user_hirarchy_list(user_data)
        for step in steps:
            step.approver = self.hr_hirarchy_manager.get_corresponding_organizational_role(hierarchy,
                                                                                           step.approver)
            if len(step.next_steps) != 0:
                self.__generate_step_approvers(user_id, step.next_steps)

    def __get_user_hirarchy_list(self, user_data):
        keys = [DIVISION_KEY, UNIT_KEY, BRANCH_KEY, DEPARTMENT_KEY, TEAM_KEY]
        return [user_data[key] for key in keys]

    def __save_new_form(self, form_object):
        changes = {ADDED_KEY: [form_object.uuid]}
        self.form_commincator.create_form(form_object)
        self.user_commincator.update_user_active_forms_file(form_object.metadata.creator_id,
                                                            changes)
        for approver in self.__get_all_awaiting_approvers(form_object.metadata.next_steps):
            self.user_commincator.update_user_awaiting_forms_file(approver, changes)

    def __get_all_awaiting_approvers(self, steps):
        approvers = []
        for step in steps:
            if step.status == WAITING:
                approvers.append(step.approver)
            elif step.status == APPROVED:
                approvers = approvers + self.__get_all_awaiting_approvers(step.next_steps)
        return approvers
