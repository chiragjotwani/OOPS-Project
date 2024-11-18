import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

links = set()
contact_numbers = []
emails = []
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
for tag in tags:
    href = tag.get('href', None)
    if href == None:
        continue
    words = re.search('https://.*', href)
    if words:
        links.add(words.group())

text = soup.get_text()

phone_pattern = r'(\+91[\-\s]?[6-9]\d{9}|\b[6-9]\d{9}\b|1800[\-\s]?\d{3}[\-\s]?\d{4}|\b1800\d{7,8}\b)'
for number in re.findall(phone_pattern, text):
    if number not in contact_numbers:
        contact_numbers.append(number)

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
for email in re.findall(email_pattern, text):
    if email not in emails:
        emails.append(email)

print("Following is the list of URLs, contact details and emails respectively in the link you gave:\n\nURLs:")
for link in links:
    print(link)

print("\nContact Details:")
for contact in contact_numbers:
    print(contact)

print("\nEmails:")
for mails in emails:
    print(mails)