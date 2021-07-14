"""
Find Intersection

Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will
represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string
containing the numbers that occur in elements of strArr in sorted order. If there is no intersection,
return the string false.

Examples

Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
Output: 1,9,10
"""


def find_intersection(str_arr):
    array_list = []
    for array in str_arr:
        array = array.replace(',', '').split()
        array_list.append(map(int, array))

    set_list = map(set, array_list)
    intersection = set.intersection(*set_list)
    str_intersection = ','.join(map(str, sorted(intersection)))

    if str_intersection:
        return str_intersection

    return False


if __name__ == "__main__":
    print(find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))