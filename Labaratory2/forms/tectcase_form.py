from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators


class TestCaseForm(Form):

   testcase_id = StringField("Id: ",[
                                    validators.DataRequired("Please enter your id."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   function_name_fk = HiddenField()
   # function_name_fk = StringField("Name: ",[
   #                                  validators.DataRequired("Please enter your name."),
   #                                  validators.Length(3, 20, "Name should be from 3 to 20 symbols")
   #                               ])


   submit = SubmitField("Save")


