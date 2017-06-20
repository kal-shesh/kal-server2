import json

from Core import IFormGetter


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
            "schema": {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "description": "",
                "type": "object",
                "properties": {
                    "Soldiers Details": {
                        "type": "object",
                        "properties": {
                            "Personal Info": {
                                "type": "object",
                                "properties": {
                                    "ID": {
                                        "type": "number"
                                    },
                                    "Rank": {
                                        "type": "string",
                                        "minLength": 1,
                                        "enum": ["Private", "Corporal", "Sergeant", "Staff Sergeant", "S.Lieutenant",
                                                 "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel",
                                                 "Brigadier-general"]
                                    },
                                    "Family Name": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "First Name": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Corps": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Unit": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Citizenship": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Family Status": {
                                        "type": "string",
                                        "minLength": 1
                                    },
                                    "Date Of Birth": {
                                        "type": "string",
                                        "format": "date-time"
                                    },
                                    "education": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Medical Profile": {
                                        "type": "number"
                                    },
                                    "Is Permanent": {
                                        "type": "boolean"
                                    },
                                    "Medical Profile set date": {
                                        "type": "string",
                                        "format": "date-time"
                                    },
                                    "Job": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Main Profession": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Main Profession Num": {
                                        "type": "number"
                                    },
                                    "Main Profession Type": {
                                        "type": "string",
                                        "minLength": 3,
                                        "maxLength": 40
                                    },
                                    "Permanent Service Start": {
                                        "type": "string",
                                        "format": "date-time"
                                    },
                                    "Start Of Next Permanent Service": {
                                        "type": "string",
                                        "format": "date-time"
                                    },
                                    "Rank Before Position": {
                                        "type": "string",
                                        "minLength": 1,
                                        "enum": ["Private", "Corporal", "Sergeant", "Staff Sergeant", "S.Lieutenant",
                                                 "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel",
                                                 "Brigadier-general"]
                                    },
                                    "End of Current Commitment": {
                                        "type": "string",
                                        "format": "date-time"
                                    }
                                },
                                "required": [
                                    "ID",
                                    "Rank",
                                    "Family Name",
                                    "First Name",
                                    "Corps",
                                    "Unit",
                                    "Citizenship",
                                    "Family Status",
                                    "Date Of Birth",
                                    "education",
                                    "Medical Profile",
                                    "Is Permanent",
                                    "Medical Profile set date",
                                    "Job",
                                    "Main Profession",
                                    "Main Profession Num",
                                    "Main Profession Type",
                                    "Permanent Service Start",
                                    "Start Of Next Permanent Service",
                                    "Rank Before Position",
                                    "End of Current Commitment"
                                ]
                            },
                            "Soldiers Request": {
                                "type": "object",
                                "properties": {
                                    "Extra Time Added To Service": {
                                        "type": "object",
                                        "properties": {
                                            "Days": {
                                                "type": "number"
                                            },
                                            "Months": {
                                                "type": "number"
                                            },
                                            "Years": {
                                                "type": "number"
                                            },
                                            "In Words": {
                                                "type": "string",
                                                "minLength": 3,
                                                "maxLength": 60
                                            }
                                        },
                                        "required": [
                                            "In Words"
                                        ]
                                    },
                                    "Starting Date": {
                                        "type": "string",
                                        "format": "date-time"
                                    }
                                },
                                "required": [
                                    "Extra Time Added To Service",
                                    "Starting Date"
                                ]
                            },
                            "Reason for the Extension of Service": {
                                "type": "string",
                                "minLength": 3,
                                "maxLength": 40
                            }
                        },
                        "required": [
                            "Personal Info",
                            "Soldiers Request",
                            "Reason for the Extension of Service"
                        ]
                    },
                    "Commander Opinion": {
                        "type": "object",
                        "properties": {
                            "Time Under My Command": {
                                "type": "string",
                                "minLength": 3,
                                "maxLength": 40
                            },
                            "I Approve The Extension of The Service": {
                                "type": "boolean"
                            },
                            "Details and Comments": {
                                "type": "string",
                                "maxLength": 500
                            }
                        },
                        "required": [
                            "Time Under My Command",
                            "I Approve The Extension of The Service",
                            "Details and Comments"
                        ]
                    }
                },
                "required": [
                    "Soldiers Details",
                    "Commander Opinion"
                ]
            },
            "next_steps": [{"step_id": "ddffd", "aprrover": "HEAD OF DEPARTMENT", "step_name": "ishur rashatz", "status": "approved",
                      "next_steps": [{"step_id": "ddffdads", "step_name": "ishur ramad", "aprrover": "HEAD OF BRANCH",
                                      "status": "waiting", "next_steps": []}]}]})

    def get_form(self, form_id):
        return json.dumps({
            "data": {
                "Soldiers Details": {
                    "Personal Info": {
                        "ID": 4408783,
                        "Rank": "Lieutenant",
                        "Family Name": "occaec",
                        "First Name": "sunt ut elit oc",
                        "Corps": "minim laborum i",
                        "Unit": "cupidatat nul",
                        "Citizenship": "sunt eiusmod ea Duis",
                        "Family Status": "incididunt ullamco sed ut",
                        "education": "quis anim tem",
                        "Medical Profile": 53521427,
                        "Is Permanent": True,
                        "Medical Profile set date": "2454-12-21T08:06:40.054Z",
                        "Job": "commo",
                        "Main Profession": "vel",
                        "Main Profession Num": 25628665,
                        "Main Profession Type": "ea dese",
                        "Permanent Service Start": "4281-02-22T14:36:28.908Z",
                        "Start Of Next Permanent Service": "1988-10-22T02:15:51.298Z",
                        "Rank Before Position": "Corporal",
                        "End of Current Commitment": "4890-03-13T00:41:00.890Z",
                        "Date Of Birth": "2881-07-20T03:08:29.840Z"
                    },
                    "Soldiers Request": {
                        "Extra Time Added To Service": {
                            "In Words": "ipsum non adipisicing occaecat in"
                        },
                        "Starting Date": "3150-07-30T23:45:24.868Z"
                    },
                    "Reason for the Extension of Service": "occaecat pariatur nostrud"
                },
                "Commander Opinion": {
                    "Time Under My Command": "consectetur nisi ipsum velit",
                    "I Approve The Extension of The Service": False,
                    "Details and Comments": "dolore qui id"
                }
            },
            "form_metadata": {
                "next_steps": [{"step_id": "ddffd", "aprrover": "ssss", "step_name": "ishur rashatz", "status": "approved",
                           "next_steps": [{"step_id": "ddffdads", "step_name": "ishur rashatz", "aprrover": "aaassss",
                                           "status": "waiting", "next_steps": []}]}],
                "form_type": "haaracha"
            },
            "uuid": "666"
        })

    def get_all_active_forms(self, user_id):
        return json.dumps({"forms": [{
            "data": {"Soldiers Details": {
                "Personal Info": {
                    "ID": 4408783,
                    "Rank": "Lieutenant",
                    "Family Name": "occaec",
                    "First Name": "sunt ut elit oc",
                    "Corps": "minim laborum i",
                    "Unit": "cupidatat nul",
                    "Citizenship": "sunt eiusmod ea Duis",
                    "Family Status": "incididunt ullamco sed ut",
                    "education": "quis anim tem",
                    "Medical Profile": 53521427,
                    "Is Permanent": True,
                    "Medical Profile set date": "2454-12-21T08:06:40.054Z",
                    "Job": "commo",
                    "Main Profession": "vel",
                    "Main Profession Num": 25628665,
                    "Main Profession Type": "ea dese",
                    "Permanent Service Start": "4281-02-22T14:36:28.908Z",
                    "Start Of Next Permanent Service": "1988-10-22T02:15:51.298Z",
                    "Rank Before Position": "Corporal",
                    "End of Current Commitment": "4890-03-13T00:41:00.890Z",
                    "Date Of Birth": "2881-07-20T03:08:29.840Z"
                },
                "Soldiers Request": {
                    "Extra Time Added To Service": {
                        "In Words": "ipsum non adipisicing occaecat in"
                    },
                    "Starting Date": "3150-07-30T23:45:24.868Z"
                },
                "Reason for the Extension of Service": "occaecat pariatur nostrud"
            },
                "Commander Opinion": {
                    "Time Under My Command": "consectetur nisi ipsum velit",
                    "I Approve The Extension of The Service": False,
                    "Details and Comments": "dolore qui id"
                }
            },
            "form_metadata": {
                "next_steps": [{"step_id": "ddffd", "aprrover": "ssss", "step_name": "ishur rashatz", "status": "approved",
                           "next_steps": [{"step_id": "ddffdads", "step_name": "ishur rashatz", "aprrover": "aaassss",
                                           "status": "waiting", "next_steps": []}]}],
                "form_type": "haaracha",
                "creation_time": "2017-06-19 11:45:00",
                "last_update_time": "2017-06-19 11:45:00",
                "creator_id": "1233",
                "displayName": "haaracha"
            },
            "uuid": "666"
        }]})

    def get_all_waiting_forms(self, user_id):
        return json.dumps({"forms": [{
            "data": {"Soldiers Details": {
                "Personal Info": {
                    "ID": 4408783,
                    "Rank": "Lieutenant",
                    "Family Name": "occaec",
                    "First Name": "sunt ut elit oc",
                    "Corps": "minim laborum i",
                    "Unit": "cupidatat nul",
                    "Citizenship": "sunt eiusmod ea Duis",
                    "Family Status": "incididunt ullamco sed ut",
                    "education": "quis anim tem",
                    "Medical Profile": 53521427,
                    "Is Permanent": True,
                    "Medical Profile set date": "2454-12-21T08:06:40.054Z",
                    "Job": "commo",
                    "Main Profession": "vel",
                    "Main Profession Num": 25628665,
                    "Main Profession Type": "ea dese",
                    "Permanent Service Start": "4281-02-22T14:36:28.908Z",
                    "Start Of Next Permanent Service": "1988-10-22T02:15:51.298Z",
                    "Rank Before Position": "Corporal",
                    "End of Current Commitment": "4890-03-13T00:41:00.890Z",
                    "Date Of Birth": "2881-07-20T03:08:29.840Z"
                },
                "Soldiers Request": {
                    "Extra Time Added To Service": {
                        "In Words": "ipsum non adipisicing occaecat in"
                    },
                    "Starting Date": "3150-07-30T23:45:24.868Z"
                },
                "Reason for the Extension of Service": "occaecat pariatur nostrud"
            },
                "Commander Opinion": {
                    "Time Under My Command": "consectetur nisi ipsum velit",
                    "I Approve The Extension of The Service": False,
                    "Details and Comments": "dolore qui id"
                }
            },
            "form_metadata": {
                "next_steps": [{"step_id": "ddffd", "aprrover": "ssss", "step_name": "ishur rashatz", "status": "approved",
                           "next_steps": [{"step_id": "ddffdads", "step_name": "ishur rashatz", "aprrover": "aaassss",
                                           "status": "waiting", "next_steps": []}]}],
                "form_type": "haaracha",
                "creation_time": "2017-06-19 11:45:00",
                "last_update_time": "2017-06-19 11:45:00",
                "creator_id": "1233",
                "displayName": "haaracha"
            },
            "uuid": "666"
        }]})
