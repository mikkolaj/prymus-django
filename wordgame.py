import random


def game(slowko):
    licz = 0
    obecny = ["_"]*len(slowko)
    while True:
        if licz >= 3:
            print("Przegrałeś :( slowko to:", slowko)
            return
        print("Pozostało", 3-licz, "szans")
        for i in obecny:
            print(i, end=" ")
        print("")
        znak = input("Podaj literkę: ")
        zgadl = False

        for i in range(len(slowka[index])):
            if znak == slowko[i] and znak != obecny[i]:
                if zgadl is False:
                    print("Zgadłeś literkę!")
                zgadl = True
                obecny[i] = znak

        if zgadl is False:
            licz += 1

        if "_" not in obecny:
            for i in obecny:
                print(i, end=" ")
            print("")
            print("Wygrałeś!")
            return


f = open("slowa.txt", "r")
slowka = f.readlines()
for i in range(len(slowka)):
    slowka[i] = slowka[i].strip("\n").lower()
print("Zgaduj literki w słowie")
index = random.randint(0, len(slowka)-1)
game(slowka[index])


