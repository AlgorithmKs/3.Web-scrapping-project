import csv
from bs4 import BeautifulSoup
import requests

def requirements_for_job(job_URL):
    page = requests.get(job_URL).text
    soup = BeautifulSoup(page, 'html.parser')
    requirements = soup.find_all(['li', 'p', 'ul'])

    requirements_list = []
    for requirement in requirements:
        hard_requirement = requirement.get_text(strip=True)
        if hard_requirement:
            requirements_list.append(hard_requirement)
    return requirements_list

def save_requirements_to_csv(job_URL, csv_filename):
    requirements_from_url = requirements_for_job(job_URL)

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Requirement']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for requirement in requirements_from_url:
            writer.writerow({'Requirement': requirement})

    print(f"Requirements data has been written to {csv_filename}.")

job_URL = 'https://www.adzuna.com/details/4412021247'
csv_filename = 'requirements_data.csv'
save_requirements_to_csv(job_URL, csv_filename)

