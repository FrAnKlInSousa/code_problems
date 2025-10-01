import os

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
    path, difficult = build_path(source, level)

    file_name = f'{formated_name}'
    print(
        f'| [{formated_name}.py]'
        f'({path}/{formated_name}.py)'
        f' | [{name}]() | {difficult} |'
    )
    return file_name, level


def create_files(file_name, platform='code_wars', level='kyu_7'):
    base_dir = '/home/franklin/projetos/code_problems/'
    target_dir = f'{base_dir}src/code_problems/code_wars/{level}/'
    target_test_dir = f'{base_dir}tests/test_code_wars/'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        open(f'{target_dir}/__init__.py', 'w', encoding='utf-8').close()
    open(f'{target_dir}/{file_name}.py', 'w', encoding='utf-8').close()

    with open(
        f'{target_test_dir}/test_{file_name}.py', 'w', encoding='utf-8'
    ) as file:
        template = f"""import pytest


@pytest.mark.parametrize(',expected', [
    (),
])
@pytest.mark.parametrize('function', [])
def test_{file_name}(expected, function):
    result = function()
    assert result == expected"""
        print(template, file=file)


if __name__ == '__main__':
    file_name, level = table_data('asd', 7)
    create_files(file_name)
