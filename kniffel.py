#! python3

import random as rd
import copy
import tabulate


def clear():
    print ("\n" * 50)

def roll(old):
    for i in range(5 - len(old)):
        x = rd.randint(1, 6)
        old.append(x)
    show(old)
    return old


def show(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    num = ", ".join(numbers)
    print("Your current numbers are: " + num + "\n")


def choose(allnumbers):
    print("\nEnter the numbers you want to keep.\n"
    "If you want to keep every number type 'all'.\n"
    "If you don't want to keep any additional numbers press 'Enter' without a value."
    )
    stays = []
    q = 0
    keep = input()
    if keep == "":
        q = 2
    elif keep.lower() == "all":
        stays = allnumbers
        q = 1
    else:
        while True:
            try:
                int(keep)
                break
            except:
                print("Only choose integer values!")
                keep = input()
        keep = list(keep)
        for i in keep:
            if i in allnumbers:
                if allnumbers.count(i) > stays.count(i):            #hier fehlt noch Fehlererkennung
                    stays.append(int(i))
                else:
                    print("You can't take those values.")
            else:
                print("You can only take numbers you already rolled.\n")
    if q == 0:
        show(stays)
    return stays, q


def turn(name):
    allrolls = []
    clear()
    for i in range(3):
        if i == 0:
            print("\nIt's your turn " + name + ".")
        elif i == 2:
            print("It's your last turn " + name + ".")
        else:
            print("It's your next turn " + name + ".")
        input("Press 'Enter' to roll!\n")
        allrolls = roll(allrolls)
        if i < 2:
            allrolls, q = choose(allrolls)
        if q == 1:
            break

    print("\nThose are " + name + "'s final numbers:")
    for i in range(len(allrolls)):
        allrolls[i] = str(allrolls[i])
    num = ", ".join(allrolls)
    print(num + "\n")
    return allrolls


def points(a, thisdict):
    print("Choose between the following options by typing its name:\n")
    for i in thisdict.keys():
        print(i)

    while True:
        breaker = 0
        take = input()
        take = take.lower()

        while True:                                     #Testet ob input-Wert im dict zur Verfügung steht
            try:
                thisdict[take]
                break
            except:
                print("This is not an option.")
                take = input()

        if thisdict[take] == False:

            for z in range(5):
                a[z] = int(a[z])

            if take == "1er":
                c = a.count(1)
                thisdict["1er"] = c * 1

            elif take == "2er":
                c = a.count(2)
                thisdict["2er"] = c * 2

            elif take == "3er":
                c = a.count(3)
                thisdict["3er"] = c * 3

            elif take == "4er":
                c = a.count(4)
                thisdict["4er"] = c * 4

            elif take == "5er":
                c = a.count(5)
                thisdict["5er"] = c * 5

            elif take == "6er":
                c = a.count(6)
                thisdict["6er"] = c * 6

            elif take == "dreierpasch":
                for i in range(3):
                    c = a.count(a[i])
                    if c >= 3:
                        thisdict["dreierpasch"] = sum(a)
                    else:
                        thisdict["dreierpasch"] = 0

            elif take == "viererpasch":
                for i in range(2):
                    c = a.count(a[i])
                    if c >= 4:
                        thisdict["viererpasch"] = sum(a)
                    else:
                        thisdict["viererpasch"] = 0

            elif take == "fullhouse":
                b = a[0]
                if a.count(b) == 3:
                    for i in range(3):
                        a.remove(b)
                    c = a[0]
                    for i in range(a.count(c)):
                        a.remove(c)
                elif a.count(b) == 2:
                    for i in range(2):
                        a.remove(b)
                    c = a[0]
                    for i in range(a.count(c)):
                        a.remove(c)
                if a == []:
                    thisdict["fullhouse"] = 25
                else:
                    thisdict["fullhouse"] = 0

            elif take == "klstraße":
                a.sort()
                a = list(dict.fromkeys(a))
                if a == [1, 2, 3, 4] or a == [2, 3, 4, 5] or a == [3, 4, 5, 6] or a == [1, 2, 3, 4, 5] or a == [2, 3, 4, 5, 6]:
                    thisdict["klstraße"] = 30
                else:
                    thisdict["klstraße"] = 0

            elif take == "grstraße":
                a.sort()
                if a == [1, 2, 3, 4, 5] or a == [2, 3, 4, 5, 6]:
                    thisdict["grstraße"] = 40
                else:
                    thisdict["grstraße"] = 0

            elif take == "kniffel":
                c = a.count(a[0])
                if c >= 5:
                    thisdict["kniffel"] = 50
                else:
                    thisdict["kniffel"] = 0

            elif take == "chance":
                thisdict["chance"] = sum(a)

            else:
                breaker = 1
                print("You have to take one option.")

            if breaker == 0:
                break

        else:
            print("You already chose this option.")

    return thisdict



def countpoints(allpoints):
    values = allpoints.values()
    if (allpoints["1er"] + allpoints["2er"] + allpoints["3er"] + allpoints["4er"] + allpoints["5er"] + allpoints["6er"]) >= 63:
        return (sum(values) + 25)
    else:
        return sum(values)


onelist = {
  "1er": False,
  "2er": False,
  "3er": False,
  "4er": False,
  "5er": False,
  "6er": False,
  "dreierpasch": False,
  "viererpasch": False,
  "fullhouse": False,
  "klstraße": False,
  "grstraße": False,
  "kniffel": False,
  "chance": False}



### Here begins the game


while True:
    players = input("Choose the number of players:\n")
    while True:
        try:
            players = int(players)
            break
        except:
            print("Only use positive integers.")
            players = input("Choose the number of players:\n")

    rounds = input("Choose the number of rounds: (13 are a full game)\n")
    while True:
        try:
            rounds = int(rounds)
            break
        except:
            print("Only use positive integers.")
            rounds = input("Choose the number of rounds: (13 are a full game)\n")

    kniffelllist = []
    namelist = []
    endlist = []

    for i in range(players):
        name = input("Enter name of Player " + str(i + 1) + "\n")
        namelist.append(name)



    for i in range(players):
        kniffelllist.append(copy.deepcopy(onelist))



    for i in range(rounds):
        for j in range(players):
            m = turn(namelist[j])
            kniffelllist[j] = points(m, kniffelllist[j])

    for i in range(players):
        b = [countpoints(kniffelllist[i]), namelist[i]]
        endlist.append(b)

    endlist.sort(reverse=True)
    for i in range(players):
        endlist[i].insert(0, str(i + 1))


    clear()


    headers = ["Rank", "Points", "Player"]

    print("Here are the final results:\n")
    print(tabulate.tabulate(endlist, headers=headers, tablefmt="psql", colalign=("right", "right", "right")))


    again = input("Do you want to play again? (yes or no)\n")
    if again != "yes":
        break
    else:
        clear()




"""
To-dos:
- jedes Würfelfeld darf im Spiel nur einmal gewählt werden. X
- zu beginn muss die Anzahl der Spieler gewählt werden können X
- es wird jedem Spieler ein Name gegeben X
- Während der Runden wird der Name genannt X
- Für Siegerehrung werden alle Plätze, Punkte una Namen angezeigt X
- count muss um Bonuspunkte erweitert werden X
- wenn feld gestrichen darf es später nicht nochmal verwendet werden X

optional:
- eine Anzeige wie die Punkte je nach Wüfelfeld verteilt werden
- Anzeige wie viele Punkte schon auf den Würfelfeldern liegen
- beide Anzeigen zu einer Tabelle kombinieren, die bei points angezeigt wird
- verwende listen innerhalb des dict, um die zusätzliche namensliste zu erübrigen
- Mögllichkeiten alle Würfel zu behalten X
- Möglichkeit alle zu behaltenden Würfel in eine Zeile einzugeben X
- Ergebnisse werden automatisch in csv datei gespeichert
- Wieso zum Fick werden die int in meinen list immer wieder zu str
(Problem tritt bei points auf)
- viel Bugs suchen

"""
