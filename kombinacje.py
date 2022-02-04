import itertools

def kombinacje(cechy):
    klucze, wartosci = zip(*cechy.items())
    kombinacje = [dict(zip(klucze, v)) for v in itertools.product(*wartosci)]
    return kombinacje


def main():
    input = {
        "szerokość": {"20cm", "16cm", "10cm"},
        "wysokość": {"30cm", "40cm"},
        "kolor": {"czarny", "biały", "zielony"},
    }
    wynik = kombinacje(input)
    for x in wynik:
        print(x)
if __name__ == '__main__':
    main()
