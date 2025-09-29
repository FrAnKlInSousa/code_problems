from datetime import datetime


def villain_name(birthdate: datetime):
    first = [
        'The Evil',
        'The Vile',
        'The Cruel',
        'The Trashy',
        'The Despicable',
        'The Embarrassing',
        'The Disreputable',
        'The Atrocious',
        'The Twirling',
        'The Orange',
        'The Terrifying',
        'The Awkward',
    ]
    last = [
        'Mustache',
        'Pickle',
        'Hood Ornament',
        'Raisin',
        'Recycling Bin',
        'Potato',
        'Tomato',
        'House Cat',
        'Teaspoon',
        'Laundry Basket',
    ]

    final_day = birthdate.day % 10
    month = birthdate.month
    return f'{first[month - 1]} {last[final_day]}'
