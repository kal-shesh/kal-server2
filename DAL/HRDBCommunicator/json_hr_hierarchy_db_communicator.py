import json

from Core.Interfaces.HRData.i_hr_hierarchy_data_getter import IHRHierarchyDataGetter
from Core.system_consts import PATH_SEPARATOR

# Mock Data Path
MOCK_HR_HIERARCHY_DATA_DB_PATH = ".{delimiter}DAL{delimiter}HRDBCommunicator{delimiter}hierarchy_data.json".format(delimiter=PATH_SEPARATOR)


class JsonHrHierarchyDbCommunicator(IHRHierarchyDataGetter):
    def __init__(self):
        pass

    def get_hierarchy_data(self):
        return self._get_data_mock(MOCK_HR_HIERARCHY_DATA_DB_PATH)

    @staticmethod
    def _get_data_mock(path):
        with open(path, "rb") as fp:
            try:
                data = json.load(fp)
            except Exception as e:
                print e
                return None
        return data
