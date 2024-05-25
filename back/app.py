
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
# импортируем модуль sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from moviepy.editor import *
import whisper


app = FastAPI()


# audioClip = AudioFileClip("tutor.mp4") #взяли аудио
# audioClip.write_audiofile("tutor.wav", buffersize=50000) #создали и и записали аудиофайл

@app.post("/video_to_txt/")
async def video_to_txt():
    model = whisper.load_model("base") #загружаем базовую модель для транскрибирования
    result = model.transcribe("files/tutor.wav") #результат работы транскрибирования из аудиофайла
    with open("tutor.txt", "w", encoding="utf-8") as f:
        f.write(result["text"]) #записываем в новый текстовый файл результат работы программы (только текст)
    # задаем язык и количество предложений в резюме
    LANGUAGE = 'russian'
    SENTENCES_COUNT = 20
    # создаем парсер и суммаризатор
    #parser = PlaintextParser.from_string('Ваш текст здесь', Tokenizer(LANGUAGE))
    parser = PlaintextParser.from_file("tutor.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    # выводим резюме
    f = open("1.txt", "w", encoding="utf-8")
    for index, sentence in enumerate(summarizer(parser.document, SENTENCES_COUNT)):
        f.write(str(index+1) + ". " + str(sentence)+"\n")
        print(sentence)
	
    