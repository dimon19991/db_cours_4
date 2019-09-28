CREATE KEYSPACE IF NOT EXISTS TESTING 
WITH replication = {
 'class': 'SimpleStrategy',
'replication_factor' : 1
 };

 CREATE TYPE IF NOT EXISTS TESTING."PERSON_DATA"
 (
 	name text,
 	surname text,
 	email text,
 	bitrhday text
 );
 
 CREATE TABLE IF NOT EXISTS TESTING."PERSON_FUNCTION_TESTCASE_RESULT"
 (
 	person_login text,
 	person_password text,
 	person_data frozen<TESTING."PERSON_DATA">,
 	function_name text,
 	function_text text,
 	counter_of_tests int STATIC,
 	testcase_id int,
 	testcase_value map<text, frozen<list<text>>>,
 	resulr_value map<text, text>,
 	testcase_iteration int,
 	PRIMARY KEY ((function_name ,testcase_iteration), person_login, function_text)
 );
 
 
 
