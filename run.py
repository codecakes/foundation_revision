import os, sys
from flask import Flask, Response, request, render_template, redirect, url_for, \
render_template_string

from model.rest_crud import create_new_rest, find_rest, edit_rest_name, \
delete_rest, listrest

app = Flask(__name__)

#Get configuration settings
#app.config.from_object(config_file)
#app.config.from_envvar('APP_CONFIG', silent=True)

@app.route('/')
def restlist():
    return "Hello"

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'GET':
        path = os.path.join(os.getcwd(), 'web','templates', 'new.html')
        return render_template_string(open(path).read())
    elif request.method == 'POST':
        rest_name = request.form['restaurantname']
        create_new_rest(rest_name)
        return redirect(url_for('listall'))

@app.route('/listall')
def listall():
    rest_list = listrest()
    print "rest list is"
    print rest_list
    if rest_list:
        path = os.path.join(os.getcwd(), 'web','templates', 'listrest.html')
        return render_template_string(open(path).read(),  rest_list=rest_list)
        #following Works
        #for r in rest_list:
        #    return str(r.name)
    else: return "Nothing!"
    
    
    

if __name__ == "__main__":
    port = 8080
    hostname = '0.0.0.0'
    app.run(debug=True, port = port, host=hostname)