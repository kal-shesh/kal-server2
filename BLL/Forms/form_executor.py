from Core import IFormExecutor
from Core.Interfaces.Forms import IFormGetter
from Core.Models import *
import json
import datetime
import traceback


class FormExecutor(IFormExecutor):
    def __init__(self, form_getter):
        self.form_getter = form_getter  # type: IFormGetter

    def create_form(self, user_id, form_data):
        # type (str, dict) -> None
        form_data = json.loads(form_data)
        form_schema = json.loads(self.form_getter.get_form_type(form_data['id']))
        form_schema_keys = self.__get_default_dictionary_by_schema(form_schema['schema']['properties'])
        partial_form_data = form_data['data']
        full_form_data = self.__complete_dictionary_by_schema_dictionary(partial_form_data, form_schema_keys)
        form_data['data'] = full_form_data
        self.__generate_metadata(form_data, form_schema)
        return json.dumps(full_form_data)

    def update_step(self, user_id, form_id, data):
        raise NotImplementedError

    def __get_default_dictionary_by_schema(self, dictionary):
        result = {}
        for key in dictionary:
            if dictionary[key]['type'] != 'object':
                result[key] = ""
            else:
                result[key] = self.__get_default_dictionary_by_schema(dictionary[key]['properties'])
        return result

    def __complete_dictionary_by_schema_dictionary(self, dictionary, schema_dictionary):
        for key in schema_dictionary:
            if key not in dictionary:
                dictionary[key] = schema_dictionary[key]
            elif type(schema_dictionary[key]) is type(dict):
                dictionary[key] = self.__complete_dictionary_by_schema_dictionary(dictionary[key],
                                                                                  schema_dictionary[key])
        return dictionary

    def __generate_metadata(self, form_data, form_type_data):
        form_data['metadata'] = {key: value for key, value in form_type_data if key != 'shcema'}
        time = str(datetime.datetime.now())
        form_data['metadata']['creation_time'] = time
        form_data['metadata']['last_update_time'] = time
        metadata = FormMetadata()