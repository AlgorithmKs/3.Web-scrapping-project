import re
import csv
from bs4 import BeautifulSoup
import requests

def extract_job_titles(job_element):
    job_titles = job_element.find_all("a", class_="text-base md:text-xl lg:text-2xl text-adzuna-green-500 hover:underline")
    job_title_list = []
    for title in job_titles:
        job_title_list.append(title.get_text(strip=True))
    return job_title_list

def extract_company_names(job_element):
    company_names = job_element.find_all("div", class_="ui-company")
    company_name_list = []
    for company in company_names:
        company_name_list.append(company.get_text(strip=True))
    return company_name_list

def extract_salary_info(job_element):
    salary_elements = job_element.find_all("a", class_="text-orange-500 inline-block hover:underline")
    salary_list = []
    for salary in salary_elements:
        salary_list.append(re.sub(r'[^\d,]', '', salary.get_text(strip=True)))
    return salary_list

def extract_job_links(job_element):
    link_elements = job_element.find_all("a")
    link_list = []

    for link in link_elements:
        link_text = link.get('href')
        if link_text and link_text.startswith("https://www.adzuna.com/details/"):
            link_list.append(link_text)

    unique_links = list(set(link_list))

    return unique_links

def extract_job_info(soup):
    job_elements = soup.find_all("div", class_="ui-search-results w-full md:w-3/4")
    job_list = []

    for job_element in job_elements:
        job_titles = extract_job_titles(job_element)
        company_names = extract_company_names(job_element)
        salary_elements = extract_salary_info(job_element)
        link_elements = extract_job_links(job_element)

        for job_title, company_name, salary, link_text in zip(job_titles, company_names, salary_elements, link_elements):
            job_list.append({
                'Job title': job_title,
                'Company name': company_name,
                'Salary': salary,
                'Link': link_text
            })

    return job_list

position = 'developer'
location = 'Hamburg'
page_number = 1

with open('job_data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Job title', 'Company name', 'Salary', 'Link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    while True:
        url = f'https://www.adzuna.com/search?q={position}&w={location}&p={page_number}'
        
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            job_list = extract_job_info(soup)

            if not job_list:
                break

            for job in job_list:
                writer.writerow(job)
                print('Job title:', job['Job title'])
                print('Company name:', job['Company name'])
                print('Salary:', job['Salary'])
                print('Link:', job['Link'], '\n')

            page_number += 1
        else:
            print(f"Failed to retrieve data from {url}")
            break

print("Job data has been written to job_data.csv.")


csv_filename = 'job_data.csv'

with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        print('Job title:', row['Job title'])
        print('Company name:', row['Company name'])
        print('Salary:', row['Salary'])
        print('Link:', row['Link'])
        print('\n')



