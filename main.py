def numar_prim(numar):
    """
    Determina daca un numar este prim.
    :param numar: un numar natural
    :return: True daca numarul este prim sau False in caz contrar
    """
    if numar < 2:
        return False
    for divizor in range(2, numar // 2 + 1):
        if numar % divizor == 0:
            return False
    return True


def eliminare_nr_prime(lst):
    """
    Elimina elementele prime din lista.
    :param lst: o lista de numere intregi
    :return: lista dupa eliminarea numerelor prime
    """
    rezultat = []
    for numar in lst:
        if numar_prim(numar) is False:
            rezultat.append(numar)
    return rezultat


def media_aritmetica_n(lst, n):
    """
    Verifica daca media aritmetica a numerelor din lista este mai mare sau egala ca un numar dat.
    :param lst:o lista de numere intregi
    :param n:un numar natural citit de la tastatura
    :return:True daca media aritmetica a numerelor este mai mare sau egala ca n sau False in caz contrar
    """
    suma = 0
    numarul_elementelor = len(lst)
    for numar in lst:
        suma = suma + numar
    media = suma / numarul_elementelor
    if n <= media:
        return True
    return False


def numar_divizori_proprii(numar):
    """
    Determina numarul de divizori proprii ai unui numar.
    :param numar: un numar natural
    :return: numarul de divizori proprii ai numarului dat
    """
    numar_divizori = 0
    for divizor in range(2, numar - 1):
        if numar % divizor == 0:
            numar_divizori = numar_divizori + 1
    return numar_divizori


def lista_cu_nr_divizori(lst):
    """
    Adauga numarul de divizori proprii dupa fiecare element.
    :param lst: o lista de numere inttregi
    :return: lista de numere intregi avand divizorii proprii dupa fiecare element
    """
    rezultat = []
    for x in lst:
        rezultat.append(x)
        numar_divizori = numar_divizori_proprii(x)
        rezultat.append(numar_divizori)
    return rezultat


def numar_aparitii(lst, x):
    """
    Determina numarul de aparitii al unui element din lista
    :param lst: o lista de numere intregi
    :param x: un numar intreg
    :return: numarul de aparitii al unui numar din lista
    """
    aparitii = 0
    for numar in lst:
        if numar == x:
            aparitii = aparitii + 1
    return aparitii


def tuplu_numar_index_aparitii(lst):
    """
    Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care peprima/
          " poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia/"
          "poziție apare numărul de apariții a numărului."
    :param lst: o lista de numere intregi
    :return: o liste de tuple in care se regaseste numarul, indexul si numarul de aparitii
    """
    rezultat = []
    for i in range(len(lst)):
        aparitii = numar_aparitii(lst, lst[i])
        tuplu = (lst[i], i, aparitii)
        rezultat.append(tuplu)
    return rezultat


def citire_lista():
    rezultat = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        numar = int(input("lst[" + str(i) + "]= "))
        rezultat.append(numar)
    return rezultat


def afisare_meniu():
    print("1.Citirea listei.")
    print("2.Afișarea listei după eliminarea numerelor prime din listă")
    print("3.Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
    print("4.Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
    print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care peprima/"
          " poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia/"
          "poziție apare numărul de apariții a numărului.")
    print("x.Iesire")


def test_eliminare_nr_prime():
    assert eliminare_nr_prime([21, 2, 1]) == [21, 1]
    assert eliminare_nr_prime([8, 19, 17, 25]) == [8, 25]
    assert eliminare_nr_prime([0, 1, 4]) == [0, 1, 4]


def test_media_aritmetica_n():
    assert media_aritmetica_n([2, 3, 4], 3) is True
    assert media_aritmetica_n([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert media_aritmetica_n([1, 1, 4], 10) is False


def test_numar_divizori_proprii():
    assert lista_cu_nr_divizori([4, 5]) == [4, 1, 5, 0]
    assert lista_cu_nr_divizori([2, 6]) == [2, 0, 6, 2]
    assert lista_cu_nr_divizori([1]) == [1, 0]


def test_tuplu_numar_index_aparitii():
    assert tuplu_numar_index_aparitii([1, 2, 1, 3]) == [(1, 0, 2), (2, 1, 1), (1, 2, 2), (3, 3, 1)]
    assert tuplu_numar_index_aparitii([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert tuplu_numar_index_aparitii([2, 1]) == [(2, 0, 1), (1, 1, 1)]


def main():
    lst = []
    while True:
        afisare_meniu()
        optiune = input("Alegeti optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(eliminare_nr_prime(lst))
        elif optiune == "3":
            n = int(input("Dati n= "))
            if media_aritmetica_n(lst, n):
                print("DA")
            else:
                print("NU")
        elif optiune == "4":
            print(lista_cu_nr_divizori(lst))
        elif optiune == "5":
            print(tuplu_numar_index_aparitii(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida!")


test_eliminare_nr_prime()
test_media_aritmetica_n()
test_numar_divizori_proprii()
test_tuplu_numar_index_aparitii()
main()
