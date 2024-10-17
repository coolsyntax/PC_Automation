from file_operations import move_to, desktop, make_folder, remove_folder, read_files
from word_operations import search_for_document, making_new_document, opening_existing_document
from wifi_operations import connect_to_wifi, enable_wifi, disable_wifi
from system_operations import lock_window, shutdown_system, empty_recycle_bin, restart_system, log_off
from utils import search_wikipedia, open_application, get_time, web_search


def process_command(query):
    if "move to folder" in query:
        move_to(query)
    elif "desktop" in query:
        desktop()
    elif "make folder" in query:
        make_folder()
    elif "remove folder" in query:
        remove_folder()
    elif "read files" in query:
        read_files()
    elif "search for document" in query:
        search_for_document()
    elif "make a new word document" in query:
        making_new_document()
    elif "open existing word document" in query:
        opening_existing_document()
    elif "wikipedia" in query:
        search_wikipedia(query)
    elif 'open application' in query:
        open_application(query)
    elif 'time' in query:
        get_time()
    elif 'search' in query or 'play' in query:
        web_search(query)
    elif 'lock window' in query:
        lock_window()
    elif 'shutdown system' in query:
        shutdown_system()
    elif 'empty recycle bin' in query:
        empty_recycle_bin()
    elif "restart" in query:
        restart_system()
    elif "log off" in query or "sign out" in query:
        log_off()
    elif "disable wi-fi" in query:
        disable_wifi()
    elif "enable wi-fi" in query:
        enable_wifi()
    elif "connect to wi-fi" in query:
        connect_to_wifi()
    elif 'quit' in query:
        exit()
