
def merge_sorted_arrays(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:]); result.extend(b[j:])
    return result


def main():
    print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))

if __name__ == "__main__":
    main()
