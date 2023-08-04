import os.path
import time
import requests
from bs4 import BeautifulSoup

print("Put some skill that you are know")
unfamiliar_skil=input(">")
print(f"Output familiar jobs {unfamiliar_skil}:")

def find_job():
    html_link = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_link, 'lxml')
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    sameanswers = False
    for index ,job in enumerate(jobs):



        published_date = job.find('span', class_="sim-posted").text
        if   "few" in published_date:

            job_date = job.find("li").i.nextSibling



            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            # print(company_name)

            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            # print(skills)



            more_info = job.header.h2.a['href'].strip()
            if unfamiliar_skil  in skills:


                with open(f'job_files/{index}.txt','a') as f:

                    f.write(f"Company name: {company_name.strip()}")
                    f.write(f"\nNeed skills: {skills.strip()}")
                    f.write("\nMore info: " + more_info.strip())
                    f.write(f'\nExperience: {job_date.strip()}')


                print(f'Files saved {index}')
print(os.getcwd())
if __name__ == '__main__':
    while True:
        find_job()
        time_wait =10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)

