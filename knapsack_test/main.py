from random import random, randint
import math
import time




def dynamic(w, v, cap, n):
    K = [[0 for i in range(cap + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(cap + 1):
            if w[i - 1] <= j != 0 and i != 0:
                K[i][j] = max(v[i - 1] + K[i - 1][j - w[i - 1]], K[i - 1][j])
            elif w[i - 1] > j != 0 and i != 0:
                K[i][j] = K[i - 1][j]
    return K


def kanpsackAZ(t, b, n):
    t.sort(key=lambda x: x[3], reverse=True)
    size = 0
    value = 0
    i = 0
    chosen = [0] * n
    el = []
    while size <= b:
        if i == n:
            break
        if size + t[i][1] <= b:
            size += t[i][1]
            value += t[i][2]
            chosen[t[i][0]] = 1
            el.append(t[i][0] + 1)
        i += 1
    return el, chosen, size, value


def knapsackBf(b, n, t):
    fmax = 0
    size = 0
    bn = []
    chosen = []
    for x in range(1, pow(2, n)):
        binary = list([int(y) for y in bin(x)[2:].zfill(n)])
        local = 0
        lsize = 0
        lchosen = []
        f = 0
        for y in range(n - 1, -1, -1):
            if binary[y]:
                if lsize + t[f][1] <= b:
                    local += t[f][2]
                    lsize += t[f][1]
                    lchosen.append(t[f][0] + 1)
            f += 1
        if local > fmax and lsize <= b:
            fmax = local
            size = lsize
            chosen = lchosen
            bn = binary
    return fmax, size, chosen, bn


def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))


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
        t = []
        t1 = []
        i = 0
        while n[0] > i:
            try:
                q = list(map(int, input().split()))
                if len(q) != 2:
                    print("Podano błędne wartości!")
                    continue
                p.append(q)
                t.append([i, q[0], q[1], q[1] / q[0]])
                t1.append([i, q[0], q[1]])
                i += 1
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

        print("\nAlgorytm zachłanny")
        elm, elementy, rozmiar, wartosc = kanpsackAZ(t, n[1], n[0])
        print(f"Rozmiar sumaryczny : {rozmiar}\nWartość symaryczna: {wartosc}")
        for x in range(len(elm)):
            print("Przedmiot", t[x][0] + 1, "waga:", t[x][1], "wartość:", t[x][2])

        print("\nAlgortym siłowy")
        fmax, size, elements, bn = knapsackBf(n[1], n[0], t1)
        print(f"Rozmiar sumaryczny : {size}\nWartość symarycznać : {fmax}")
        for x in elements:
            print("Przedmiot", t1[x - 1][0] + 1, "waga:", t1[x - 1][1], "wartość:", t1[x - 1][2])
        print("\n")
        continue
    if ans == '2':
        p_file = []
        t_file = []
        t1_file = []
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
                            t_file.append([i - 2, q[0], q[1], q[1] / q[0]])
                            t1_file.append([i - 2, q[0], q[1]])
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
        print("Wartość sumaryczna: ", K[n[0]][n[1]])
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
        print("Rozmiar sumaryczny: ", wc)

        print("\nAlgorytm zachłanny")
        elm, elementy, rozmiar, wartosc = kanpsackAZ(t_file, n[1], n[0])
        print(f"Rozmiar sumaryczny : {rozmiar}\nWartość symaryczna: {wartosc}")
        for x in range(len(elm)):
            print("Przedmiot", t_file[x][0] + 1, "waga:", t_file[x][1], "wartość:", t_file[x][2])

        print("\nAlgortym siłowy")
        fmax, size, elements, bn = knapsackBf(n[1], n[0], t1_file)
        print(f"Rozmiar sumaryczny : {size}\nWartość symaryczna : {fmax}")
        for x in elements:
            print("Przedmiot", t1_file[x - 1][0] + 1, "waga:", t1_file[x - 1][1], "wartość:", t1_file[x - 1][2])

        print("\n")
    n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000] # ilość elementów
    # n = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44]
    #n = [10000]
    n2 = [28]
    #cap2 = [150, 300, 450, 600, 750, 900, 1050, 1200, 1350, 1500]
    cap2 = [1000]
    cap = [1500, 3000, 4500, 6000, 7500, 9000, 10500, 12000, 13500, 15000]
    if ans == '3':
        for h in n:
            for i in cap2:
                print(f"Wartość: {i}", end=" ")
                tab_AD = []
                avg_AD = 0
                tab_AZ = []
                avg_AZ = 0
                tab_AB = []
                avg_AB = 0
                print(f"etap", end=" ")
                for j in range(1, 11):
                    print(j, end=" ")
                    p = []
                    t = []
                    t1val = []  # ogólnie generator liczb
                    t1wt = []
                    for x in range(h):  # zmianan i na n
                        r = randint(1, 150)  # rozmiar przedmiotu
                        wartosc = randint(1, 250)  # wartość przedmiotu
                        p.append([r, wartosc])
                        t.append([x, r, wartosc, wartosc / r])  # index | rozmiar | wartość |     wartość/rozmiar
                        t1val.append(wartosc)  # index | rozmiar | wartość
                        t1wt.append(r)

                    w = []
                    v = []
                    for j in range(h):
                        w.append(p[j][0])
                        v.append(p[j][1])

                    '''time_AD = time.time()
                    K = dynamic(w, v, i, h)
                    end_AD = time.time() - time_AD
                    tab_AD.append(end_AD)
                    avg_AD += end_AD'''

                    time_AZ = time.time()
                    elm, elementy, rozmiar, wartosc = kanpsackAZ(t, i, h)
                    end_AZ = time.time() - time_AZ
                    tab_AZ.append(end_AZ)
                    avg_AZ += end_AZ

                    # time_AB = time.time()
                    # # fmax, size, elements, bn = knapsackBf(cap, i, t1)
                    # knapSack(i,t1wt, t1val, n) # pojemność | waga | wartosc | ilosc przedmiotów
                    # end_AB = time.time() - time_AB
                    # tab_AB.append(end_AB)
                    # avg_AB += end_AB

                # Odchylenie
                #avg_AD = avg_AD / 10
                avg_AZ = avg_AZ / 10
                # avg_AB = avg_AB/10
                #os_AD = 0
                os_AZ = 0
                # os_AB = 0
                for k in range(10):
                    #os_AD += (tab_AD[k] - avg_AD) * (tab_AD[k] - avg_AD)
                    os_AZ += (tab_AZ[k] - avg_AZ) * (tab_AZ[k] - avg_AZ)
                    # os_AB += (tab_AB[k] - avg_AB) * (tab_AB[k] - avg_AB)
                #os_AD = math.sqrt(os_AD / 10)
                os_AZ = math.sqrt(os_AZ / 10)
                # os_AB = math.sqrt(os_AB/10)


                #with open('AD.txt', 'a') as f:
                #    form = "{}\t{}\t{}\n".format(i, avg_AD, os_AD)
                #    f.write(form)

                with open('AZ.txt', 'a') as f:
                    form = "{}\t{}\t{}\n".format(i, avg_AZ, os_AZ)
                    f.write(form)

                # with open('AB.txt', 'a') as f:
                #     form = "{}\t{}\t{}\n".format(i, avg_AB, os_AB)
                #     f.write(form)
                print("\n")
        '''for h in n2:
            print(f"Wartość: {h}")
            for i in cap2:
                #print(f"Wartość: {i}", end=" ")
                tab_AB = []
                avg_AB = 0
                print(f"etap", end=" ")
                for j in range(1, 11):
                    print(j, end=" ")
                    p = []
                    t = []
                    t1val = []  # ogólnie generator liczb
                    t1wt = []
                    for x in range(h):  # zmianan i na n
                        r = randint(1, 150)  # rozmiar przedmiotu
                        wartosc = randint(1, 250)  # wartość przedmiotu
                        p.append([r, wartosc])
                        t.append([x, r, wartosc, wartosc / r])  # index | rozmiar | wartość |     wartość/rozmiar
                        t1val.append(wartosc)  # index | rozmiar | wartość
                        t1wt.append(r)


                    time_AB = time.time()
                    # fmax, size, elements, bn = knapsackBf(cap, i, t1)
                    knapSack(i,t1wt, t1val, h) # pojemność | waga | wartosc | ilosc przedmiotów
                    end_AB = time.time() - time_AB
                    tab_AB.append(end_AB)
                    avg_AB += end_AB

                # Odchylenie
                avg_AB = avg_AB/10
                os_AB = 0
                for k in range(10):
                    os_AB += (tab_AB[k] - avg_AB) * (tab_AB[k] - avg_AB)
                os_AB = math.sqrt(os_AB/10)

                with open('AB.txt', 'a') as f:
                    form = "{}\t{}\t{}\n".format(i, avg_AB, os_AB)
                    f.write(form)
                print("\n")'''
    if ans == '4':
        break
