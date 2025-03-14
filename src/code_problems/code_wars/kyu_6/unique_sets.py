from typing import Any, Generator, List, Set, Union

from src.utils.check_processing_time import timeit_decorator


@timeit_decorator(repeats=100000)
def unique_sets(group: List[set]) -> bool:
    found_values = set()

    def has_duplicated_value(my_set_list, scanner: set) -> bool:
        for sub_item in my_set_list:
            if isinstance(sub_item, tuple):
                if not has_duplicated_value(sub_item, found_values):
                    continue
                return True
            if isinstance(sub_item, (set, frozenset)):
                if not has_duplicated_value(frozenset(sub_item), found_values):
                    continue
                return True
            if sub_item in scanner:
                return True
            scanner.add(sub_item)
        return False

    for item in group:
        if has_duplicated_value(item, found_values):
            return False
    return True


def unique_sets_gpt_improvement(group: List[set]) -> bool:
    found_values = set()

    def has_duplicated_value(item: Union[set, frozenset, tuple]) -> bool:
        if isinstance(item, (set, frozenset, tuple)):
            for sub_item in item:
                if has_duplicated_value(sub_item):
                    return True
        else:
            if item in found_values:
                return True
            found_values.add(item)
        return False

    return not any(has_duplicated_value(item) for item in group)


def unique_sets_gpt(groups: List[Set[Any]]) -> bool:
    seen_values = set()

    def extract_values(item):
        """Retorna um conjunto de valores individuais
        extraídos do item, explorando estruturas compostas."""
        if isinstance(item, (tuple, frozenset)):
            return {
                sub_value for sub in item for sub_value in extract_values(sub)
            }
        return {item}

    for group in groups:
        values_in_group = set()

        for item in group:
            extracted = extract_values(item)

            # Verifica se há valores repetidos dentro do mesmo grupo
            if values_in_group & extracted:
                return False

            values_in_group |= extracted  # Adiciona ao grupo atual

        # Verifica se há valores já vistos em outros conjuntos
        if seen_values & values_in_group:
            return False

        seen_values |= values_in_group  # Adiciona ao conjunto global

    return True


def unique_sets_gpt_performance(groups: List[Set[Any]]) -> bool:
    seen_values = set()

    def extract_values(item: Any) -> Generator[Any, None, None]:
        """Gera todos os valores individuais dentro de um item,
        incluindo estruturas compostas."""
        if isinstance(item, (tuple, frozenset)):
            for sub in item:
                yield from extract_values(sub)
        else:
            yield item

    for group in groups:
        values_in_group = set()

        for item in group:
            for value in extract_values(item):
                if value in values_in_group:
                    return False
                values_in_group.add(value)

        if (
            seen_values & values_in_group
        ):  # Verifica se já apareceu em outro conjunto
            return False

        seen_values |= values_in_group  # Atualiza o conjunto global

    return True


unique_sets([
    {
        frozenset({72, (31, 'fnlxzm', 9, 'efepgl'), 'wqboyq', 76}),
        89,
        ('mveya', ('ovmdf', 'feuo'), 'vnrm'),
        frozenset({
            frozenset({64, frozenset({'seivwl', 'chtns', 92, 63}), 'jmja'}),
            5,
            'zdmdlw',
        }),
    },
    {
        ('esisi', 'gikm'),
        frozenset({97, 11, 13}),
        frozenset({
            'ossxfi',
            frozenset({69, 'xrkj'}),
            'epafk',
            ('jhrkl', 86, 25),
        }),
        'yuao',
    },
    {
        'jaxyog',
        'jou',
        (
            (73,),
            frozenset({50}),
            'tqj',
            frozenset({72, 'lipcck', 100, 'ogcsnb'}),
        ),
        frozenset({'ydoflv'}),
    },
])
