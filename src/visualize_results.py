import json
import matplotlib.pyplot as plt
import pandas as pd

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def visualize_data(articles):
    df = pd.DataFrame(articles)
    df['title_length'] = df['title'].apply(len)
    plt.figure()  # Create a new figure
    df['title_length'].hist(bins=15)
    plt.title('Distribution of Title Lengths')
    plt.xlabel('Title Length')
    plt.ylabel('Frequency')

    # Save plot to a file
    plt.savefig('./results/title_length_distribution.png')

if __name__ == '__main__':
    processed_data_path = './data/processed/processed.txt'
    articles = load_data(processed_data_path)
    visualize_data(articles)
