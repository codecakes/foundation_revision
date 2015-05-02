from flask import Flask, request, render_template, redirect, url_for

from model.rest_crud import create_new_rest, find_rest, edit_rest_name, \
delete_rest

app = Flask(__name__)

#Get configuration settings
#app.config.from_object(config_file)
#app.config.from_envvar('APP_CONFIG', silent=True)

@app.route('/')
@app.route('/restlist')
def restlist():
    return "Hello"

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'GET':
        return render_template('/web/templates/new.html')
    elif request.method == 'POST':
        rest_name = request.form['restaurantname']
        create_new_rest(rest_name)
        return redirect(url_for('restlist'))


if __name__ == "__main__":
    port = 8080
    hostname = '0.0.0.0'
    app.run(debug=True, port = port, host=hostname)