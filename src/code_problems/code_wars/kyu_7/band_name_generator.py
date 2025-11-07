def band_name_generator(name: str):
    if name[0] == name[-1]:
        return f'{name.title()}{name[1::]}'
    return f'The {name.title()}'
