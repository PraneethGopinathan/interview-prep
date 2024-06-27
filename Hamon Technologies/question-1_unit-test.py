# Corrected version of the code with unit test case.
# Used Pytest here
# To run the unit-test install pytest package and run pytest question-1_unit-test.py

def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r

def test_empty_string():
    assert f("") == {}

def test_single_character():
    assert f("a") == {'a': 1}

def test_repeated_characters():
    assert f("aa") == {'a': 2}

def test_multiple_characters():
    assert f("ab") == {'a': 1, 'b': 1}

def test_mixed_characters():
    assert f("aabbcc") == {'a': 2, 'b': 2, 'c': 2}

def test_special_characters():
    assert f("a!a!b@b") == {'a': 2, '!': 2, 'b': 2, '@': 1}


# print(f("praneeth"))