from voice_engine import takeCommand
from greeting import WishMe
from command_processor import process_command
from file_operations import desktop

if __name__ == '__main__':
    WishMe()
    desktop()
    while True:
        query = takeCommand().lower()
        process_command(query)
