from Core import IFormGetter
import json


class FormGetter(IFormGetter):
    def __init__(self):
        pass

    def get_all_forms_types(self):
        return json.dumps(
            {"forms": [{"id": "hul", "displayName": "tofesHul", "description": "a form to ask premission to hul",
                        "jpeg": "http://files.softicons.com/download/web-icons/free-web-icon-pack-1-by-rockettheme/png/128x128/earth.png"},
                       {"id": "haaracha", "displayName": "tofes haarachat keva",
                        "description": "a form to ask premission to hul",
                        "jpeg": "http://files.softicons.com/download/holidays-icons/desktop-halloween-icons-by-aha-soft/png/128x128/Death.png"}]})

    def get_form_type(self, type_id):
        raise NotImplementedError

    def get_form(self, form_id):
        raise NotImplementedError

    def get_all_active_forms(self, user_id):
        raise NotImplementedError

    def get_all_waiting_forms(self, user_id):
        raise NotImplementedError
