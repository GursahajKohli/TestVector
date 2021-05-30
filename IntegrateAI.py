from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as xml
import xml.etree.ElementTree as xml1
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

import json

#Integrate AI

r = requests.get('https://boards.greenhouse.io/integrateai')

html = r.text

soup = BeautifulSoup(html, 'html.parser')


child = []
for tag in soup.findAll('div',{'class' : 'opening'}):

    child.append(tag.findChild())
job_board = 'https://boards.greenhouse.io'

job_links = []
for opening in child:
    job_links.append(job_board+opening['href'])


root = xml.Element('jobs')
tree = xml.ElementTree(root)
for jobs in job_links:

    job_request = requests.get(jobs)
    job_html = job_request.text
    job_soup = BeautifulSoup(job_html, 'html.parser')

    for job in job_soup.findAll('div', {'id' : 'content'}):
        #print(job)
        job_title = job_soup.find('h1', {'class' : 'app-title'}).string
        job_location = job_soup.find('div', {'class' : 'location'}).string
        job_content = job_soup.find('div', {'id' : 'content'})
        job_content = str(job_content).replace('<div class="" id="content">', '').replace('</div>', '')
        #print("Job title :: ", job_title)
        #print("Job location :: ", job_location)
        #print("Job contents :: ", job_content)


        jobXml = Element('job')
        root.append(jobXml)
        jobTitle = xml.SubElement(jobXml, 'job_title')
        jobTitle.text = job_title
        print(job_title)

        description = xml.SubElement(jobXml, 'description')
        description.text = job_content

        url = xml.SubElement(jobXml, 'url')
        url.text = jobs
        print(url)

        apply_email = xml.SubElement(jobXml, 'apply_email')

        company = xml.SubElement(jobXml, 'company')
        company.text = "integrate.ai"

        company_url = xml.SubElement(jobXml, 'company_url')
        company_url.text = "https://integrate.ai/"

        city = xml.SubElement(jobXml, 'city')
        city.text = str(job_location.strip())

        location = xml.SubElement(jobXml, 'location')
        location.text = "Canada"

        reference = xml.SubElement(jobXml, 'reference')
        #reference.text = "1234"

'''
#Vector Bamboo

r = requests.get('https://vectorinstitute.bamboohr.com/jobs/')
print(r.status_code)
html = r.text

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.findAll('script', {'id' : 'positionData'}):
    #print(tag.string.split("},{"))
    obj = json.loads(tag.string)

jobs = []
for i in range(0, len(obj)):

    if obj[i]['departmentLabel'] == 'AI Engineering & Technology':
        jobs.append(obj[i])
for job in jobs:

    jobXml = Element('job')
    root.append(jobXml)
    jobTitle = xml.SubElement(jobXml, 'job_title')
    jobTitle.text = job['jobOpeningName']

    description = xml.SubElement(jobXml, 'description')
    description.text = job_content

    url = xml.SubElement(jobXml, 'url')
    url.text = jobs

    apply_email = xml.SubElement(jobXml, 'apply_email')

    company = xml.SubElement(jobXml, 'company')
    company.text = "integrate.ai"

    company_url = xml.SubElement(jobXml, 'company_url')
    company_url.text = "https://integrate.ai/"

    city = xml.SubElement(jobXml, 'city')
    city.text = str(job_location)

    location = xml.SubElement(jobXml, 'location')
    location.text = "Canada"

    reference = xml.SubElement(jobXml, 'reference')
    #reference.text = "1234"
    '''


print(xml1.tostring(root))
file_obj = open("Job_posts.xml", "w+")
file_obj.write(str(xml1.tostring(root))[2:-1])

print("Done!")


