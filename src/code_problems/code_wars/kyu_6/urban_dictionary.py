import re


class WordDictionary:
    def __init__(self):
        self.database = []

    def add_word(self, word):
        self.database.append(word)

    def search(self, word):
        for item in self.database:
            pattern = r'\b' + word + r'\b'
            result = re.search(pattern, item)
            if result:
                print(f'achei: {item}')
                return True
        return False


wd = WordDictionary()

wd.add_word('codewars')
wd.search('co..w...')
