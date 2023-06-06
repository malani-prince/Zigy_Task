from app import app
from models.text_model import text_model
from flask import request, render_template, jsonify, make_response, send_file, redirect

obj = text_model()

# Task-1: 
# insted of < zigy.in/1 > I use < '/insert_text' >
# Multiple Text Box Insert
# with that Check List for each BLock < Default Value 1(Task Not completed) >

# Insert
@app.route('/insert_text', methods=['GET', 'POST'])
def insert_into_data():
    return render_template('insert_data.html')

# display the inserted data and create the entry into database as well
@app.route('/display', methods=['POST'])
def display_text():
    data = request.form['text']
    tf = obj.insert_models(data)
    if tf:
        return render_template('Display.html', DATA = data)
    else:
        return {
            "message": "enter Valid Data.....!"
        }


# task-2: Check List Boxes

# display all the data inside the Database
# Get ALL Data
@app.route("/Display_all_data")
def display_data():
    data = obj.data_return()
    return render_template('all_data.html', DATA = data)

# Update List
@app.route('/update_list')
def update_controller():
    data = obj.data_return()
    return render_template("update_data.html", DATA=data)

@app.route("/update_list/update", methods=['POST'])
def update_route():
    id = request.form['id']
    x = int(id)
    dq = obj.find_data_models(x)
    if dq:
        data = obj.data_return()
        return render_template('all_data.html', DATA = data)
    else:
        return "enter valid id"