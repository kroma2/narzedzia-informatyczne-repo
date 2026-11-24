"""Przykład do dokumentacji: sortowanie bąbelkowe."""


def bubble_sort(data):
    """Zwraca nową listę posortowaną rosnąco."""
    result = data.copy()
    n = len(result)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


if __name__ == "__main__":
    values = [7, 2, 9, 1, 5]
    print(bubble_sort(values))
