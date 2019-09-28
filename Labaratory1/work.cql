INSERT INTO testing."PERSON_FUNCTION_TESTCASE_RESULT" (person_login,
	person_password,
	person_data, 
	function_name,
	function_text,
	counter_of_tests,
	testcase_id,
    testcase_value,
    resulr_value,
    testcase_iteration
	     )
	VALUES ('Dima', '12341234',
{"name": 'Dima', "surname": 'Koltsov', "email": 'dik_2010@ukr.net', "bitrhday": '01-01-1999'}, 'add',
'def add(a, b):\n\treturn a+b', 2, 1, {'a' : ['int', '1'], 'b' : ['int', '2']}, {'int': '3'}, 1);

INSERT INTO testing."PERSON_FUNCTION_TESTCASE_RESULT" (person_login,
	person_password,
	person_data, 
	function_name,
	function_text,
	counter_of_tests,
	testcase_id,
    testcase_value,
    resulr_value,
    testcase_iteration
	     )
	VALUES ('Dima', '12341234',
{"name": 'Dima', "surname": 'Koltsov', "email": 'dik_2010@ukr.net', "bitrhday": '01-01-1999'}, 'add',
'def add(a, b):\n\treturn a+b', 2, 2, {'a' : ['int', '1'], 'b' : ['int', '6']}, {'int': '6'}, 2);

INSERT INTO testing."PERSON_FUNCTION_TESTCASE_RESULT" (person_login,
	person_password,
	person_data, 
	function_name,
	function_text,
	counter_of_tests,
	testcase_id,
    testcase_value,
    resulr_value,
    testcase_iteration
	     )
	VALUES ('Yarik', '12341234',
{"name": 'Yarik', "surname": 'Artemenko', "email": 'yar_2010@ukr.net', "bitrhday": '11-08-1999'}, 'sub',
'def sub(a, b):\n\treturn a-b', 1, 1, {'a' : ['int', '1'], 'b' : ['int', '2']}, {'int': '-1'}, 1);

CREATE INDEX IF NOT EXISTS user on testing."PERSON_FUNCTION_TESTCASE_RESULT" (person_data);

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET person_data = {
	"name": 'Dima',
	"surname": 'Koltsov',
	"email": 'dik19994@gmail.com',
	"bitrhday": '01-01-1999'
}WHERE function_name = 'add' AND testcase_iteration = 1 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';

select * from testing."PERSON_FUNCTION_TESTCASE_RESULT";

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET person_data = {
	"name": 'Dima',
	"surname": 'Koltsov',
	"email": 'dik19994@gmail.com',
	"bitrhday": '01-01-1999'
}WHERE function_name = 'add' AND testcase_iteration = 2 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';

select * from testing."PERSON_FUNCTION_TESTCASE_RESULT";

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET counter_of_tests = 3, person_password = 'qwerqwer'
WHERE function_name = 'sub' AND testcase_iteration = 1 AND person_login = 'Yarik' AND function_text = 'def sub(a, b):\n\treturn a-b';

select * from testing."PERSON_FUNCTION_TESTCASE_RESULT";

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET testcase_id = 2
WHERE function_name = 'sub' AND testcase_iteration = 1 AND person_login = 'Yarik' AND function_text = 'def sub(a, b):\n\treturn a-b';

select * from testing."PERSON_FUNCTION_TESTCASE_RESULT";

select 
	person_login, function_text, resulr_value
from testing."PERSON_FUNCTION_TESTCASE_RESULT"
WHERE function_name = 'add' AND testcase_iteration = 1 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';

select 
	function_name, person_data
from testing."PERSON_FUNCTION_TESTCASE_RESULT"
WHERE function_name = 'add' AND testcase_iteration = 2 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';

select 
	person_login, testcase_value, resulr_value
from testing."PERSON_FUNCTION_TESTCASE_RESULT"
WHERE function_name = 'sub' AND testcase_iteration = 1 AND person_login = 'Yarik' AND function_text = 'def sub(a, b):\n\treturn a-b';

select 
	testcase_id, counter_of_tests, resulr_value
from testing."PERSON_FUNCTION_TESTCASE_RESULT"
WHERE function_name = 'sub' AND testcase_iteration = 1 AND person_login = 'Yarik' AND function_text = 'def sub(a, b):\n\treturn a-b';
