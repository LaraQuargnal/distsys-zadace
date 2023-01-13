def funkcija1(x):
    if not all(isinstance(y, str) for y in x):
        raise ValueError("Svi elementi u listi moraju biti string!")
    return [y for y in x if len(y) > 4]

print(funkcija1(["Pas", "Macka", "Stol"]))
 
