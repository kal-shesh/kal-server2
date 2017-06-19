from flask import Flask
from flask_cors import CORS, cross_origin
import json
from BLL.Forms import *

# from Forms import *

app = Flask(__name__)
CORS(app)
form_getter = MockFormGetter()


@app.route("/forms")
def get_all_avilable_forms():
    # return Forms.get_all_forms()
    return form_getter.get_all_forms()


@app.route("/forms/<id>")
def get_form(id):
    response = form_getter.get_form(id)
    print response
    return response
    # return Forms.get_all_forms()


@app.route("/HRdata/hr_id=<hr_id>&form_id=<form_id>")
def get_all_hr_data_for_form(hr_id, form_id):
    # return HRdata.get_human(id)
    return "id: {}, form_id:{}".format(hr_id, form_id)


@app.route("/forms3")
def get_all_aforms():
    pass
    # return Forms.get_all_forms()


if __name__ == '__main__':
    app.run()
