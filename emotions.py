from transformers import pipeline

emotion_classifier = pipeline('sentiment-analysis')

text = "subject is intersting"
result = emotion_classifier(text)

print(result)
