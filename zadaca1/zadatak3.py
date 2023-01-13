def funkcija3(artikli):
    assert isinstance(artikli, list)
    assert all(isinstance(d, dict) for d in artikli)
    for d in artikli:
        assert all(k in d for k in ("cijena", "naziv", "kolicina"))
    ukupna_cijena = sum(d["cijena"]*d["kolicina"] for d in artikli)
    lista_artikla = [{"naziv": d["naziv"], "cijena": d["cijena"], "kolicina": d["kolicina"]} for d in artikli]
    return {"ukupno": {"artikli": lista_artikla}, "ukupna_cijena": ukupna_cijena}

"""
def funkcija3(artikli):
    if not isinstance(artikli, list):
        raise ValueError("Error. Mora biti lista.")
    if not all(isinstance(d, dict) for d in artikli):
        raise ValueError("Error. Svi elementi u listi moraju biti dictionary. ")
    for d in artikli:
        if not all(k in d for k in ("cijena", "naziv", "kolicina")):
            raise ValueError("Error. Svi dictionary moraju imati odgovarajuca 3 kljuca.")
    ukupna_cijena = sum(d["cijena"]*d["kolicina"] for d in artikli)
    lista_artikla = [{"naziv": d["naziv"], "cijena": d["cijena"], "kolicina": d["kolicina"]} for d in artikli]
    return {"ukupno": {"artikli": lista_artikla}, "ukupna cijena": ukupna_cijena}
"""

print(funkcija3([{"cijena":8,"naziv":"Kruh","kolicina":3}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}]))
