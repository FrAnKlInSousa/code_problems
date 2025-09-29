import pytest

from src.code_problems.code_wars.kyu_6.unique_sets import unique_sets


@pytest.mark.parametrize('group,expected', [
    ([ {5,8 , (1,2), "rvbc" }, {"fnyh", "esa", 1}, {("cev","cdv",0), 18}   ], False),
    ([ {5,8 , (1,2), "rvbc" }, {"fnyh", "esa", 6}, {("cev","cdv",0), 18}   ], True),
    ([], True),
    ([ {5,8 , (1,2), "rvbc" },
       { frozenset({"fnyh", 0}), "esa", 6},
       {("cev","cdv",0), 18}   ], False),
    ([ {5,8 , (1,(2,6,(9,100,107),890,(1,(5,6))), (3,4,5)), "rvbc" }, {"fnyh", "esa", 6}, {("cev","cdv",20), 18}   ], False),
    ([{frozenset({72, (31, 'fnlxzm', 9, 'efepgl'), 'wqboyq', 76}), 89, ('mveya', ('ovmdf', 'feuo'), 'vnrm'), frozenset({frozenset({64, frozenset({'seivwl', 'chtns', 92, 63}), 'jmja'}), 5, 'zdmdlw'})}, {('esisi', 'gikm'), frozenset({97, 11, 13}), frozenset({'ossxfi', frozenset({69, 'xrkj'}), 'epafk', ('jhrkl', 86, 25)}), 'yuao'}, {'jaxyog', 'jou', ((73,), frozenset({50}), 'tqj', frozenset({72, 'lipcck', 100, 'ogcsnb'})), frozenset({'ydoflv'})}], False),
])
@pytest.mark.parametrize('function', [unique_sets])
def test_unique_sets(expected, function, group):
    result = function(group)
    assert result == expected




