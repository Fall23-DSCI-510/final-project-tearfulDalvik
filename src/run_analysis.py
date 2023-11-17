import json
import pandas as pd

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def analyze_data(articles):
    df = pd.DataFrame(articles)
    return df.describe()

if __name__ == '__main__':
    processed_data_path = './data/processed/processed.txt'
    articles = load_data(processed_data_path)
    analysis_results = analyze_data(articles)
    print(analysis_results)
