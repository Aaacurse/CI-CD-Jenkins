from src.operations import add,subtract,multiply

def test_add():
    assert add(1,1)==2
    assert add(-1,1)==0
    assert add(-1,-1)==-2

def test_subtract():
    assert subtract(5,3)==2
    assert subtract(2,2)==0
    assert subtract(-1,-1)==0
    assert subtract(3,5)==-2

def test_multiply():
    assert multiply(1,0)==0
    assert multiply(3,5)==15
    assert multiply(-1,-1)==1