from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class FunctionForm(Form):
   # function_name = HiddenField()

   function_name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your Login."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   person_text = StringField("Text: ", [
                                   validators.DataRequired("Please enter your password."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                               ])

   counter_of_tests = StringField("Count of tests: ", [
                                   validators.DataRequired("Please enter your name."),
                                   validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                               ])

   # person_login_fk = StringField("Person login: ", [
   #                                 validators.DataRequired("Please enter your surname."),
   #                                 validators.Length(3, 20, "Name should be from 3 to 20 symbols")
   #                             ])

   person_login_fk = HiddenField()

   submit = SubmitField("Save")


