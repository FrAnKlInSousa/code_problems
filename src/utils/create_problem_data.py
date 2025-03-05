def format_name(name: str):
    name = name.lower().replace(' ', '_').replace('#', '')
    test = 'test_' + name
    print(name, test)
    return name


def table_data(name: str, level: int):
    print(
        f'| [{format_name(name)}.py]'
        f'(src/code_problems/code_wars/kyu_{level}/)'
        f' | [{name}]() | {level} Kyu |'
    )
