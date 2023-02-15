from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    # проверяем что по переданному пути есть файл и он имеет расширение ПДФ
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
    # читаем ПДФ файл в строку
        # используем контекстный менеджер
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            # пробегаемся по всем страницам и извлекаем текст из каждой страницы
            pages = [page.extract_text() for page in pdf.pages]
        # склеиваем страницы между собой
        text = ''.join(pages)
        # удаляем из текста переносы строки (так как они будут восприниматься как длительные паузы)
        text = text.replace('\n', '')

        # формируем айдио-файл
        my_audio = gTTS(text=text, lang=language)
        # получаем имя файла с помощью свойства stem
        file_name = Path(file_path).stem
        # сохраняем аудио-файл с помощью save
        my_audio.save(f'{file_name}.mp3')

        # возвращаем ответ об успешно проделанной работе
        return f'[+] {file_name}.mp3  saved sucessfully'
    else:
        return 'File not exists'



def main():
    file_path = input("Enter a file's path: ")
    language = input("Choose language ['en' or 'ru']: ")
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()

