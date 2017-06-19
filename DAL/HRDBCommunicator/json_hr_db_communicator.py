import json

# Mock Data Path
MOCK_HR_DATA_DB_PATH="mock_elaborate.json"

class JsonHrDbCommunicator(object):
    def __init__(self):
        self._data = self._get_data_mock(MOCK_HR_DATA_DB_PATH)

    def get_hr_data_by_key(self, id, key):
        pass

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
            pass
