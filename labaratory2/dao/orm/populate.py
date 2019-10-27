from labaratory2.dao.orm.model import *

db.create_all()


db.session.query(ormResult).delete()
db.session.query(ormParameters).delete()
db.session.query(ormTestCase).delete()
db.session.query(ormFunction).delete()
db.session.query(ormPersons).delete()




Dima = ormPersons(  person_login = "Dima",
                person_password = "0000",
                person_name = "Dima",
                person_surname = "Koltsov",
                person_email = "dik19994@gmail.com",
                person_birthday = "1999-01-01")

Vlad = ormPersons(  person_login = "Vlad",
                person_password = "0000",
                person_name = "Vlad",
                person_surname = "Kanevckyi",
                person_email = "vladkaneve@gmail.com",
                person_birthday = "1999-02-04")

Vadim = ormPersons(  person_login = "Vadim",
                person_password = "0000",
                person_name = "Vadim",
                person_surname = "Pits",
                person_email = None,
                person_birthday = "1998-10-29")

Yarik = ormPersons(  person_login = "Yarik",
                person_password = "0000",
                person_name = "Yarik",
                person_surname = "Artemenko",
                person_email = None,
                person_birthday = "1999-08-11")

Srhey = ormPersons(  person_login = "Srhey",
                person_password = "0000",
                person_name = "Srhey",
                person_surname = "Gorodnuk",
                person_email = None,
                person_birthday = "1999-10-02")

add = ormFunction( function_name = "add",
                person_text = "def add(a, b):\n\treturn a+b",
                counter_of_tests = 10)

sub = ormFunction( function_name = "sub",
                person_text = "def sub(a, b):\n\treturn a-b",
                counter_of_tests = 10)

mult = ormFunction( function_name = "mult",
                person_text = "def mult(a, b):\n\treturn a*b",
                counter_of_tests = 10)

div = ormFunction( function_name = "div",
                person_text = "def div(a, b):\n\treturn a/b",
                counter_of_tests = 10)

abs = ormFunction( function_name = "abs",
                person_text = "def abs(a):\n\treturn abs(a)",
                counter_of_tests = 10)


Dima.Persons_Function.append(add)
Vlad.Persons_Function.append(sub)
Vadim.Persons_Function.append(mult)
Yarik.Persons_Function.append(div)
Srhey.Persons_Function.append(abs)

i_1 = ormTestCase(testcase_id = 1)
i_2 = ormTestCase(testcase_id = 2)
i_3 = ormTestCase(testcase_id = 3)
i_4 = ormTestCase(testcase_id = 4)
i_5 = ormTestCase(testcase_id = 5)

add.Function_TescCase.append(i_1)
sub.Function_TescCase.append(i_2)
mult.Function_TescCase.append(i_3)
div.Function_TescCase.append(i_4)
abs.Function_TescCase.append(i_5)

p_0i_1_1 = ormParameters(parameters_index = 0,
    testcase_iteration = 1,
    parameters_value = 2)

p_1i_1_2 = ormParameters(parameters_index = 1,
    testcase_iteration = 1,
    parameters_value = 3)

p_0i_1_3 = ormParameters(parameters_index = 0,
    testcase_iteration = 1,
    parameters_value = 4)

p_1i_1_4 = ormParameters(parameters_index = 1,
    testcase_iteration = 1,
    parameters_value = 5)

p_0i_1_5 = ormParameters( parameters_index = 0,
    testcase_iteration = 1,
    parameters_value = -7)


i_1.TestCase_Parameters.append(p_0i_1_1)
i_1.TestCase_Parameters.append(p_1i_1_2)
i_2.TestCase_Parameters.append(p_0i_1_3)
i_2.TestCase_Parameters.append(p_1i_1_4)
i_5.TestCase_Parameters.append(p_0i_1_5)


iter_1 = ormResult(result_value = 5,
                    testcase_iteration = 1)

iter_2 = ormResult(result_value = -1,
                    testcase_iteration = 1)

iter_3 = ormResult(result_value = 4,
                    testcase_iteration = 1)

iter_4 = ormResult(result_value = 0.25,
                    testcase_iteration = 1)

iter_5 = ormResult(result_value = 7,
                    testcase_iteration = 1)

i_1.TestCase_Result.append(iter_1)
i_2.TestCase_Result.append(iter_2)
i_3.TestCase_Result.append(iter_3)
i_4.TestCase_Result.append(iter_4)
i_5.TestCase_Result.append(iter_5)


db.session.add_all([Dima, Vlad, Vadim, Yarik, Srhey, add, sub, mult, div, abs, i_1, i_2, i_3, i_4, i_5,
                    p_0i_1_1, p_1i_1_2, p_0i_1_3, p_1i_1_4, p_0i_1_5, iter_1, iter_2, iter_3, iter_4, iter_5])



db.session.commit()