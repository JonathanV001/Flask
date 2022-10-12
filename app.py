from datetime import date, datetime
from urllib import request
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, static_url_path='/static')
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {}


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = date.today()
    time = datetime.now()
    timeStr = time.strftime("%H:%M:%S")
    return render_template('index.html', currentDate=currentDate, time=timeStr)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST', 'GET'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    # Write your to code here to check whether number is even or odd and render result.html page
    if(number == None):
        # dont understand render template
        string = "No number provided"
        return render_template("result.html", string=string)
    elif(str.isdigit(number) == False):
        string = "Provided input is not an integer"
        return render_template("result.html", string=string)
    elif(int(number) % 2 == 0):
        string = "Number " + number + " is even"
        return render_template("result.html", string=string)
    elif(int(number) % 2 != 0):
        string = "Number " + number + " is odd"
        return render_template("result.html", string=string)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST', 'GET'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    organisation = request.form['orgList']
    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = organisation


    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
