def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome("ana"))
    print(is_palindrome("facundo"))
    print(is_palindrome(10))


if __name__ == "__main__":
    run()
