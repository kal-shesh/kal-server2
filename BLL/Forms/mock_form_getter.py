import json
from i_form_getter import IFormGetter


class MockFormGetter(IFormGetter):
    def get_all_forms_types(self):
        return json.dumps(
            {"forms": [{"id": "hul", "displayName": "tofesHul", "description": "a form to ask premission to hul",
                        "jpeg": "http://files.softicons.com/download/web-icons/free-web-icon-pack-1-by-rockettheme/png/128x128/earth.png"},
                       {"id": "haaracha", "displayName": "tofes haarachat keva",
                        "description": "a form to ask premission to hul",
                        "jpeg": "http://files.softicons.com/download/holidays-icons/desktop-halloween-icons-by-aha-soft/png/128x128/Death.png"}]})

    def get_form_type(self, type_id):
        return json.dumps({
            "id": "haaracha",
            "displayName": "tofes haarachat keva",
            "description": "a form to ask premission to hul",
            "jpeg": "http://files.softicons.com/download/holidays-icons/desktop-halloween-icons-by-aha-soft/png/128x128/Death.png",
            "schema": {"$schema": "http://json-schema.org/draft-04/schema#",
                       "definitions": {},
                       "id": "http://example.com/example.json",
                       "properties": {
                           "Soldiers Request": {
                               "id": "/properties/Soldiers Request",
                               "properties": {
                                   "Citizenship": {
                                       "id": "/properties/Soldiers Request/properties/Citizenship",
                                       "type": "string"
                                   },
                                   "Corps": {
                                       "id": "/properties/Soldiers Request/properties/Corps",
                                       "type": "string"
                                   },
                                   "DOB": {
                                       "id": "/properties/Soldiers Request/properties/DOB",
                                       "type": "string"
                                   },
                                   "Family Name": {
                                       "id": "/properties/Soldiers Request/properties/Family Name",
                                       "type": "string"
                                   },
                                   "Family Status": {
                                       "id": "/properties/Soldiers Request/properties/Family Status",
                                       "type": "string"
                                   },
                                   "First Name": {
                                       "id": "/properties/Soldiers Request/properties/First Name",
                                       "type": "string"
                                   },
                                   "ID": {
                                       "id": "/properties/Soldiers Request/properties/ID",
                                       "type": "integer"
                                   },
                                   "Is Perminent": {
                                       "id": "/properties/Soldiers Request/properties/Is Perminent",
                                       "type": "boolean"
                                   },
                                   "Job": {
                                       "id": "/properties/Soldiers Request/properties/Job",
                                       "type": "string"
                                   },
                                   "Main Profession": {
                                       "id": "/properties/Soldiers Request/properties/Main Profession",
                                       "type": "string"
                                   },
                                   "Main Profession Num": {
                                       "id": "/properties/Soldiers Request/properties/Main Profession Num",
                                       "type": "integer"
                                   },
                                   "Main Profession Type": {
                                       "id": "/properties/Soldiers Request/properties/Main Profession Type",
                                       "type": "string"
                                   },
                                   "Medical Profile": {
                                       "id": "/properties/Soldiers Request/properties/Medical Profile",
                                       "type": "integer"
                                   },
                                   "Medical Profile set date": {
                                       "id": "/properties/Soldiers Request/properties/Medical Profile set date",
                                       "type": "string"
                                   },
                                   "Permanent Service Start": {
                                       "id": "/properties/Soldiers Request/properties/Permanent Service Start",
                                       "type": "string"
                                   },
                                   "Rank": {
                                       "id": "/properties/Soldiers Request/properties/Rank",
                                       "type": "string"
                                   },
                                   "Unit": {
                                       "id": "/properties/Soldiers Request/properties/Unit",
                                       "type": "string"
                                   },
                                   "education": {
                                       "id": "/properties/Soldiers Request/properties/education",
                                       "type": "string"
                                   }
                               },
                               "type": "object"
                           }
                       },
                       "type": "object"
                       }})

    def get_form(self, form_id):
        return json.dumps({
            "data": {
                "Soldiers Request": {
                    "ID": 8161702,
                    "Rank": "SLT",
                    "Family Name": "Schreiber",
                    "First Name": "Daniel",
                    "Corps": "Daniel",
                    "Unit": "Daniel",
                    "Citizenship": "Daniel",
                    "Family Status": "S",
                    "DOB": "01/08/1996",
                    "education": "non",
                    "Medical Profile": 64,
                    "Is Perminent": True,
                    "Medical Profile set date": "04/02/2015",
                    "Job": "Programer",
                    "Main Profession": "Officer",
                    "Main Profession Num": 1,
                    "Main Profession Type": "Cyber",
                    "Permanent Service Start": "03/02/2018"
                }},
            "metadata": {
                "steps": [{"step_id": "ddffd", "aprrover": "ssss", "step_name": "ishur rashatz", "status": "approved",
                           "next_steps": [{"step_id": "ddffdads", "step_name": "ishur rashatz", "aprrover": "aaassss",
                                           "status": "waiting"}]}]
            }
        })

    def get_all_active_forms(self, user_id):
        return json.dumps({"forms": []})

    def get_all_waiting_forms(self, user_id):
        return json.dumps({"forms": []})
