import sys
from random import randint

class AVLNode():
    def __init__(self,key):
        self.key=key
        self.left_child=None
        self.right_child=None
        self.height=1

class AVL():
    def insert(self,root,key):
        if not root:
            return AVLNode(key)
        elif key<root.key:
            root.left_child = self.insert(root.left_child,key)
        else:
            root.right_child = self.insert(root.right_child,key)
        root.height=1+max(self.heightGet(root.left_child),self.heightGet(root.right_child))
        #balance factor
        balance=self.balance(root)
        if balance > 1 and key < root.left_child.val: #ll
            return self.rightR(root)
        if balance < -1 and key > root.right_child.val: #rr
            return self.leftR(root)
        if balance > 1 and key > root.left_child.val: #lr
            root.left_child=self.leftR(root.left_child)
            return self.rightR(root)
        if balance < -1 and key < root.right_child.val: #rl
            root.right_child=self.rightR(root.right_child)
            return self.leftR(root)
        return root

    def leftR(self,l): #left Rotate
        a=l.right_child
        b=a.left_child
        a.left_child=l
        l.right_child=b

        l.height = 1 + max(self.heightGet(l.left_child), self.heightGet(l.right_child))
        a.height = 1 + max(self.heightGet(a.left_child), self.heightGet(a.right_child))

        return a #new root

    def rightR(self,l): #right rotate
        a = l.left_child
        b = a.right_child
        a.left_child = l
        l.right_child = b

        l.height = 1 + max(self.heightGet(l.left_child), self.heightGet(l.right_child))
        a.height = 1 + max(self.heightGet(a.left_child), self.heightGet(a.right_child))

        return a  # new root

    def heightGet(self,root):
        if not root:
            return 0
        return root.height

    def balance(self,root):
        if not root:
            return 0
        a=self.heightGet(root.left_child)-self.heightGet(root.right_child)
        return a

    def delete(self, root, key):
        if not root:
            return root
        elif key<root.key:
            root.left_child=self.delete(root.left_child,key)
        elif key>root.key:
            root.right_child=self.delete(root.right_child,key)
        else:
            if root.left_child is None:
                a=root.right_child
                root=None
                return a
            if root.right_child is None:
                a=root.left_child
                root=None
                return a
            a=self.min_val(root.right_child)
            root.key=a.key
            root.right_child=self.delete(root.right_child,a.key)
        if root is None:
            return root

        root.height = 1 + max(self.heightGet(root.left_child), self.heightGet(root.right_child))

        balance = self.balance(root) #balancing tree
        if balance > 1 and key < root.left_child.val:  # ll
            return self.rightR(root)
        if balance < -1 and key > root.right_child.val:  # rr
            return self.leftR(root)
        if balance > 1 and key > root.left_child.val:  # lr
            root.left_child = self.leftR(root.left_child)
            return self.rightR(root)
        if balance < -1 and key < root.right_child.val:  # rl
            root.right_child = self.rightR(root.right_child)
            return self.leftR(root)
        return root

    def min_val(self,root):
        if root is None or root.left_child is None:
            return root
        return  self.min_val(root.left_child)

    def pre_order(self,root):
        if root is not None:
            print(root.key, end=" ")
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)

    def post_order(self,root,tab):
        if root is None:
            return
        self.post_order(root.left_child, tab)
        self.post_order(root.right_child, tab)
        tab.append(root.key)

    def find_min(self,root):
        temp = root
        while temp.left_child is not None:
            print(temp.key, end="->")
            temp = temp.left_child
        print(temp.key)
        return temp.key

    def find_max(self,root):
        temp = root
        while temp.right_child is not None:
            print(temp.key, end="->")
            temp = temp.right_child
        print(temp.key)
        return temp.key

    def find_and_print(self,root, key):
        if key == root.key:
            return self.pre_order(root)

        if key < root.key:
            return self.find_and_print(root.left_child, key)

        return self.find_and_print(root.right_child, key)

    def post_order_delete(self,root):
        print("\nDelete post-order")
        self.post_order(root, self.post_order_tab)
        print("Deleted values")
        for x in range(len(self.post_order_tab)):
            val = self.post_order_tab[x]
            print(val, end="->")
            self.delete(root, val)

def random_number_generator(n):
    tab = []
    for x in range(n):
        tab.append(randint(10, 10*n))
    return tab


def shell_sort(t, n):
    interval = 1
    j = 1
    while (pow(3, j) - 1) / 2 < n:
        interval = (pow(3, j) - 1) // 2
        j += 1

    while interval > 0:
        for y in range(interval, n):
            temp = t[y]
            j = y
            while j >= interval and t[j - interval] < temp:
                t[j] = t[j - interval]
                j -= interval
            t[j] = temp
        interval = (interval - 1)//3


def mid(t, l, p):
    if l < p:
        median = (l + p)//2
        print(median)
        mid(t, l, median)
        mid(t, median + 1, p)


post_order_tab = []
tree=AVL()
while True:
    root = None
    print("Menu:\n1 - Dane wejściowe\n2 - Testy\n3 - Zakończ działanie programu")
    x = input()
    if x == "1":
        print("Ile chcesz podać liczb?")
        ile_liczb = input()
        if ile_liczb.isnumeric():
            ile_liczb = int(ile_liczb)
            ile = 0
            while ile < ile_liczb:
                try:
                    number = int(input())
                    if type(number) == int:
                        root = tree.insert(root, number)
                        ile += 1
                except:
                    print("To nie jest liczba spróbuje jeszcze raz!")
            while True:
                print("Menu procedur:\n1 - Wyszukiwanie min i max\n2 - Usunięcie elementu\n3 - Wypisanie in-order"
                      "\n4 - Wypisanie pre-order\n5 - Usunięcie całego drzewa(post-order)\n6 - Wypisanie pre-order podrzewa"
                      "\n7 - Równoważenie drzewa\n8 - Powrót do menu głównego")
                try:
                    chosen = int(input())
                    if type(chosen) == int:
                        if chosen == 1:
                            print("Największa wartość : ")
                            tree.find_max(root)
                            print("Najmniejsza wartość : ")
                            tree.find_min(root)
                            print("\n")
                        if chosen == 2:
                            print("Podaj ile wartości chcesz usunąć: ")
                            value = int(input())
                            if type(value) == int:
                                for v in range(value):
                                    value_td = int(input())
                                    if type(value_td) == int:
                                        tree.delete(root, value_td)
                            print("\n")
                        if chosen == 3:
                            print("In-order")
                            tree.in_order(root)
                            print("\n")
                        if chosen == 4:
                            print("Pre-order")
                            tree.pre_order(root)
                            print("\n")
                        if chosen == 5:
                            print("Delete post-order")
                            tree.post_order_delete(root)
                            print("\n")
                        if chosen == 6:
                            print("Podaj klucz do podrzewa: ")
                            key = int(input())
                            if type(key) == int:
                                print("Find a key")
                                tree.find_and_print(root, key)
                                print(tree.find_and_print(root, key))
                                print("\n")
                        if chosen == 7:
                            print("Nie wiem o co cmon") #
                        if chosen == 8:
                            break
                except:
                    print("To chyba nie jest poprawna wartość! Spróbuj ponownie.")
        else:
            print("To nie jest liczba podaj poprawną wartość!")

    elif x == "2":
        print(x)
    elif x == "3":
        sys.exit()
    else:
        print("Podaj poprawną wartość")