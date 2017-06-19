import json

from Core.Interfaces.HRData.i_hr_hierarchy_data_getter import IHRHierarchyDataGetter

# Mock Data Path
MOCK_HR_HIERARCHY_DATA_DB_PATH = "hierarchy_data.json"


class JsonHrHierarchyDbCommunicator(IHRHierarchyDataGetter):
    def __init__(self):
        pass

    def get_hierarchy_data(self):
        self._get_data_mock(MOCK_HR_HIERARCHY_DATA_DB_PATH)

    @staticmethod
    def _get_data_mock(path):
        with open(path, "rb") as fp:
            try:
                data = json.loads(fp)
            except Exception as e:
                print e
                return None
        return data
