def bubble_sort(values):
    n = len(values)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        print(f"After pass {i + 1}: {values}")

        if not swapped:
            break

    return values


def main():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]

    print("Original list:", numbers)
    sorted_numbers = bubble_sort(numbers.copy())
    print("Sorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
    