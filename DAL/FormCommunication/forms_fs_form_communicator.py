import os
import json

from Core.Interfaces.FormCommunication.i_form_communicator import *
from Core.Models.form import Form
from Core.Keys.FormsFSKeys.forms_fs_file_navigation_keys import PATH_SEPARATOR, FORMS_FS_ROOT, FORMS_FOLDER_NAME


class FormsFSFormCommunicator(IFormCommunicator):
    def __init__(self, users_communicator):
        self._users_communicator = users_communicator

    def get_form(self, form_id):
        form_path = "{root}{delimiter}{forms}{delimiter}{id}.json".format(delimiter=PATH_SEPARATOR,
                                                                          root=FORMS_FS_ROOT,
                                                                          forms=FORMS_FOLDER_NAME,
                                                                          id=form_id)
        if not os.path.exists(form_path):
            raise ValueError("Form does not exist. ID: {id}".format(id=form_id))

        with open(form_path, "rb") as form_fp:
            # Convert to Form model
            form = Form.create_from_dictionary(json.load(form_fp))

        return form

    def update_form(self, form):
        form_path = "{root}{delimiter}{forms}{delimiter}{id}.json".format(delimiter=PATH_SEPARATOR,
                                                                          root=FORMS_FS_ROOT,
                                                                          forms=FORMS_FOLDER_NAME,
                                                                          id=form.uuid)
        if not os.path.exists(form_path):
            raise ValueError("Form does not exist already. ID: {id}".format(id=form.uuid))

        with open(form_path, "wb+") as form_fp:
            json.dump(Form.serialize_to_json(form), form_fp)

    def create_form(self, form):
        form_path = "{root}{delimiter}{forms}{delimiter}{id}.json".format(delimiter=PATH_SEPARATOR,
                                                                          root=FORMS_FS_ROOT,
                                                                          forms=FORMS_FOLDER_NAME,
                                                                          id=form.uuid)
        if os.path.exists(form_path):
            raise ValueError("Form exists already. ID: {id}".format(id=form.uuid))

        with open(form_path, "wb+") as form_fp:
            json.dump(Form.serialize_to_json(form), form_fp)

    def get_all_active_forms_by_user(self, user_id):
        forms = list()
        ids = self._users_communicator.get_user_active_forms_ids(user_id)
        for form_id in ids:
            forms.append(self.get_form(form_id))
        return forms

    def get_all_awaiting_forms_by_user(self, user_id):
        forms = list()
        ids = self._users_communicator.get_user_awaiting_forms_ids(user_id)
        for form_id in ids:
            forms.append(self.get_form(form_id))
        return forms
