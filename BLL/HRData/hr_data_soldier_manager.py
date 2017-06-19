import json


from Core.Interfaces.HRData.i_hr_soldier_data_manager import IHRSoldiersDataManager


class HRSoldiersDataManager(IHRSoldiersDataManager):
    def __init__(self, soldier_data_getter):
        self._data = soldier_data_getter.get_soldiers_data()

    def get_hr_soldier_data_by_id(self, id_number):
        if id_number in self._data:
            try:
                return json.dumps(self._data[id_number])
            except Exception as e:
                pass
        return None

