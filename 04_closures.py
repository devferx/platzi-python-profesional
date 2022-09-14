def make_repearter_of(n: int):
    def repeater(string: str):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n

    return repeater


def make_division_by(n):
    def div(n2):
        return n2 / n

    return div


def run():
    repeat_5 = make_repearter_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repearter_of(10)
    print(repeat_10("Platzi"))
    # ---
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()
