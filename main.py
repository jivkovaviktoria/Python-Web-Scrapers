import requests
from bs4 import BeautifulSoup

# Scrape data from Wisdom Pet Medicine website

response = requests.get("http://wisdompetmed.com/")

# Retrieve content of Wisdom Pet Medicine website

soup = BeautifulSoup(response.text)

# Find all featured testimonials

featured_testimonials = soup.find_all("div", class_="quote")

testimonials_info = []

for testimonial in featured_testimonials:
    testimonials_info.append(testimonial.text)

with open("wisdompet_testimonials.txt", "w", encoding="utf-8") as f:
    for testimonial in testimonials_info:
        f.write(testimonial)

# Find all staff members with their biographies

staff = soup.find_all("div", class_="info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")

staff_info = []

for member in staff:
    staff_info.append(member.text)

with open("wisdompet_staff_members.txt", "w", encoding="utf-8") as f:
    for member in staff_info:
        f.write(member)

# Find all links on the Wisdom pet medicine website

links = soup.find_all("a")

for link in links:
    link.text, link.get("href")

with open("wisdompet.txt", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

