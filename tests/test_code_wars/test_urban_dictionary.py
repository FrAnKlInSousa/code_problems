from src.code_problems.code_wars.kyu_6.urban_dictionary import WordDictionary



def test_urban_dictionary():
    wd = WordDictionary()
    wd.add_word("a")
    wd.add_word("at")
    wd.add_word("ate")
    wd.add_word("ear")
    assert wd.search("a") == True
    assert wd.search("a.") == True
    assert wd.search("a.e") == True
    assert wd.search("b") == False
    assert wd.search("e.") == False
    assert wd.search("ea.") == True
    assert wd.search("ea..") == False
    wd.add_word("co")
    wd.add_word("cod")
    wd.add_word("code")
    wd.add_word("codewars")
    assert wd.search("........") == True
    assert wd.search("c.o") == False
    assert wd.search("cod.") == True
    assert wd.search("c.o") == False
    assert wd.search("co..w..s") == True
    assert wd.search("co..w..") == False