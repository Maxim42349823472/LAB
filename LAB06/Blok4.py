
def find_negative_pairs(arr):

    pairs = []

    for i in range(len(arr) - 1):

        if arr[i] < 0 and arr[i + 1] < 0:

            pairs.append((arr[i], arr[i + 1]))

    return pairs


def main():

    array = [-1, -2, 3, -4, -5, 6, -7, -8, 9, 10]


    negative_pairs = find_negative_pairs(array)

    print("Пары отрицательных чисел, стоящих рядом:", negative_pairs)


if __name__ == "__main__":

    main()







def remove_duplicates(arr):

    # Создаем новый массив без дубликатов

    unique_elements = []

    for num in arr:

        if num not in unique_elements:

            unique_elements.append(num)

    return unique_elements


def main():

    array = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]


    unique_array = remove_duplicates(array)

    print("Массив без одинаковых элементов:", unique_array)


if __name__ == "__main__":

    main()
