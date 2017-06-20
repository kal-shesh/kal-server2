import json
import os

from Core.Interfaces.FormCommunication.i_empty_form_communicator import *
from Core.Keys.FormsFSKeys.forms_fs_file_navigation_keys import PATH_SEPARATOR, FORMS_FS_ROOT, EMPTY_FORMS_FOLDER_NAME
from Core.Models.form import Form


class FormsFSEmptyFormCommunicator(IEmptyFormCommunicator):
    def __init__(self, forms_communicator):
        self._forms_communicator = forms_communicator

    def get_form(self, form_id):
        return Form.serialize_to_json(self._forms_communicator.get_form(form_id))

    def get_all_waiting_forms(self, user_id):
        forms = []
        for form in self._forms_communicator.get_all_awaiting_forms_by_user(user_id):
            forms.append(json.loads(Form.serialize_to_json(form)))
        return json.dumps(forms)

    def get_all_active_forms(self, user_id):
        forms = []
        for form in self._forms_communicator.get_all_active_forms_by_user(user_id):
            forms.append(json.loads(Form.serialize_to_json(form)))
        return json.dumps(forms)

    def get_all_forms_types(self):
        forms_list = []
        empty_forms_path = "{root}{delimiter}{empty_forms}".format(root=FORMS_FS_ROOT,
                                                                   empty_forms=EMPTY_FORMS_FOLDER_NAME,
                                                                   delimiter=PATH_SEPARATOR)
        for f in os.listdir(empty_forms_path):
            path = "{empty_forms_folder}{delimiter}{file}".format(empty_forms_folder=empty_forms_path,
                                                                  delimiter=PATH_SEPARATOR,
                                                                  file=f)
            with open(path, "r") as fp:
                data = json.load(fp)
                forms_list.append(data)
        return json.dumps(forms_list)

    def get_form_type(self, type_id):
        form_path = "{root}{delimiter}{empty_forms}{delimiter}{type_id}.json".format(root=FORMS_FS_ROOT,
                                                                                     empty_forms=EMPTY_FORMS_FOLDER_NAME,
                                                                                     delimiter=PATH_SEPARATOR,
                                                                                     type_id=type_id)
        with open(form_path, "r") as form_type:
            data = form_type.read()

        return data
