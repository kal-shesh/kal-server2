class IUsersCommunicator(object):
    def update_user_active_forms_file(self, user_id, changes):
        raise NotImplementedError()

    def update_user_awaiting_forms_file(self, user_id, changes):
        raise NotImplementedError()

    def get_user_active_forms_ids(self, user_id):
        raise NotImplementedError()

    def get_user_awaiting_forms_ids(self, user_id):
        raise NotImplementedError()
