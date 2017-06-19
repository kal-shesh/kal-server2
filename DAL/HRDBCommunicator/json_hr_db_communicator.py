import json

from Core.Keys.hr_data_keys import *
from Core.Interfaces.i_hr_data_getter import IHRDataGetter

# Mock Data Path
MOCK_HR_DATA_DB_PATH = "mock_elaborate.json"


class JsonHrDbCommunicator(IHRDataGetter):
    def __init__(self):
        self._data = self._get_data_mock(MOCK_HR_DATA_DB_PATH)

    def get_hr_data_by_id(self, id_number):
        if id_number in self._data:
            try:
                return json.dumps(self._data[id_number])
            except Exception as e:
                pass
        return None

    @staticmethod
    def _get_data_mock(path):
        hr_data = dict()
        with open(path, "rb") as fp:
            try:
                data = json.loads(fp)
            except Exception as e:
                print e
                return None

        for person in data:
            hr_data[person[ID_NUMBER]] = person
        return hr_data
