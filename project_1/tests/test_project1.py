from project_1 import main

def test_function():
    r = main.my_function() 
    assert r == "Hello World"

def test_function2():
    r = main.my_function()
    assert r != "Pakistan Zindabad"       