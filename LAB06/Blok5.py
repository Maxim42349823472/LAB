def is_divisible_by_its_digits(num):

    digits = [int(d) for d in str(num) if d != '0']  

    return all(num % digit == 0 for digit in digits)


def find_numbers(n):

    result = []

    for i in range(1, n + 1):

        if is_divisible_by_its_digits(i):

            result.append(i)

    return result


def main():

    n = int(input("Введите натуральное число n: "))

    divisible_numbers = find_numbers(n)

    print("Числа, не превосходящие", n, "и делящиеся на каждую из своих цифр:", divisible_numbers)


if __name__ == "__main__":

    main()









def reverse_digits(n):

    if n < 10:

        print(n, end=' ')  # печатаем последнюю цифру

    else:

        print(n % 10, end=' ')  # печатаем последнюю цифру

        reverse_digits(n // 10)  # рекурсивно вызываем для оставшейся части числа


def main():

    number = int(input("Введите натуральное число: "))

    print("Цифры числа", number, "в обратном порядке:")

    reverse_digits(number)


if __name__ == "__main__":

    main()
