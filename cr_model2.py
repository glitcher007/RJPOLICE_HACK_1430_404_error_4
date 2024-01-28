
import os
from os import listdir
import nltk
from os.path import isfile, join
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r'C:\Users\glitcher\Desktop\Rj_hackathon_2\venv\ocr.json'
from google.cloud import vision
from my_timer import my_timer
from googletrans import Translator
from pre_process import perform_ner,stem,tokenize
from pre_process import remove_stopwords,remove_specific_characters
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summarize import t5_summarizer
from gtts import gTTS

#nltk.download('stopwords')
#ltk.download('punkt')
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
    mypath = r"C:/Users/glitcher/Desktop/Rj_hackathon_2/venv/imgs"
    only_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for image_path in only_files:
        # print(os.path.join(mypath, image_path))
        text = detect_text(os.path.join(mypath, image_path))
        english_text = translate_hindi_to_english(text)
        #token_text=tokenize(english_text)
        removed_words=remove_stopwords(english_text)
        lowered_words=removed_words.lower()
        new_words=remove_stopwords(lowered_words)
        new_words1=remove_specific_characters(new_words)
       # print(new_words1)
        token_text=tokenize(new_words1)
        
        
        
        
        #print(token_text)
        
       # print(token_text)
        
        return  text_to_speech(text)
        
       

def translate_hindi_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='hi', dest='en')
    return translation.text




def text_to_speech(text, language='en', output_file='output.mp3'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech to an MP3 file
    tts.save(output_file)

    # Play the generated MP3 file (optional)
    os.system("start " + output_file)  # This command may vary based on your operating system




if __name__ == "__main__":
     main()