from transformers import pipeline
from webScraper import webScrape
import pandas as pd 

def getSentimentHelper(text):
    classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
    prediction = classifier(text)
    prediction = prediction[0]
    pred = pd.DataFrame.from_records(prediction)
    result = pred.sort_values(by='score', ascending=False)
    result = result.iloc[0]['label']
    return result 


#this is where the user will input texts
def get_sentiment(song_title, artist_name):
    lyrics = webScrape(song_title, artist_name)
    lyrics = open("lyrics.txt")
    data = lyrics.read()
    lyrics.close()
    sentiment = getSentimentHelper(data)
    return sentiment    



# song_title = "Float on"
# artist_name = "Modest Mouse"
# print(get_sentiment(song_title, artist_name))