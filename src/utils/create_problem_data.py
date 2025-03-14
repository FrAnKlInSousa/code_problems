from src.utils.remove_extra_spaces import remove_extra_spaces


def format_name(name: str):
    filtered_name = []
    for char in name:
        if char.isalnum():
            filtered_name.append(char)
        else:
            filtered_name.append(' ')
    temp_name = ''.join(filtered_name)
    temp_name = remove_extra_spaces(temp_name)
    final_name = temp_name.lower().replace(' ', '_')
    return final_name


def build_path(source, level: [int, str]):
    path = f'src/code_problems/{source}/'
    difficult = ''
    if source == 'code_wars':
        path += f'kyu_{level}'
        difficult += f'{level} Kyu'
    elif source == 'leetcode':
        path += level
        difficult = level.capitalize()
    return path, difficult


def table_data(name: str, level: int | str = 'easy', source='code_wars'):
    formated_name = format_name(name)
    print(formated_name, 'test_' + formated_name)
    path, difficult = build_path(source, level)

    print(
        f'| [{formated_name}.py]'
        f'({path}/{formated_name}.py)'
        f' | [{name}]() | {difficult} |'
    )
