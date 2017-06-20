class IEmptyFormCommunicator:
    def get_all_forms_types(self):
        raise NotImplementedError

    def get_form_type(self, type_id):
        raise NotImplementedError

    def get_form(self, form_id):
        raise NotImplementedError

    def get_all_active_forms(self, user_id):
        raise NotImplementedError

    def get_all_waiting_forms(self, user_id):
        raise NotImplementedError

