def dynamic(w, v, cap, n):
    K = [[0 for i in range(cap + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(cap + 1):
            if w[i - 1] <= j and i != 0 and j != 0:
                K[i][j] = max(v[i - 1] + K[i - 1][j - w[i - 1]], K[i - 1][j])
            elif w[i - 1] > j and i != 0 and j != 0:
                K[i][j] = K[i - 1][j]
    return K


while True:
    print("1 - Wprowadź dane z klawiatury\n2 - Wprowadź dane z pliku\n3 - Testy\n4 - Zakończ program")
    ans = input()
    if ans != '1' and ans != '2' and ans != '3' and ans != '4':
        print("Podano błędną wartość!")
        continue
    if ans == '1':
        try:
            print("Podaj liczbę przedmiotów i pojemność plecaka:")
            n = list(map(int, input().split()))
            if len(n) != 2:
                print("Podano błędne wartości!")
                continue
        except:
            print("Podano błędne wartości!")
            continue
        print("Podaj rozmiar przedmiotu oraz jego wartość:")
        p = []
        i = 0
        while n[0] > i:
            try:
                q = list(map(int, input().split()))
                if len(q) != 2:
                    print("Podano błędne wartości!")
                    continue
                i += 1
                p.append(q)
            except:
                print("Podano błędne wartości!")
        print("Algorytm programowania dynamicznego")
        w = []
        v = []
        for i in range(n[0]):
            w.append(p[i][0])
            v.append(p[i][1])
        K = dynamic(w, v, n[1], n[0])
        print("Maksymalna wartość: ", K[n[0]][n[1]])
        W = n[1]
        nk = n[0]
        wc = 0
        i = n[0]
        while nk != 0:
            if K[nk][W] != K[nk - 1][W]:
                print("Przedmiot", i, "waga:", w[nk - 1], "wartość:", v[nk - 1])
                wc = wc + w[nk - 1]
                W = W - w[nk - 1]
            i -= 1
            nk -= 1
        print("Sumaryczna waga: ", wc)

        print("Algorytm zachłanny")
        # program

        print("Algortym siłowy")
        # program
        continue
    if ans == '2':
        p_file = []
        try:
            with open("cases.txt", 'r') as f:
                i = 1
                for line in f:
                    if i == 1:
                        n = list(map(int, line.split()))
                        if len(n) != 2:
                            print("Podano błędne wartości!")
                            continue
                    else:
                        q = list(map(int, line.split()))
                        if q not in p_file:
                            p_file.append(q)
                        else:
                            print("Jedna z wartości wystepuje wielokrotnie i nie została dodana.")
                i += 1
        except:
            print("Podano błędne wartości lub taki plik nie istnieje!")
            continue
        print("Algorytm programowania dynamicznego")
        w = []
        v = []
        for i in range(n[0]):
            w.append(p_file[i][0])
            v.append(p_file[i][1])
        K = dynamic(w, v, n[1], n[0])
        print("Maksymalna wartość: ", K[n[0]][n[1]])
        W = n[1]
        nk = n[0]
        wc = 0
        i = n[0]
        while nk != 0:
            if K[nk][W] != K[nk - 1][W]:
                print("Przedmiot", i, "waga:", w[nk - 1], "wartość:", v[nk - 1])
                wc = wc + w[nk - 1]
                W = W - w[nk - 1]
            i -= 1
            nk -= 1
        print("Sumaryczna waga: ", wc)

        print("Algorytm zachłanny")
        # program
        print("Algortym siłowy")
        # program
    if ans == '3':
        print("Testy w przygotowaniu...")
    if ans == '4':
        break
