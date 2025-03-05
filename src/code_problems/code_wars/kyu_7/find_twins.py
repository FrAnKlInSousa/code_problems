def find_twins(citizens: list):
    for citizen in citizens:
        if citizens.count(citizen) > 1:
            return citizen
