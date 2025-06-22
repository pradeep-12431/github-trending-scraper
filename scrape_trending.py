import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch GitHub Trending Page
url = "https://github.com/trending"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Step 2: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
repo_tags = soup.find_all('h2', class_='h3 lh-condensed')[:5]  # Top 5

# Step 3: Extract Repo Names and Links
data = []
for tag in repo_tags:
    anchor = tag.find('a')
    repo_name = anchor.text.strip().replace('\n', '').replace(' ', '')
    repo_link = 'https://github.com' + anchor['href']
    data.append([repo_name, repo_link])

# Step 4: Write to CSV
with open('trending_repos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Repository Name', 'Link'])
    writer.writerows(data)

print("✅ Trending repositories scraped and saved to trending_repos.csv")
