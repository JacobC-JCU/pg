print("Hello world!")

def number (cislo):
    print("Funkce spuštěná.")
    if cislo % 2 == 0:
        print(f"Cislo {cislo} je sude.")
    else:
        print(f"Cislo {cislo} je liché.")


if __name__ == "__main__":
    number(2)