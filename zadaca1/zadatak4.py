def funkcija4(lista1, lista2):
    assert len(lista1) == len(lista2), "Liste moraju imati isti broj elemenata. "
    return [x if x == y else -1 for x, y in zip(lista1, lista2)]

print(funkcija4([1,2,3,4,5],[2,2,4,4,5]))


  
  
