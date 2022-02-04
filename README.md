# Indeed-Web-Scraping
Custom Website of Indeed Job Postings from Catalina Island with Leaflet map, D3 HTML Table, and Heroku API map. 


![image](https://user-images.githubusercontent.com/87084344/152458477-bc865153-d34a-4d0f-9771-e3e62677ac75.png)

### Web Scraping
Began with using Python, BeautifulSoup to connect to indeed.com and pull the data fields we wanted. Built out a loop to create all the data that we could then export via csv file. 

### SQL
Utilized postgreSQL to build a table and import the data from our csv file and normalize the data. 

### Heroku
Created a heroku app that allows visitors to post new jobs to the site on a map.

### HTML Table
used D3 to pull data from JSON files into a table that then is filtered to allow user to type and limit the job postings. 

### Leaflet
Utilized JavaScript Leaflet to map out the locations of the current postings. Due to the general addresses used on indeed, we clustered the markers on the map. 

### Data Limitations
We only pulled the data once and job postings would be outdated. 
Catalina Island had a limited number of jobs that we later realized many jobs were duplicates but posted on different days.
Not much salary data available to compare. 

Project Team
