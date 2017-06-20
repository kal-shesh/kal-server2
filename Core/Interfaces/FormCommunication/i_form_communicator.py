class IFormCommunicator(object):
    def create_form(self, form):
        raise NotImplementedError()

    def update_form(self, form):
        raise NotImplementedError()

    def get_form(self, form_id):
        raise NotImplementedError()

    def get_all_active_forms_by_user(self, user_id):
        raise NotImplementedError()

    def get_all_awaiting_forms_by_user(self, user_id):
        raise NotImplementedError()