class IFormExecutor:
    def create_form(self, user_id, form_data):
        raise NotImplementedError

    def update_step(self, user_id, form_id):
        raise NotImplementedError
