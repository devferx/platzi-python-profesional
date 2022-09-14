from ast import main


def main():
    my_set1 = {3, 4, 5}
    my_set2 = {5, 6, 7}

    # Union
    my_set3 = my_set1 | my_set2
    print(my_set3)
    # Interseccion
    my_set4 = my_set1 & my_set2
    print(my_set4)
    # Diferencia
    my_set5 = my_set1 - my_set2
    print(my_set5)
    my_set6 = my_set2 - my_set1
    print(my_set6)
    # Diferencia simetrica
    my_set7 = my_set1 ^ my_set2
    print(my_set7)


if __name__ == "__main__":
    main()
