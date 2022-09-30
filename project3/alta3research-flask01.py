#!/usr/bin/python3

# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
import yaml
import json


# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

rickmortychars = [{
    "name": "Rick Sanchez",
    "first episode appearence" : "Pilot",
    "birthday" : "January 26",
    "age" : "70",
    "species" : "human"
    },
    {
    "name" : "Morty Smith",
    "first episode appearence" : "Pilot",
    "birthday" : "Septmember 19",
    "age" : "14",
    "species" : "human"
        },
    {
    "name": "Mr. Meeseeks",
    "first episode appearence" : "Meeseeks and Destroy",
    "birthday" : "unknown",
    "age" : "unknown",
    "species" : "artificial humanoid " 
        },
    {
    "name" : "snuffles",
    "first episode appearance" : "Total Rickall",
    "birthday" : "unknown ",
    "age" : "unknown",
    "species" : "dog"
        }]

## This is where we want to redirect users to
@app.route("/success/<username>")
def success(username):
    return render_template("project3.html", name = username)

@app.route("/") # user can land at "/"
@app.route("/landing") # or user can land at "/landing"
def landing():
    return render_template("login.html") # look for templates/postmaker.html
# This is where login.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("username"): # if nm was assigned via the POST
            user = request.form.get("username") # grab the value of username from the POST
        else: # if a user sent a post without username then assign value defaultuser
            user = "Pete"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("username"): # if nm was assigned as a parameter=value
            user = request.args.get("username") # pull username from localhost:5060/login?nm=larry
        else: # if username was not passed...
            user = "Pete" # ...then user is just Pete
    return redirect(url_for("success", username = user)) # pass back to /success with val for username

@app.route("/alterego/<altersuper>,<real>,<superpower>,<secondpow>,<altergadget>,<transport>")
#once form from enterego is submitted, redirect here with the data from form and render correct template using jinja
def alterego(altersuper,real,superpower,secondpow,altergadget,transport):
    return render_template("alter.html", supernm = altersuper, realnm = real, superpow = superpower,secondarypow = secondpow,gadget = altergadget,transportation = transport)
#route for post/form to grab all values from the form
@app.route("/enterego", methods= ["POST","GET"])
def enterego():
    #if method post grab values from form input and assign variables
    if request.method == "POST":
            supername = request.form.get("alterSuperName")
            realname = request.form.get("alterRealName")
            power = request.form.get("power")
            secondaryPower = request.form.get("secondaryPower")
            gadget = request.form.get("gadget")
            transportation = request.form.get("transportation")
    elif request.method == "GET":
        redirect(url_for("success"))
    return redirect(url_for("alterego", altersuper = supername, real = realname, superpower = power, secondpow = secondaryPower, altergadget = gadget, transport = transportation))
# route to grab data from our api and to post new data to api
@app.route("/rickmortydata", methods = ["GET","POST"])
def data():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            name = data["name"]
            firstapp = data["first episode appearance"]
            birthday = data["birthday"]
            age = data["age"]
            species = data["species"]
            rickmortychars.append({"name":name,"first episode appearance":firstapp,"birthday":birthday,"age":age,"species":species})
    #returns legal JSON
    return jsonify(rickmortychars)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)
