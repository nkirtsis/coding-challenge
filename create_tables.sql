DROP SCHEMA IF EXISTS load CASCADE;
CREATE SCHEMA load;

DROP TABLE IF EXISTS load.event;
CREATE TABLE load.event (
	id				 	VARCHAR NOT NULL,
	event_type		 	VARCHAR NOT NULL,
	username		 	VARCHAR NOT NULL,
	user_email		 	VARCHAR NOT NULL,
	user_type		 	VARCHAR NOT NULL,
	organization_name 	VARCHAR,
	plan_name	 		VARCHAR,
	received_at	 		TIMESTAMP WITHOUT TIME ZONE NOT NULL
);

DROP TABLE IF EXISTS load.organization;
CREATE TABLE load.organization(
	organization_key 	VARCHAR NOT NULL UNIQUE,
	organization_name 	VARCHAR NOT NULL,
	created_at 			TIMESTAMP WITHOUT TIME ZONE NOT NULL
);


DROP SCHEMA IF EXISTS test CASCADE;
CREATE SCHEMA test;

DROP TABLE IF EXISTS test.test;
CREATE TABLE test.test (
	id				INTEGER NOT NULL,
	name		 	VARCHAR NOT NULL
);