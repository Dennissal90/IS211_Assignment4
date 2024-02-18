import time
import random

def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end = time.time()
    return found, end-start

def ordered_sequential_search(a_list, item):
    a_list.sort()
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end = time.time()
    return found, end-start

def binary_search_iterative(a_list, item):
    a_list.sort()
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end-start

def binary_search_recursive(a_list, item):
    a_list.sort()
    start = time.time()

    def binary_search(a_list, item, first, last):
        if first > last:
            return False
        else:
            midpoint = (first + last) // 2
            if item == a_list[midpoint]:
                return True
            else:
                if item < a_list[midpoint]:
                    return binary_search(a_list, item, first, midpoint-1)
                else:
                    return binary_search(a_list, item, midpoint+1, last)

    found = binary_search(a_list, item, 0, len(a_list) - 1)
    end = time.time()
    return found, end-start

def main():
    list_sizes = [500, 1000, 5000]
    for size in list_sizes:
        total_time = {'ss': 0, 'oss': 0, 'bis': 0, 'brs': 0}
        for _ in range(100):
            test_list = random.sample(range(2000000), size)
            _, time_taken = sequential_search(test_list, -1)
            total_time['ss'] += time_taken

            _, time_taken = ordered_sequential_search(test_list, -1)
            total_time['oss'] += time_taken

            _, time_taken = binary_search_iterative(test_list, -1)
            total_time['bis'] += time_taken

            _, time_taken = binary_search_recursive(test_list, -1)
            total_time['brs'] += time_taken

        print(f"For list size {size}:")
        print(f"Sequential Search took {total_time['ss'] / 100:.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {total_time['oss'] / 100:.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {total_time['bis'] / 100:.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {total_time['brs'] / 100:.7f} seconds to run, on average")

if __name__ == "__main__":
    main()