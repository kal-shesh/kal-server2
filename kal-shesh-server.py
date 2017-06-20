from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
from BLL import *
from DAL import *

# from Forms import *

from Core.system_consts import PATH_SEPARATOR
MATCHER_PATH = ".{delimiter}Core{delimiter}Configs{delimiter}display_name_to_hr_data_mapping.json".format(delimiter=PATH_SEPARATOR)

app = Flask(__name__)
CORS(app)
hr_dal = JsonHrSoldiersDbCommunicator()
hirarchy_data_getter = JsonHrHierarchyDbCommunicator()
user_commincator = FormsFSUserCommunicator()
form_commincator = FormsFSFormCommunicator(user_commincator)
hr_data_manager = HRSoldiersDataManager(hr_dal)
hr_hirarchy_manager = HRDataHierarchyManager(hirarchy_data_getter)
form_getter = MockFormGetter()
my_form_executor = FormExecutor(form_getter, form_commincator, user_commincator, hr_data_manager, hr_hirarchy_manager)
#my_form_executor = MockFormExecutor()
hr_getter = HRSoldiersDataManager(hr_dal)
with open(MATCHER_PATH, "rb") as matcher_fp:
    adapter = DisplayNameToHRServerClientDataExchangeMatcher(json.load(matcher_fp)['mapping'])


@app.route("/forms", methods=['GET'])
def get_all_available_forms():
    # return Forms.get_all_forms()
    return form_getter.get_all_forms_types()


@app.route("/forms/<type_id>", methods=['GET'])
def get_form(type_id):
    response = form_getter.get_form_type(type_id)
    return response
    # return Forms.get_all_forms()


@app.route("/forms/active/<user_id>", methods=['POST'])
def create_form(user_id):
    # writing to file and to user_id file
    data = my_form_executor.create_form(user_id, request.data)
    if data:
        return "succeeded"


@app.route("/forms/active/update/user=<user_id>&form_id=<form_id>", methods=['POST'])
def update_step(user_id, form_id):
    # writing to file and to user_id file
    form_executor.update_step(user_id, form_id, request.data)


@app.route("/forms/active/my/user_id=<user_id>", methods=['GET'])
def get_forms_by_user_id(user_id):
    # writing to file and to user_id file
    return form_getter.get_all_active_forms(user_id)


@app.route("/forms/active/my/form_id=<form_id>", methods=['GET'])
def get_form_by_user_id(form_id):
    # writing to file and to user_id file
    return form_getter.get_form(form_id)


@app.route("/forms/active/waiting/<user_id>", methods=['GET'])
def get_waiting_forms_by_user_id(user_id):
    # writing to file and to user_id file
    return form_getter.get_all_waiting_forms(user_id)


@app.route("/HRdata/<user_id>", methods=['GET'])
def get_user_data(user_id):
    result = hr_getter.get_hr_soldier_data_by_id(user_id)
    for key in result.keys():
        new_key = adapter.match_server_to_client(key)
        data = result[key]
        del result[key]
        result[new_key] = data
    return json.dumps(result)


if __name__ == '__main__':
    app.run()
