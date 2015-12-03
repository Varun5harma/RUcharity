from flask import render_template
from app import app

#view (MVC)

@app.route('/')
@app.route('/index/')

def index():
	user = {'nickname': 'Miguel'}  # fake user
	return render_template('index.html',
                            title='Home',
	                        user=user)


# def index():
#     user = {'nickname': 'Miguel'}  # fake user
#     return render_template('index.html',
#                            title='Home',
#                            user=user)
