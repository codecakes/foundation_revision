#!/usr/bin/env python

import os, sys
from flask import Flask, Response, request, render_template, redirect, \
url_for ,send_from_directory
#from flask_bootstrap import Bootstrap

from model.rest_crud import create_new_rest, \
edit_rest_id, delete_rest, listrest, find_rest_name_by_id

def create_app():
  app = Flask(__name__)
  #Bootstrap(app)
  return app

app = create_app()

#Get configuration settings
#app.config.from_object(config_file)
#app.config.from_envvar('APP_CONFIG', silent=True)

#serve custom location static files
#stylesheets
@app.route('/static/css/<path:filename>')
def serve_static_css(filename):
  return send_from_directory(os.path.join(os.getcwd(), 'web','static','css'), filename)

#js
@app.route('/static/js/<path:filename>')
def serve_static_js(filename):
  return send_from_directory(os.path.join(os.getcwd(), 'web','static','js'), filename)

#img
@app.route('/static/img/<path:filename>')
def serve_static_img(filename):
  return send_from_directory(os.path.join(os.getcwd(), 'web','static','img'), filename)


#HOMEPAGE index
@app.route('/')
def index():
  return render_template('index.html')
  #This WORKS
  #with app.test_request_context():
    #return url_for('serve_static_css', filename='bootstrap.css')



##All Restaurant Object Operations
#create - new restaurant
@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'GET':
        return render_template('rest/new.html')
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
        #following Works
        #for r in rest_list:
        #    return str(r.name)
        return render_template('rest/listrest.html', rest_list=rest_list)
    else: return "Nothing!"

#update - edit existing restaurants
@app.route('/update/<int:rest_id>', methods=['POST', 'GET'])
def update(rest_id):
    rest = find_rest_name_by_id(rest_id)
    if request.method == 'GET':
        return render_template('rest/update.html', rest=rest)
    elif request.method == 'POST':
        new_rest_name = request.form['new_name']
        edit_rest_id(rest_id, new_rest_name)
        return redirect(url_for('listall'))

#delete - delete a restaurant
@app.route('/delete/<int:rest_id>', methods=['POST', 'GET'])
def delete(rest_id):
    rest = find_rest_name_by_id(rest_id)
    if request.method == 'GET':
        return render_template('rest/delete.html', rest=rest)
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
