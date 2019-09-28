from cassandra.cluster import Cluster

cluster = Cluster()
connection = cluster.connect('testing')

batch = """
BEGIN BATCH
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

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET person_data = {
	"name": 'Dima',
	"surname": 'Koltsov',
	"email": 'dik19994@gmail.com',
	"bitrhday": '01-01-1999'
}WHERE function_name = 'add' AND testcase_iteration = 1 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';

UPDATE testing."PERSON_FUNCTION_TESTCASE_RESULT" 
SET counter_of_tests = 3, person_password = 'qwerqwer'
WHERE function_name = 'add' AND testcase_iteration = 1 AND person_login = 'Dima' AND function_text = 'def add(a, b):\n\treturn a+b';
APPLY BATCH;
"""
connection.execute(batch)