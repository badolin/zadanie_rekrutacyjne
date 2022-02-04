def kombinacje(cechy):
    klucze, wartosci = zip(*cechy.items())

    wynik = [[]]
    for wartosc in wartosci:
        wynik = [x+[y] for x in wynik for y in wartosc]

    kombinacje = [dict(zip(klucze, v)) for v in wynik]
    return kombinacje

def main():
    input = {
        "szerokość": {"20cm", "16cm", "10cm"},
        "wysokość": {"30cm", "40cm"},
        "kolor": {"czarny", "biały", "zielony"},
        "długośc": {"100cm", "200cm", "400cm", "500cm"}
    }
    wynik = kombinacje(input)
    for x in wynik:
        print(x)

if __name__ == '__main__':
    main()
