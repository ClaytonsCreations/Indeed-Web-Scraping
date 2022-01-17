SELECT * FROM indeed_jobs;

SELECT jobtitle, company, location, jobsummary, yearly_salary, id 
FROM indeed_jobs
WHERE yearly_salary <> 'None';