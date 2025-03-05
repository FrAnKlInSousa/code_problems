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



def table_data(name: str, level: int):
    formated_name = format_name(name)
    print(formated_name, 'test_' + formated_name)
    print(
        f'| [{formated_name}.py]'
        f'(src/code_problems/code_wars/kyu_{level}/{formated_name}.py)'
        f' | [{name}]() | {level} Kyu |'
    )
