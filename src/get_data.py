import requests
import json

def fetch_news(api_key, query='technology', page=1):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    API_KEY = '3d7d9fb79fe442b7b224a9c0529c76fe'  # Replace with your News API key
    news_data = fetch_news(API_KEY)

    # Save the data
    with open('./data/raw/raw.txt', 'w') as file:
        json.dump(news_data, file)
