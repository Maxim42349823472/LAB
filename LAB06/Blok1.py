def convert_to_kilograms(unit, mass):

    if unit == 1:  # килограмм

        return mass

    elif unit == 2:  # миллиграмм

        return mass / 1_000_000

    elif unit == 3:  # грамм

        return mass / 1000

    elif unit == 4:  # тонна

        return mass * 1000

    elif unit == 5:  # центнер

        return mass * 100

    else:

        return None


def main():

    print("Введите номер единицы измерения:")

    print("1 — килограмм")

    print("2 — миллиграмм")

    print("3 — грамм")

    print("4 — тонна")

    print("5 — центнер")


    try:

        unit = int(input("Номер единицы измерения: "))

        mass = float(input("Введите массу: "))


        kilograms = convert_to_kilograms(unit, mass)


        if kilograms is not None:

            print(f"Масса в килограммах: {kilograms:.6f} кг")

        else:

            print("Некорректный номер единицы измерения.")

    except ValueError:

        print("Пожалуйста, введите корректные числовые значения.")


if __name__ == "__main__":

    main()