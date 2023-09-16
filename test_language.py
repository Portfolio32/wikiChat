from language import matches
import pytest

def test_synonyms():
    assert matches("ok", "fine") == 1
    assert matches("ok I'm good", "fine I'm good") == 3


def test_punctuations():
    assert matches("An apple fell.", "An apple fell.") == 3
    assert matches("An apple fell?", "An apple fell?") == 3
    assert matches("Among mammal, cattle, deer, horse, lion, bat, bear, wolf", "Among mammal, cattle, deer, horse, lion, bat, bear, wolf") == 9

def test_parenthese():
    assert matches("articulated animal (arthropod annelid)","articulated animal (arthropod annelid)") == 4

def test_normal_short():
    assert matches("I", "I") == 1
    assert matches("An apple fell", "An apple fell") == 3
    
def test_normal_long():
    assert matches("Despite what your teacher may have told you there is a wrong way to wield a lasso","Despite what your teacher may have told you there is a wrong way to wield a lasso") == 17

def test_empty():
    assert matches("","") == 0 
    assert matches("An apple fell off the tree", "") == 0
    assert matches("", "An apple fell off the tree") == 0

def test_invalids():
    with pytest.raises(TypeError):
        matches(1, 1)