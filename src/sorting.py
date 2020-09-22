
def printCurrentHand(lst, count):
    nicknames = []
    for j in range(len(lst)):
        nicknames.append(lst[j].getNickName())
    print(count, ":", nicknames)
    print('\n')

def bubbleSort(lst):
    count = 0
    printCurrentHand(lst, count)
    while True:
        swapped = False

        for k in range(len(lst) - 1):
            if lst[k].getCardValue() > lst[k+1].getCardValue():
                lst[k], lst[k+1] = lst[k+1], lst[k]
                count += 1
                printCurrentHand(lst, count)
                swapped = True

        if not swapped:
            break


def insertionSort(lst):
    count = 0
    printCurrentHand(lst, count)
    for i in range(1, len(lst)):
        cur = lst[i]
        k = i - 1
        while k >= 0 and lst[k].getCardValue() > cur.getCardValue():
            lst[k+1] = lst[k]
            count += 1
            printCurrentHand(lst, count)
            k -= 1

        lst[k+1] = cur
