from Core.Interfaces.Forms.i_form_executor import IFormExecutor


class MockFormExecutor(IFormExecutor):
    def create_form(self, user_id, form_data):
        pass

    def update_step(self, user_id, form_id, data):
        print user_id + form_id + data
        pass
