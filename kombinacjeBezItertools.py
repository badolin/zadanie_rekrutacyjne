def kombinacje(cechy):
    keys, values = zip(*cechy.items())

    result = [[]]
    for value in values:
        result = [x+[y] for x in result for y in value]

    kombinacje = [dict(zip(keys, v)) for v in result]
    return kombinacje

def main():
    input = {
        "szerokość": {"20cm", "16cm", "10cm"},
        "wysokość": {"30cm", "40cm"},
        "kolor": {"czarny", "biały", "zielony"},
        "długośc": {"100cm", "200cm", "400cm", "500cm"}
    }
    result = kombinacje(input)
    for x in result:
        print(x)

if __name__ == '__main__':
    main()
