def total_resistance(resistances):

    total = 0

    for resistance in resistances:

        total += resistance

    return total


def main():

    n = int(input("Введите количество элементов в цепи: "))

    

    resistances = []

    for i in range(n):

        resistance = float(input(f"Введите сопротивление элемента {i + 1}: "))

        resistances.append(resistance)


    total = total_resistance(resistances)

    print(f"Общее сопротивление цепи: {total:.2f} Ом")

if __name__ == "__main__":

    main()





def largest_k(n):

    k = 0

    while (k + 1) ** 2 <= n:

        k += 1

    return k


def main():

  

    n = int(input("Введите целое число N (> 0): "))

    

    if n <= 0:

        print("Число N должно быть больше 0.")

        return


    k = largest_k(n)

    print(f"Наибольшее целое число K, квадрат которого не превосходит N: {k}")


if __name__ == "__main__":

    main()