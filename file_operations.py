import os
from voice_engine import speak, takeCommand


def desktop():
    desk = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    os.chdir(desk)
    speak("Do You Want to Know files and folder on your desktop")
    query = takeCommand().lower()
    if query == "yes":
        folders = os.listdir()
        check_for_folder(folders)
    elif query == "no":
        speak("Ok Got it")


def check_for_folder(folders):
    for folder in folders:
        if "." not in folder:
            speak(f"Folder {folder}")
        elif ".xlsx" in folder:
            speak(f"Excel file {folder}")
        elif ".txt" in folder:
            speak(f"Text file {folder}")
        elif ".ppt" in folder:
            speak(f"PPT {folder}")
        elif ".doc" in folder:
            speak(f"Word file {folder}")
        elif ".pdf" in folder:
            speak(f"PDF {folder}")


def move_to(query):
    keyword = "folder"
    before_keyword, keyword, after_keyword = query.partition(keyword)
    after_keyword = after_keyword.strip().lower()

    files = os.listdir()

    for file in files:
        if after_keyword == file.lower():
            os.chdir(file)
            print(os.getcwd())
            speak(f'Do you want to read files and folder of {file}')
            ans = takeCommand().lower()
            if "yes" in ans:
                folders = os.listdir()
                check_for_folder(folders)
            elif ans == "no":
                speak("Ok Got it")


def make_folder():
    speak("Please Say the name of the folder")
    folder_name = takeCommand().lower()
    os.mkdir(folder_name)
    speak(f"Folder {folder_name} has been created")


def remove_folder():
    speak("Please Tell the name of the folder to remove")
    folder_name = takeCommand().lower()
    path = os.path.join(os.getcwd(), folder_name)
    try:
        os.rmdir(path)
        speak(f"Folder {folder_name} has been removed")
    except OSError as e:
        speak(f"Unable to remove the folder. Error: {e}")


def read_files():
    folders = os.listdir()
    check_for_folder(folders
