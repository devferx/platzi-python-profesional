class EvenNumbers:
    def __init__(self, max=None):
        self.max = max
        self.num = 0

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


def main():
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    # print(next(my_iter))
    # print(next(my_iter))

    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break

    iterador = EvenNumbers(100)
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))


if __name__ == "__main__":
    main()
