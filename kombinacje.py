import itertools

def kombinacje(cechy):
    keys, values = zip(*cechy.items())
    kombinacje = [dict(zip(keys, v)) for v in itertools.product(*values)]
    return kombinacje


def main():
    input = {
        "szerokość": {"20cm", "16cm", "10cm"},
        "wysokość": {"30cm", "40cm"},
        "kolor": {"czarny", "biały", "zielony"},
    }
    result = kombinacje(input)
    for x in result:
        print(x)
if __name__ == '__main__':
    main()
