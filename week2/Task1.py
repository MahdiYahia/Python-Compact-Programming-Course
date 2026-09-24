def get_last_value(item):
    return item[-1]

if __name__ == "__main__":
    tuples_sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    sorted_tuples = sorted(tuples_sample_list, key=get_last_value)
    print(sorted_tuples)