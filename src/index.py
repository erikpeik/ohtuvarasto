from varasto import Varasto


def main():
    olutta = Varasto(100.0, 20.2)
    print(f"Luonnin jälkeen Olutvarasto: {olutta}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")


if __name__ == "__main__":
    main()
