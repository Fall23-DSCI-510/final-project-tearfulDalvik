
import json

def clean_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        articles = data.get('articles', [])

    clean_articles = []
    for article in articles:
        cleaned_article = {key: article[key] for key in ['title', 'description', 'content']}
        clean_articles.append(cleaned_article)

    return clean_articles

if __name__ == '__main__':
    raw_data_path = './data/raw/raw.txt'
    cleaned_data = clean_data(raw_data_path)

    with open('./data/processed/processed.txt', 'w') as file:
        json.dump(cleaned_data, file)
