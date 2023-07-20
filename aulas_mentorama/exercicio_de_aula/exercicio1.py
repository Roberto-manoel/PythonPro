import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.w3schools.io/file/yaml-sample-example/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
yaml_example = soup.find('pre').text
comments = re.findall(r'#(.*)', yaml_example)
for comment in comments:
    print(comment)

with open('example.yaml', 'w') as file:
    file.write(yaml_example)
