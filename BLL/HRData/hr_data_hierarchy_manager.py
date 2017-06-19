from Core.Interfaces.HRData.i_hr_data_hierarchy_manager import IHRDataHierarchyManager
from Core.Keys.hr_soldier_data_keys import TEAM_KEY, DEPARTMENT_KEY, BRANCH_KEY, UNIT_KEY, DIVISION_KEY


class HRDataHierarchyManager(IHRDataHierarchyManager):
    def __init__(self, hierarchy_data_getter):
        self._data = hierarchy_data_getter.get_hierarchy_data()

    def get_corresponding_organizational_role(self, user_organizational_data, role):
        for organizational_unit in user_organizational_data:
            if role in self._data[user_organizational_data[organizational_unit]]:
                return self._data[role]
