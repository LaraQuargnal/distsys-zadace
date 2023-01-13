
def funkcija6(x, y):
    assert type(x) == type(y), "Parametri moraju biti istog tipa. "
    assert (type(x) == list or type(x) == dict), "Parametri moraju biti ili liste ili dictionary"
    if type(x) == list:
        return x + y
    else:
        return {**x, **y}

"""
def funkcija6(x,y):
    assert type(x) == type(y)
    assert isinstance(x, list) or isinstance(x, dict)
    if isinstance(x,list):
        return [*x,*y] 
    else:
        return {**x,**y}
"""

"""
def funkcija6(x, y):
    if type(x) != type(y):
        raise TypeError("Parametri nisu istog tipa. ")
    if type(x) != list and type(x) != dict:
        raise TypeError("Parametri moraju biti ili liste ili dictionary. ")
    if type(x) == list:
        return x + y
    else:
        return {**x, **y}
"""
    
print(funkcija6([1,2,1,2],[3,2]))
print(funkcija6({1:2,3:2},{5:2,4:1}))
