ilosc_dodanych = int(input())

class ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

    def __repr__(self):
        wydruk = "(’"+self.tytul+"’,’"+self.autor+"’)"
        return wydruk

ksiazki = []

for i in range(ilosc_dodanych):
    dane = eval(input())
    tytul = dane[0]
    autor = dane[1]
    rok = dane[2]
    egzemplarz = ksiazka(tytul, autor, rok)
    ksiazki.append(egzemplarz)

tytul = []


for egzemplarz in ksiazki:
    tytul.append(egzemplarz.tytul)
ilosc = []

for n in tytul:
    ilosc.append(tytul.count(n))
x = 0
razem = []
for egzemplarz in ksiazki:
    razem.append("('"+egzemplarz.tytul+"', '"+egzemplarz.autor+"', "+str(ilosc[x])+")")
    x += 1
    razem = set(razem)
    razem = sorted(razem)

for razem_egzemplarze in razem:
    print(razem_egzemplarze)
