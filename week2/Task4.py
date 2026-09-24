def strings_to_lists(strings):
    return list(map(list, strings))


if __name__ == "__main__":
    sample_list_of_strings = ["Compact", "Programming", "Course"]
    print(strings_to_lists(sample_list_of_strings))