DROP TABLE IF EXISTS indeed_jobs;

-- creating table frame to import data
CREATE TABLE indeed_jobs (
	JobTitle varchar(100),
	Company	varchar(100),
	Location varchar(100),
	JobSummary varchar (255),
	Posted varchar (50),
	DataPulled varchar(50),
	Salary varchar (50)
);

SELECT * FROM indeed_jobs;

-- normalizing location data
UPDATE indeed_jobs
SET location = 'Avalon, CA'
WHERE location = 'Avalon, CA 90704';

SELECT * FROM indeed_jobs;

-- Removing 'Posted' to normalize date posted data
UPDATE indeed_jobs
SET posted = REPLACE(posted, 'Posted', '');

SELECT * FROM indeed_jobs;

-- Adding Unique ID column
ALTER TABLE indeed_jobs
ADD ID SERIAL PRIMARY KEY;

SELECT * FROM indeed_jobs;

-- normalizing salary info by changing hourly to yearly
UPDATE indeed_jobs
SET salary = '$33,280 - $56,160'
WHERE salary = '$16 - $27 an hour';

UPDATE indeed_jobs
SET salary = '$39,520 - $47,840'
WHERE salary = '$19 - $23 an hour';

UPDATE indeed_jobs
SET salary = '$54,080 - $66,560'
WHERE salary = '$26 - $32 an hour';

UPDATE indeed_jobs
SET salary = '$62,400 - $104,000'
WHERE salary = '$30 - $50 an hour';

UPDATE indeed_jobs
SET salary = '$41,600'
WHERE salary = 'From $20 an hour';

UPDATE indeed_jobs
SET salary = '$45,760'
WHERE salary = 'From $22 an hour';

SELECT * FROM indeed_jobs;

-- Removing "a year" from some to normalize data
UPDATE indeed_jobs
SET salary = REPLACE(salary, 'a year', '')
WHERE salary LIKE '%a year%';

SELECT * FROM indeed_jobs;

-- Updating salary column to signify numbers are yearly
ALTER TABLE indeed_jobs
RENAME COLUMN salary TO yearly_salary;

SELECT * FROM indeed_jobs;

