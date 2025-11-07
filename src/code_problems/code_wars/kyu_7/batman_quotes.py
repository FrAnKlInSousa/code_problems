class BatmanQuotes(object):
    def __init__(self):
        self.persons = {'B': 'Batman', 'R': 'Robin', 'J': 'Joker'}

    @staticmethod
    def find_index(hero: str):
        for char in hero:
            if char.isdigit():
                return int(char)

    def find_person(self, hero: str):
        return self.persons.get(hero[0])

    @staticmethod
    def get_quote(quotes: list, hero: str):
        index = BatmanQuotes.find_index(hero)
        person = BatmanQuotes().find_person(hero)
        return f'{person}: {quotes[index]}'


class BatmanQuotesClever(object):
    @staticmethod
    def get_quote(quotes: list, hero: str):
        heroes = ['Batman', 'Robin', 'Joker']
        index = int(next(filter(str.isdigit, hero)))
        return f'{heroes[index]}: {quotes[index]}'
