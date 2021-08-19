"""
find the peak in unsorted list of integer
time complexity: O(log(n))
space complexity: O(1)
"""


def find_peak(list):
    start, end = 0, len(list) - 1
    while start < end:
        mid = start + (end - start) // 2

        # Check if it's a peak
        if list[mid] > list[mid - 1] and list[mid] > list[mid + 1]:
            return list[mid]
        if list[mid - 1] > list[mid + 1]:
            end = mid
        else:
            start = mid + 1
        return list[start]
