from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from src.user.forms import RegistrationForm, LoginForm
from src.user.models import User

user_blueprint = Blueprint('user',
                           __name__,
                           template_folder='templates/users')


@user_blueprint.route('/registration', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():

        name = form.name.data
        last_name = form.last_name.data
        region = form.region.data
        email = form.email.data
        password = form.password.data

        user = User(name, last_name, region, email, password)

        try:
            user.create()
        except:
            flash("user registration failed", "danger")
        else:
            flash('user registered!', "success")

        form.name.data = ''
        form.last_name.data = ''
        form.email.data = ''
        form.password.data = ''

        return redirect(url_for('user.register_user'))

    return render_template('register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    print(form.validate_on_submit())

    if form.validate_on_submit():

        email = form.email.data

        user_by_email = User.get_by_email(email)

        if user_by_email and user_by_email.check_password(form.password.data):

            try:
                login_user(user_by_email)
            except:
                flash('login failed', 'danger')
                return render_template("login.html", form=form)
            else:
                flash('login successful', "success")
            next = request.args.get("next")

            if next is None:
                next = url_for('user.profile')

            return redirect(url_for("user.profile"))

        else:
            flash("such email doesn't exists", 'danger')

    return render_template("login.html", form=form)