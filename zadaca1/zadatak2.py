def funkcija2(l, d):
    assert isinstance(l, list) and isinstance(d, dict)
    assert len(l) == len(d)
    assert all(isinstance(x, int) for x in l)
    # return {k: l[v] if 5 <= v < 10 else -1 for k, v in dct.items()}
    return {k:v if (v > 5 and v < 10) else -1 for k,v in zip(d,l)}

"""
def funkcija1(l, d):
    if not (isinstance(l, list) and isinstance(d, dict)):
        raise ValueError("Moraju biti lista i dictionary!")
    if len(l) != len(d):
        raise ValueError("Lista i dictionary moraju imati isti broj elemenata.")
    if not all(isinstance(x, int) for x in l):
        raise ValueError("Svi elementi u listi moraju biti integeri.")
    return {k: l[v] if 5 <= v < 10 else -1 for k, v in d.items()}
"""
    
print(funkcija2([8,7,1], {1:2,2:1,3:2}))

 
