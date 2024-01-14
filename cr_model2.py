
import os
from os import listdir
from os.path import isfile, join
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r'C:\Users\glitcher\Desktop\Rj_hackathon_2\venv\ocr.json'
from google.cloud import vision
from my_timer import my_timer
import time


def detect_text(path):
    client = vision.ImageAnnotatorClient()
    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    ocr_text = []
    for text in texts:
        ocr_text.append(f"\r\n{text.description}")
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return texts[0].description


def main():
    mypath = r"C:/Users/glitcher/Desktop/Rj_police_hackathon/venv/imgs"
    only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for image_path in only_files:
        # print(os.path.join(mypath, image_path))
        text = detect_text(os.path.join(mypath, image_path))
        #english_text = translate_hindi_to_english(text)
        print(text)
       
'''
def translate_hindi_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text
'''

if __name__ == "__main__":
     main()