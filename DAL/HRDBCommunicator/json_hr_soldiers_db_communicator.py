import json

from Core.Interfaces.HRData.i_hr_soldiers_data_getter import IHRSoldierDataGetter
from Core.Keys.hr_soldier_data_keys import *

# Mock Data Path
MOCK_HR_SOLDIERS_DATA_DB_PATH = "soldiers_data.json"


class JsonHrSoldiersDbCommunicator(IHRSoldierDataGetter):
    def __init__(self):
        pass

    def get_soldiers_data(self):
        self._get_data_mock(MOCK_HR_SOLDIERS_DATA_DB_PATH)

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
            hr_data[person[ID_NUMBER_KEY]] = person
        return hr_data
