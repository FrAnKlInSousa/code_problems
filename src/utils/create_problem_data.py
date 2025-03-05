def format_name(name: str):
    name = name.lower().replace(' ', '_').replace('#', '')
    return name


def table_data(name: str, level: int):
    formated_name = format_name(name)
    print(formated_name, 'test_' + formated_name)
    print(
        f'| [{formated_name}.py]'
        f'(src/code_problems/code_wars/kyu_{level}/{formated_name}.py)'
        f' | [{name}]() | {level} Kyu |'
    )
