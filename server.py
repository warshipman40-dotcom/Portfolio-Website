#must use the right interpreter Venc
from flask import Flask, render_template, request, redirect
import os
import csv
#creates an instance of a flask object
app = Flask(__name__)
#.\.venv\Scripts\Activate.ps1
#$env:FLASK_APP="server.py"
#$env:FLASK_DEBUG = "1"
#flask run

#curly brackets {{}} dynamically update
#e.g {{4 + 5}} shows as 9

#css and js files are usually static when we send them (don't change)
#files have to be stored as static/style.css
#flask passes <username> into the function
#when somebody visits this url, run the function below
@app.route("/")
def my_home():
    #flask render_template tries to look in a folder called templates
    return render_template("index.html")

#dynamically accepts differnet URL parameters and stores in page_name
#e.g somebody visits "aboutme.html" returns render_template("aboutme.html")
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open("database.txt", mode = "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data):
    with open("database.csv", mode = "a", newline = "") as csv_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csv_database, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #we use post because get data is visible in URL
    #we also use post because the user submits data to our server
    if request.method == "POST":
        #request.form returns the data the user submitted
        #turning form data into a dictionary
        data = request.form.to_dict()
        write_to_csv(data)
        #redirects to our html file
        return redirect("thankyou.html")
    else:
        return "Something went wrong! Try again!"
    

#os.startfile("http://127.0.0.1:5000")