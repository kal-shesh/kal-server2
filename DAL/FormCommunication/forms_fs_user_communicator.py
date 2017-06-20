import os
import json

from Core.Interfaces.FormCommunication.i_users_communicator import IUsersCommunicator

from Core.Keys.FormsFSKeys.forms_fs_user_form_changes_keys import *
from Core.Keys.FormsFSKeys.forms_fs_file_navigation_keys import *


class FormsFSUserCommunicator(IUsersCommunicator):
    def __init__(self):
        pass

    def get_user_active_forms_ids(self, user_id):
        active_forms_file_path = "{root}{delimiter}{users}{delimiter}{user}{delimiter}{active_forms}" \
            .format(root=FORMS_FS_ROOT,
                    delimiter=PATH_SEPARATOR,
                    users=USERS_FOLDER_NAME,
                    user=user_id,
                    active_forms=ACTIVE_FORMS_FILE_NAME)

        if not os.path.exists(active_forms_file_path):
            raise ValueError("Active Forms File does not exist. ID: {id}".format(id=user_id))

        with open(active_forms_file_path, "rb") as active_forms_fp:
            ids = json.load(active_forms_fp)
        return ids

    def get_user_awaiting_forms_ids(self, user_id):
        awaiting_forms_file_path = "{root}{delimiter}{users}{delimiter}{user}{delimiter}{awaiting_forms}" \
            .format(root=FORMS_FS_ROOT,
                    delimiter=PATH_SEPARATOR,
                    users=USERS_FOLDER_NAME,
                    user=user_id,
                    awaiting_forms=AWAITING_FORMS_FILE_NAME)

        if not os.path.exists(awaiting_forms_file_path):
            raise ValueError("Awaiting Forms File does not exist. ID: {id}".format(id=user_id))

        with open(awaiting_forms_file_path, "rb") as active_forms_fp:
            ids = json.load(active_forms_fp)
        return ids

    def update_user_active_forms_file(self, user_id, changes):
        user_folder = FormsFSUserCommunicator._get_user_folder_by_id(user_id)
        active_forms_file_path = "{user_folder}{delimiter}{active_forms}" \
            .format(user_folder=user_folder,
                    delimiter=PATH_SEPARATOR,
                    active_forms=ACTIVE_FORMS_FILE_NAME)

        data = list()

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if os.path.exists(active_forms_file_path):
            with open(active_forms_file_path, "rb") as active_forms_read_fp:
                data = json.load(active_forms_read_fp)

        if ADDED_KEY in changes:
            for add_change in changes[ADDED_KEY]:
                if add_change not in data:
                    data.append(add_change)
        if REMOVED_KEY in changes:
            for remove_change in changes[REMOVED_KEY]:
                if remove_change in data:
                    data.remove(remove_change)

        with open(active_forms_file_path, 'w+') as active_forms_write_fp:
            json.dump(data, active_forms_write_fp)

    def update_user_awaiting_forms_file(self, user_id, changes):
        user_folder = FormsFSUserCommunicator._get_user_folder_by_id(user_id)
        awaiting_forms_file_path = "{user_folder}{delimiter}{awaiting_forms}" \
            .format(user_folder=user_folder,
                    delimiter=PATH_SEPARATOR,
                    awaiting_forms=AWAITING_FORMS_FILE_NAME)

        data = list()

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if os.path.exists(awaiting_forms_file_path):
            with open(awaiting_forms_file_path, "rb") as awaiting_forms_read_fp:
                data = json.load(awaiting_forms_read_fp)

        if ADDED_KEY in changes:
            for add_change in changes[ADDED_KEY]:
                if add_change not in data:
                    data.append(add_change)
        if REMOVED_KEY in changes:
            for remove_change in changes[REMOVED_KEY]:
                if remove_change in data:
                    data.remove(remove_change)

        with open(awaiting_forms_file_path, "w+") as awaiting_forms_write_fp:
            json.dump(data, awaiting_forms_write_fp)

    @staticmethod
    def _get_user_folder_by_id(user_id):
        return "{root}{delimiter}{users}{delimiter}{user}" \
            .format(root=FORMS_FS_ROOT,
                    delimiter=PATH_SEPARATOR,
                    users=USERS_FOLDER_NAME,
                    user=user_id)
