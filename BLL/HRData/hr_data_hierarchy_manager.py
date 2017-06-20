from Core.Interfaces.HRData.i_hr_data_hierarchy_manager import IHRDataHierarchyManager


class HRDataHierarchyManager(IHRDataHierarchyManager):
    def __init__(self, hierarchy_data_getter):
        self._data = dict(hierarchy_data_getter.get_hierarchy_data())

    def get_corresponding_organizational_role(self, user_organizational_data, role):
        data = self._data
        for organizational_unit in user_organizational_data:
            if role in data[organizational_unit]:
                return data[organizational_unit][role]
            data = data[organizational_unit]
