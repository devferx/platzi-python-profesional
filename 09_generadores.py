def my_gen():
    print("Hello World!")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n


def main():
    a = my_gen()

    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a))  # StopIteration

    my_list = [0, 1, 2, 3, 4, 10]

    my_second_list = [x * 2 for x in my_list]
    my_second_gen = (x * 2 for x in my_list)

    print(next(my_second_gen))
    print(next(my_second_gen))
    print(next(my_second_gen))
    print(next(my_second_gen))


if __name__ == "__main__":
    main()
