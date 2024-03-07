from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import DecimalField, RadioField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired, Email, Length

from werkzeug.security import generate_password_hash
from email_validator import validate_email, EmailNotValidError
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
bootstrap = Bootstrap5(app)


class MyForm(FlaskForm):
    email = StringField('Email', validators=[Email("This field requires a valid email address")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8,
                                                                             message="Password must be at least 8 charcters long")])
    submit = SubmitField(label='Log in')
    """
    remember_me = BooleanField('Remember me')
    salary = DecimalField('Salary', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'),('UK', 'United Kingdom')])
    message = TextAreaField('Message', validators=[InputRequired()])
    photo = FileField('Photo')
    """


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # remember_me = form.remember_me.data
        # salary = form.salary.data
        # gender = form.gender.data
        # country = form.country.data
        # message = form.message.data
        # photo = form.photo.data.filename
        # return f'Name: {name} < br > Password: {generate_password_hash(password)}< br > Remember me: {remember_me} < br > Salary: {salary} < br > Gender: {gender} < br > Country: {country} < br > Message: {message} < br > Photo: {photo} '
        print(f'Email: {email} Password: {generate_password_hash(password)}')
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
