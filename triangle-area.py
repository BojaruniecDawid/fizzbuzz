wysokosc = input('Podaj wysokosc trojkata: ')

podstawa = input('Podaj dlugosc podstawy trojkata:')

podstawa, wysokosc = float(podstawa), float(wysokosc)

pole = podstawa*wysokosc*0.5
if podstawa < 0 and wysokosc < 0:
    print('Liczba musi być wieksza od zera')
if podstawa > 0 and wysokosc > 0:
    print(pole)







