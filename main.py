from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# импортируем модуль sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from moviepy.editor import *
import whisper


UPLOAD_DIR = Path() / 'uploads'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile/")
async def create_upload_files(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR / file_upload.filename
    with open(save_to, 'wb') as f:
        f.write(data)

    return {"Получилось!"}

    """ model = whisper.load_model("base") #загружаем базовую модель для транскрибирования
    result = model.transcribe("uploads/" + file_upload.filename) #результат работы транскрибирования из аудиофайла
   
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
	
    """
    

