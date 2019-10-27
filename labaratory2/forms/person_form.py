from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class PersonForm(Form):

   person_login = StringField("Login: ",[
                                    validators.DataRequired("Please enter your Login."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   person_password = StringField("Password: ",[
                                    validators.DataRequired("Please enter your password."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   person_name = StringField("Name: ", [
                                   validators.DataRequired("Please enter your name."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                               ])

   person_surname = StringField("Surname: ",[
                                       validators.DataRequired("Please enter your surname."),
                                       validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                   ])


   person_email = StringField("Email: ",[
                                 validators.DataRequired("Please enter your name."),
                                 validators.Email("Wrong email format")
                                 ])

   person_birthday = DateField("Birthday: ", [ validators.DataRequired("Please enter your birthday.")])


   submit = SubmitField("Save")


