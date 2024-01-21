from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, FileField, DecimalField, RadioField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, InputRequired

'''
Open the Terminal in PyCharm (bottom left). 
python -m pip install -r requirements.txt
This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.secret_key = 'rohit'


class LoginForm(FlaskForm):  # all field which we want in our form

    name = StringField(label='Name:', validators=[DataRequired(), Length(min=2)])
    email = EmailField(label='Email:', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(min=3)])
    remember_me = BooleanField('Remember me')
    salary = DecimalField('Salary', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[
        ('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'),
                                              ('UK', 'United Kingdom')])
    message = TextAreaField('Message')
    photo = FileField('Photo')
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_name = login_form.name.data
        email_id = login_form.email.data
        password = login_form.password.data
        if user_name.lower() == "rohit" and email_id == "mymail@gmail.com" and password == "123456789":
            return render_template("success.html", user=user_name, mail=email_id)
        else:
            return render_template("denied.html")
            # return f"Name: {user_name}<br>mail: {email_id}<br>pass: {password}"

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
