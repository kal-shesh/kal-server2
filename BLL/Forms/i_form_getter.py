class IFormGetter:
    def get_all_forms(self):
        raise NotImplementedError

    def get_form(self, id):
        raise NotImplementedError
