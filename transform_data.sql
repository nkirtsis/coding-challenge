DROP SCHEMA IF EXISTS transform CASCADE;
CREATE SCHEMA transform;


-- day dim table
DROP TABLE IF EXISTS transform.day;
CREATE TABLE transform.day (
	day_id  	INTEGER PRIMARY KEY,
	day_name 	DATE NOT NULL UNIQUE
);

-- TODO: get the dates from config
INSERT INTO transform.day (day_id, day_name)
SELECT
	to_char(d :: DATE , 'YYYYMMDD') :: INTEGER AS day_id,
	d :: DATE AS day_name
FROM generate_series('2020-12-05' :: TIMESTAMP, '2020-12-12' :: TIMESTAMP, '1 day') AS d;


-- orgs dim table
DROP TABLE IF EXISTS transform.organization;
CREATE TABLE transform.organization (
	organization_id  	SERIAL PRIMARY KEY,
	organization_name 	VARCHAR NOT NULL UNIQUE
);

INSERT INTO transform.organization (organization_name)
SELECT organization_name
FROM load.organization
GROUP BY 1
ORDER BY 1;


-- user dim table in SCD2
DROP TABLE IF EXISTS transform.user_history;
CREATE TABLE transform.user_history(
	user_history_id  	SERIAL PRIMARY KEY,
	user_source_id 	 	VARCHAR,
	user_id 	 		INTEGER,	 
	username 			VARCHAR, 	 		
	user_email		 	VARCHAR, 
	user_type 			VARCHAR, 
	organization_name 	VARCHAR, 
	plan_name 			VARCHAR,
	from_date 			TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	to_date			 	TIMESTAMP WITHOUT TIME ZONE NOT NULL, 	
	is_deleted 			SMALLINT NOT NULL,
	is_current_state 	SMALLINT NOT NULL
);

INSERT INTO transform.user_history (user_source_id, user_id, username, user_email, user_type, organization_name, plan_name, from_date, to_date, is_deleted, is_current_state)
SELECT
	user_source_id,
	user_id,
	username,
	user_email,
	user_type,
	organization_name,
	plan_name,
	from_date,
	coalesce(to_date, '9999-12-31'::TIMESTAMP WITHOUT TIME ZONE) AS to_date,
	is_deleted,
	CASE WHEN to_date IS NULL THEN 1 ELSE 0 END :: SMALLINT AS is_current_state
FROM (SELECT 
		id AS user_source_id,
		dense_rank() OVER (ORDER BY username) AS user_id,
		username,
		CASE WHEN event_type = 'User Deleted' THEN 1 ELSE 0 END :: SMALLINT AS is_deleted,
		received_at AS from_date,
		lead(received_at) OVER (PARTITION BY username ORDER BY received_at) AS to_date,
		user_email,
		user_type,
		organization_name,
		plan_name
	FROM load.event
) data
ORDER BY 2,7;


-- user count in SCD
-- SELECT day_id, sum(case when is_deleted = 0 then 1 end) AS users FROM transform.user_fact GROUP BY 1 ORDER BY 1
DROP TABLE IF EXISTS transform.user_fact;
CREATE TABLE transform.user_fact AS
SELECT 
	d.day_id,
	h.user_id,
	h.is_deleted
FROM transform.day d
JOIN transform.user_history h
	ON h.from_date <= d.day_name
	AND d.day_name < h.to_date
ORDER BY 1,2;