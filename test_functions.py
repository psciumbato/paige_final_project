import mock
import builtins

from functions import check_input
from functions import get_residence
from functions import get_partner
from functions import get_kids
from functions import get_car

def test_check_input():
    with mock.patch.object(builtins, 'input', lambda _: 'some_input'):
        assert check_input(question='a') == 'some_input'
        
def test_get_residence():
    #with mock.patch.object(__builtins__, 'input', lambda _: 'r'):
    #assert get_residence() in ['mansion', 'apartment', 'shack', 'house']
    pass

def test_get_partner():
    #with mock.patch.object(__builtins__, 'input', lambda _: 'some_input'):
    assert get_partner
        
def test_get_kids():
    #with mock.patch.object(__builtins__, 'input', lambda _: 'some_input'):
    assert get_kids
        
def test_get_car():
    #with mock.patch.object(__builtins__, 'input', lambda _: 'some_input'):
    assert get_car