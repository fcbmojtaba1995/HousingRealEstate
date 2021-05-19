from constants import PROFILES_FILE_PATH
from store import load_data


class Client:

    @staticmethod
    def search():
        return load_data(PROFILES_FILE_PATH)