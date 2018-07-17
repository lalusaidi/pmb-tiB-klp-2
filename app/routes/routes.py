from app import app
from flask import render_template, url_for, flash
from app.controllers.daftar import DaftarController
from app.controllers.user import UserController
#import login
from flask_login import current_user, login_user, logout_user, login_required
from app.models.models import User
from flask import flash, redirect
from flask import request
from werkzeug.urls import url_parse
from app.forms.login import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#route pendaftar
@app.route('/daftar', methods=['GET', 'POST'])
def index_daftar():
    return DaftarController().index()

@app.route('/daftar/input', methods=['POST', 'GET'])
def input_daftar():
    return DaftarController().input()
    
#edit
@app.route('/daftar/<id>/edit', methods=['POST', 'GET'])
def edit_daftar(id):
    return DaftarController().edit(id)
#delete
@app.route('/daftar/<id>/delete')
def delete_daftar(id):
    return DaftarController().delete(id)
#route admin
@app.route('/user', methods=['GET', 'POST'])

def index_user():
    return render_template('user/index.html', title='Admin Panel')

#inputuser
@app.route('/user/input', methods=['GET', 'POST'])
def input_user():
    return UserController().input()

#login
@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index_user'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password_hash.data):
            flash('Username atau password salah')
            return redirect(url_for('login'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = url_for('index_user')
        return redirect(next_page)
        return redirect(url_for('index_user'))
    return render_template('user/login.html', title='Log In', form=form)

#logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#edit
@app.route('/user/<id>/edit', methods=['POST', 'GET'])
def edit_user(id):
    return UserController().edit(id)

#delete
@app.route('/user/<id>/delete')
def delete_user(id):
    return UserController().delete(id)