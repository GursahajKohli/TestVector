from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as xml
import xml.etree.ElementTree as xml1
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import re

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
        job_img = job_soup.find('img')['src']
        print(job_img)

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

r = requests.get('https://www.canvass.io/careers')
html = r.text

#print(html)

soup = BeautifulSoup(html, 'html.parser')
i = 0
job_links = []
company_link = "https://www.canvass.io"
for tags in soup.findAll('a', {'class' : 'job-listing-card w-inline-block'}):

    job_links.append(company_link + tags['href'])

for jobs in job_links:

    job_request = requests.get(jobs)
    job_html = job_request.text
    job_soup = BeautifulSoup(job_html, 'html.parser')

    job_title = job_soup.find('h1', {'class' : 'page-title-2 section-header'}).string
    job_location = job_soup.find('div', {'class' : 'job-listing-info-text'}).string
    job_content = str(job_soup.find('div', {'class' : 'project-rich-text w-richtext'})).replace("Â", '').replace('â', '').replace('â', "")
    job_c = job_content.encode("utf-8")

    #print(job_c)
    input()
    #job_content = re.sub('Ã¢Â€Â¢\t', '', job_content) .replace('Ã¢Â€Â¢\tWe', 'We').replace('Â·Â Â Â', '').replace('Â', '').replace('â', '').replace('¢\t', '')
    print(job_content)

    job_content = '<html><body>' + job_content + '</body></html>'
    job_img = job_soup.find('img', {'class' : 'logo'})['src']

    jobXml = Element('job')
    root.append(jobXml)

    jobTitle = xml.SubElement(jobXml, 'job_title')
    jobTitle.text = job_title

    description = xml.SubElement(jobXml, 'description')
    description.text = job_content

    url = xml.SubElement(jobXml, 'url')
    url.text = jobs
    print(jobs)

    apply_email = xml.SubElement(jobXml, 'apply_email')
    apply_email.text = 'info@canvass.io'

    company = xml.SubElement(jobXml, 'company')
    company.text = "CANVASS"

    company_url = xml.SubElement(jobXml, 'company_url')
    company_url.text = "https://www.canvass.io/"

    city = xml.SubElement(jobXml, 'city')
    city.text = str(job_location.strip())

    location = xml.SubElement(jobXml, 'location')
    location.text = "Canada"

    reference = xml.SubElement(jobXml, 'reference')

print(xml1.tostring(root))
file_obj = open("Job_posts.xml", "w+")
file_obj.write(str(xml1.tostring(root))[2:-1])

print("Done!")


