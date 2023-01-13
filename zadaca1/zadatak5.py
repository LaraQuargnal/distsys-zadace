def funkcija5(studenti):
    return [{"id":i,"ime":j,"prezime":k} for i,j,k in sorted(studenti) if j[0] == k[0]]

print(funkcija5([(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]))
