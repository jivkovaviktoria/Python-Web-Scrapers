import requests
from bs4 import BeautifulSoup

# With example city

response = requests.get("https://www.zaplata.bg/shoumen/")

soup = BeautifulSoup(response.content, "html.parser")

results = soup.find(class_="main")

job_elements = results.find_all("div", class_="main")

job_offers_info = []

for job_element in job_elements:
    title_element = job_element.find("div", class_="title")
    location_element = job_element.find("div", class_="city")
    salary_element = job_element.find("div", class_="salary")

    job_offer = {"title": title_element.text.strip(), "location": location_element.text.strip(), "salary": "unknown"}
    
    if salary_element != None: job_offer["salary"] = salary_element.text.strip()

    job_offers_info.append(job_offer)

with open("job_offers.txt", "w", encoding="utf-8") as f:
    for offer in job_offers_info:
        f.write("\n" + offer["title"] + "\n" + offer["location"] + "\n" + offer["salary"] + "\n")


            

