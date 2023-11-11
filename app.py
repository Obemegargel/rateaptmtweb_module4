from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')#this gave some trouble but figured it out

@app.route('/submit', methods=['POST'])
def submit():
    lastapartmentname = request.form['lastapartmentname']
    lasthousingtype = request.form['lasthousingtype']
    laststarrating = request.form['laststarrating']
    pastcost = request.form['pastcost']
    nextapartmentname = request.form['nextapartmentname']
    nextsemestername = request.form['nextsemestername']
    nextcost = request.form['nextcost']

    with open('data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([lastapartmentname, lasthousingtype, laststarrating, pastcost, nextapartmentname, nextsemestername, nextcost])

    return redirect(url_for('index'))





import csv #testing something
@app.route('/datadisplay')
def other():#I could have named this function datadisplay instead of other because it is just a name but would have to change it in form.html accordingly

    with open('data.csv', 'r') as csv_file:#testing something
        csv_reader = csv.reader(csv_file)#testing something
        data = list(csv_reader)#testing something

    return render_template('datadisplay.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
    