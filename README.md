# Description
This programm scrap information about job positions 
('Job title', 'Company name', 'Salary', 'Link') from website https://www.adzuna.com/

# Instruction
1.Download file on your local machine.
2.Create a virtual environment (instruction):
https://metanit.com/python/django/1.2.php
3.Install the required libraries from the requirements.txt
(If you have errors use pip3 install beatifulsoup4 and pip3 install requests)

Part 1:
1.Open job_list.py and change strings 60 (position), 61 (location). You can write whatever you want.
2.Script will scrap information from HTML-site in CSV file 'job_data.csv' in you current directory.

Part 2:
If you want to scrap information about current position:
1.Open position_req.py
2.On string 30 add any link from  CSV file 'job_data.csv' about job position.
3.Script will scrap information from HTML-site in CSV file 'requirements_data.csv' in you current directory.