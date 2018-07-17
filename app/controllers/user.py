from flask import url_for, redirect, render_template
from app.forms.user import UserSave
from app.models.models import User
from app import db

class UserController:
    def input(self):
        usersave =UserSave()
        if usersave.validate_on_submit():
            user= User(username=usersave.username.data)
            user.set_password(usersave.password_hash.data)
            user.save()
            return redirect(url_for('input_user'))
        user=User().getAll()
        return render_template('user/input.html', form= usersave, title='Administrator Index', user=user)

    def edit(self, id):
        usersave= UserSave()
        user= User().getOne(id)
        if usersave.validate_on_submit():
            user.username= usersave.username.data
            user.password_hash= usersave.password_hash.data
            db.session.commit()
            return redirect(url_for('input_user'))
        return render_template('user/edit.html', form=usersave, user=user)

    def delete(self, id):
        user = User().getOne(id)
        user.delete()
        return redirect(url_for('input_user'))