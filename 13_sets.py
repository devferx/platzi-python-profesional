import random


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicatesv2(some_list):
    return list(set(some_list))


def main():
    # [1,1,2,2,4] -> [1,2,4]
    random_list = [random.randint(0, 20) for _ in range(20)]
    print(random_list)
    print(remove_duplicates(random_list))
    print(remove_duplicatesv2(random_list))


if __name__ == "__main__":
    main()
