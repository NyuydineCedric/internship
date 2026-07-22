#CUSTOM SORTING WITHOUT SORTED
def bubble_sort(numbers):
    
    for i in range(len(numbers)):

        for j in range(len(numbers) - 1):

            if numbers[j] > numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def bubble_sort_desc(numbers):

    for i in range(len(numbers)):

        for j in range(len(numbers) - 1):

            if numbers[j] < numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


numbers = [5, 3, 8, 4, 2]

print(bubble_sort(numbers.copy()))
print(bubble_sort_desc(numbers.copy()))