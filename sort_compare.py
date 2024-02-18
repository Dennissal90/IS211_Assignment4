import time
import random

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    end = time.time()
    return end - start

def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2
    end = time.time()
    return end - start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return end - start

def main():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        total_time = {'insertion': 0, 'shell': 0, 'python': 0}
        for _ in range(100):
            test_list = random.sample(range(2000000), size)
            total_time['insertion'] += insertion_sort(test_list[:])  # Copy list to avoid in-place sorting
            total_time['shell'] += shell_sort(test_list[:])  # Copy list to avoid in-place sorting
            total_time['python'] += python_sort(test_list[:])  # Copy list to avoid in-place sorting

        print(f"For list size {size}:")
        print(f"Insertion Sort took {total_time['insertion'] / 100:.7f} seconds to run, on average")
        print(f"Shell Sort took {total_time['shell'] / 100:.7f} seconds to run, on average")
        print(f"Python's built-in Sort took {total_time['python'] / 100:.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
