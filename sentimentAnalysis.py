from transformers import pipeline
import pandas as pd
import json
import os

def sentimentAnalysis():


    # Create the directory for saving reviews
    if not os.path.exists('reviews'):
        os.makedirs('reviews')  

    # Load ABSA model from Hugging Face
    absa = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    # open file
    dataf = pd.read_csv(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\Data\reviews.csv")
    reviews = dataf['text']

    positive = {}
    negative = {}
    neutral = {}

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for review in reviews:
        sentiment = absa(review)
        rating = sentiment[0]['label'].split()[0]

        rating = int(rating)

        # negative
        if rating < 2:
            negative[negative_count] = review
            negative_count += 1

        # neutral
        elif rating == 2:
            neutral[neutral_count] = review
            neutral_count += 1

        # positive
        elif rating > 2:
            positive[positive_count] = review
            positive_count += 1

    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\negative.json", 'w+') as file:
        json.dump(negative, file)
    
    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\positive.json", 'w+') as file:
        json.dump(positive, file)

    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\neutral.json", 'w+') as file:
        json.dump(neutral, file)

    reviewCount = {"positive" : positive_count, 
            "negative" : negative_count,
            "neutral" : neutral_count
            }

    with open(r"C:\Tejeswar\product Review\Aspect Based Product Analysis\Aspect Based Sentiment Analysis\reviews\count.json", 'w+') as file:
        json.dump(reviewCount, file)

if __name__ == '__main__':
    sentimentAnalysis()