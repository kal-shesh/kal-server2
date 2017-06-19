import json
from i_hr_getter import IHRGetter


class MockHRGetter(IHRGetter):
    def get_user_details(self, user_id):
        return json.dumps(
            {
                "ENTITY_TYPE": "Soldier",
                "FIRST_NAME": "MIAH",
                "PERSONAL_NUMBER": "3b4b05b8-03ca-4a2f-a76f-9008170eeb6f",
                "ID_NUMBER": "e6866cd1-dd6d-4ab4-af4d-b22a70907ad6",
                "LAST_NAME": "VALENZUELA",
                "USER_NAME": "miahvalenzuel9716",
                "RANK": "\"Beginner\"",
                "SERVICE_TYPE": "Post",
                "BIRTH_DATE": "1991-01-01",
                "SEX": "f",
                "RELEASE_DATE": "2017-02-07",
                "ADDRESS": "6730 SUNNYSIDE",
                "TAFKID": "Mefaket",
                "VOIP_PHONE": "0509",
                "CELL_PHONE": "(814) 747-6198"
            })
