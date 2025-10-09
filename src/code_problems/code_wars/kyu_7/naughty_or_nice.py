

def what_list_am_i_on(actions: list[str]):
    bad_things = 0
    good_things = 0
    for word in actions:
        if word.startswith(('b', 'f', 'k')):
            bad_things += 1
        elif word.startswith(('g', 's', 'n')):
            good_things += 1

    return 'naughty' if bad_things >= good_things else 'nice'
