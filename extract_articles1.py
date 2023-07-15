import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and extract the article title
    article_title = ''
    title_element = soup.find('h1')
    if title_element:
        article_title = title_element.text.strip()

    # Find and extract the article text
    article_text = ''
    article_content = soup.find('article')
    if article_content:
        paragraphs = article_content.find_all('p')
        for paragraph in paragraphs:
            article_text += paragraph.text.strip() + '\n'

    return article_title, article_text


def save_article_text(url_id, article_title, article_text):
    filename = f'{url_id}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(article_title + '\n\n')
        file.write(article_text)


# Read the input.xlsx file using pandas
df = pd.read_excel('input.xlsx')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    try:
        # Extract article text
        article_title, article_text = extract_article_text(url)

        # Save the article text to a text file
        save_article_text(url, article_title, article_text)

        print(f'Saved article {url}.txt')
    except Exception as e:
        print(f'Error extracting article {url}: {str(e)}')

print('Extraction and saving completed!')
