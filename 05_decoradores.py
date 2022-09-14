def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original")
        func()

    return envoltura


@decorador
def saludo():
    print("¡Hola!")


def mayusculas(func):
    def envoltura(texto: str):
        return func(texto).upper()

    return envoltura


@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"


def main():
    saludo()
    print(mensaje("Cesar"))


if __name__ == "__main__":
    main()
