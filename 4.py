#!/usr/bin/python

def menor_custo(s, cc):

    if s == 0:
        return s

    elif cc > s:
        return s

    else:

        sum = 0
        setor = 1
        cont = 1

        for i in range(cc):
            sum = sum + setor
            cont = cont + 1

        setor = setor + 1

        while cont <= s:
            sum = sum + setor
            cont = cont + 1
            setor = setor + 1

        return sum


def teste():
    try:

        assert menor_custo(5, 10) == 5, 'Error caso 1'
        assert menor_custo(6, 5) == 7, 'Error caso 2'
        assert menor_custo(5000, 2) == 12497501, 'Error caso 3'
        assert menor_custo(0, 5000) == 0, 'Error caso 4'
        assert menor_custo(144, 8) == 9460, 'Error caso 5'
        assert menor_custo(5000, 4000) == 505500, 'Error caso 6'

        return True

    except AssertionError as error:
        return error

    except Exception as exception:
        return exception


def main():
    #print(teste())
    entrada = input()
    s, cc = entrada.split(' ')
    s = int(s)
    cc = int(cc)
    print(menor_custo(s, cc))


if __name__ == "__main__":
    main()
