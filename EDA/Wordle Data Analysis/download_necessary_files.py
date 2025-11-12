import kaggle
from bs4 import BeautifulSoup
import requests
import csv

kaggle.api.authenticate()

kaggle.api.dataset_download_files("benhamner/wordle-tweets", 
    path='assets',
    unzip=True)


page_to_scrape = requests.get("https://wordfinder.yourdictionary.com/wordle/answers/")
soup = BeautifulSoup(page_to_scrape.content, 'html.parser')
answers = soup.find_all('tr')

data_to_save = []

for item in answers:
    
    tokens = item.get_text().split()
    
   
    if len(tokens) >= 4:
        number = tokens[2]
        word = tokens[3]
        data_to_save.append([number, word])


with open('assets/wordle_answers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Number', 'Word'])  
    writer.writerows(data_to_save)

print("Data saved to wordle_answers.csv")