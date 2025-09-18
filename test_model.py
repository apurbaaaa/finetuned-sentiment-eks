from transformers import pipeline

nlp = pipeline("sentiment-analysis", model="./sentiment_model")

print(nlp("I really love this class!"))
print(nlp("This subject is terrible."))
