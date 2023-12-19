def bubble_sort(l):
    laenge = len(l)

    for i in range(0, laenge - 1):
        for j in range(0, laenge - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    print(l)

liste = [6, 4, 10, 2, 5]

bubble_sort(liste)