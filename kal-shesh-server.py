from flask import Flask, request
from flask_cors import CORS, cross_origin
from BLL.Forms import *

# from Forms import *

app = Flask(__name__)
CORS(app)
form_getter = MockFormGetter()
form_executor = MockFormExecutor()


@app.route("/forms", methods=['GET'])
def get_all_available_forms():
    # return Forms.get_all_forms()
    return form_getter.get_all_forms()


@app.route("/forms/<id>", methods=['GET'])
def get_form(id):
    response = form_getter.get_form(id)
    return response
    # return Forms.get_all_forms()


@app.route("/forms/active/<user_id>", methods=['POST'])
def create_form(user_id):
    # writing to file and to user_id file
    form_executor.create_form(user_id, request.data)


@app.route("/forms/active/update/user=<user_id>&form_id=<form_id>", methods=['POST'])
def update_step(user_id, form_id):
    # writing to file and to user_id file
    form_executor.update_step(user_id, form_id, request.data)


@app.route("/forms/active/my/<user_id>", methods=['GET'])
def get_forms_by_user_id(user_id):
    # writing to file and to user_id file
    pass


@app.route("/forms/active/my/form_id=<form_id>", methods=['GET'])
def get_form_by_user_id(form_id):
    # writing to file and to user_id file
    pass


@app.route("/forms/active/waiting/<user_id>", methods=['GET'])
def get_waiting_forms_by_user_id(user_id):
    # writing to file and to user_id file
    pass


@app.route("/HRdata/=<hr_id>", methods=['GET'])
def get_user_data(hr_id):
    # return HRdata.get_human(id)
    return "id: {}".format(hr_id)


if __name__ == '__main__':
    app.run()
