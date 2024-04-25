import requests
from flask import Flask, render_template, request


app = Flask(__name__)




@app.get("/")
def choice():
    actions = ["/random_int", "/random_item_from_list", "/current_date"]
    return render_template("choice.html", actions=actions)

@app.post("/actions")
def action():
    form_result = request.form["action"]
    result = requests.get("http://127.0.0.1:5000" + f"{form_result}").json()
    return render_template("action.html", result=result)



