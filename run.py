import os, sys
from flask import Flask, Response, request, render_template, redirect, \
url_for, render_template_string

from model.rest_crud import create_new_rest, \
edit_rest_id, delete_rest, listrest, find_rest_name_by_id

app = Flask(__name__)

#Get configuration settings
#app.config.from_object(config_file)
#app.config.from_envvar('APP_CONFIG', silent=True)

@app.route('/')
def restlist():
    return "New Restarant Service HomePage"


##All Restaurant Object Operations
#create - new restaurant
@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'GET':
        path = os.path.join(os.getcwd(), 'web','templates', 'rest', 'new.html')
        return render_template_string(open(path).read())
    elif request.method == 'POST':
        rest_name = request.form['restaurantname']
        create_new_rest(rest_name)
        return redirect(url_for('listall'))

#read - list all restaurants
@app.route('/listall')
def listall():
    rest_list = listrest()
    print "rest list is"
    print rest_list
    if rest_list:
        path = os.path.join(os.getcwd(), 'web','templates', 'rest', 'listrest.html')
        return render_template_string(open(path).read(),  rest_list=rest_list)
        #following Works
        #for r in rest_list:
        #    return str(r.name)
    else: return "Nothing!"

#update - edit existing restaurants
@app.route('/update/<int:rest_id>', methods=['POST', 'GET'])
def update(rest_id):
    rest = find_rest_name_by_id(rest_id)
    if request.method == 'GET':
        path = os.path.join(os.getcwd(), 'web','templates', 'rest', 'update.html')
        return render_template_string(open(path).read(), rest=rest)
    elif request.method == 'POST':
        new_rest_name = request.form['new_name']    
        edit_rest_id(rest_id, new_rest_name)
        return redirect(url_for('listall'))
    
#delete - delete a restaurant
@app.route('/delete/<int:rest_id>', methods=['POST', 'GET'])
def delete(rest_id):
    rest = find_rest_name_by_id(rest_id)
    if request.method == 'GET':
        path = os.path.join(os.getcwd(), 'web','templates', 'rest', 'delete.html')
        return render_template_string(open(path).read(), rest=rest)
    elif request.method == 'POST':
        confirm = request.form['submit']    
        if confirm == "Yes":
            delete_rest(rest_id)
        return redirect(url_for('listall'))

##All Restaurant Object Operations END


if __name__ == "__main__":
    port = 8080
    hostname = '0.0.0.0'
    app.run(debug=True, port = port, host=hostname)