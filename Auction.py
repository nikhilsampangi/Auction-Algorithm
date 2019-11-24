import numpy as np


def Input(Aij):
    # Part - 1 : Taking Inputs
    print("\nNetwork Optimimzation Programming Assignment #3")
    print("\nAuction Algorithm")
    max_a = 0
    if(Aij == []):  # For Manual Input
        n = int(input("\nNo of Persons : "))
        m = int(input("\nNo of Objects : "))
        print("\nEnter the Benefit(aij) martix Aij :")
        Aij = []
        for i in range(n):
            Aij.append([int(x) for x in input().split()])
            if max_a < max(Aij[i]):
                max_a = max(Aij[i])
            if len(Aij[i]) != m:
                print("\nError: Expected ", m, " values in a row")
                return
    else:
        print("\nGiven Input -\n")
        for lines in Aij:
            print(lines)
        # print(\n)
        m = len(Aij[0])
        n = len(Aij)
        for i in range(n):
            if max_a < max(Aij[i]):
                max_a = max(Aij[i])

    # Part - 2 : Initial Assignment
    S = []                         # Starting with empty assignment
    p = [0 for i in range(m)]      # price Variable for each object
    q = [max_a for i in range(n)]  # profit variable for each person

    # print(max_a)
    Forward_Auction(Aij, S, p, q)


def Forward_Auction(Aij, S, p, q):
    # Part - 3 : Forward Auction
    # taking epsilon as 1/n
    e = 1/len(q)
    unass = [i+1 for i in range(len(q))]
    # Forward Auction Algorithm
    while(unass != []):
        Pi = unass.pop()
        # finding the best j
        Ji = []
        for j in range(len(p)):
            Ji.append((Aij[Pi-1][j] - p[j]))
        j = np.argmax(Ji)
        v = Ji[j]
        Ji.remove(v)
        w = max(Ji)
        bid = p[j]+v-w+e
        # updating p's and q's
        p[j] = bid
        q[Pi-1] = Aij[Pi-1][j]-p[j]
        for i in range(len(S)):
            if (S[i][1])-1 == j:
                S.remove(S[i])
                break
        S.append([Pi, j+1])
        # print("\nCurrent Assignment: ", S)

        # Selecting the person i to assign
        assigned = []  # list to  keep track of persons that are assigned
        for i in range(len(S)):
            assigned.append(S[i][0])
        if len(assigned) == len(q):
            if len(p) == len(q):
                print("\nFinal Assignment for the Symmetric Problem is-")
                print(S)
            else:
                Reverse_Auction(Aij, S, p, q)
            return
        unass = [person for person in [i+1 for i in range(len(q))] if person not in assigned]


def Reverse_Auction(Aij, S, p, q):
    # Part - 4 : Reverse Auction
    # taking epsilon as 1/n
    e = 1/len(q)
    # finding the objects that are unassigned and with pj greater than lamda
    obj_a = []
    for i in range(len(S)):
        obj_a.append(S[i][1])
    # list of unassigned objects
    obj_una = [obj for obj in [i+1 for i in range(len(p))] if obj not in obj_a]
    # unassigned objects with pj greater than lamda

    # for lamda value
    l = []
    for i in range(len(obj_a)):
        l.append(p[obj_a[i]-1])
    lamda = min(l)

    for i in range(len(obj_una)):
        if p[obj_una[i]-1] <= lamda:
            obj_una.remove(obj_una[i])
    if len(obj_una) != 0:
        while(obj_una != []):
            obj = obj_una.pop()
            # Finding the best person i
            Ij = []
            for i in range(len(q)):
                Ij.append(Aij[i][obj-1] - q[i])
            i = np.argmax(Ij)
            v2 = Ij[i]
            Ij.remove(v2)
            w2 = max(Ij)

            if lamda >= v2-e:
                p[obj-1] = lamda
            else:
                delta = min([v2-lamda, v2-w2+e])
                p[obj-1] = v2 - delta
            q[i] = Aij[i][obj-1]-p[obj-1]

            for j in range(len(S)):
                if(S[j][0])-1 == i:
                    S.remove(S[j])
                    break
            S.append([i+1, obj])
    elif len(obj_una) == 0:
        print("\nFinal Assignment for the Asymmetric Problem is-")
        print(S)
        return


# Manual Input
# Input([])
#
# Symmetric Examples
# Input([[8, 7, 6, 5], [5, 8, 7, 6], [6, 7, 5, 8], [7, 5, 8, 6]])
# Input([[8, 2, 10, 16], [10, 8, 12, 13], [17, 5, 11, 9], [9, 6, 9, 7]])
#
# Asymmetric Examples
# Input([[8, 2, 10, 16, 1], [10, 8, 12, 13, 1], [17, 5, 11, 9, 1], [9, 6, 9, 7, 1]])
Input([[8, 2, 10, 16, 14], [10, 8, 12, 13, 14], [17, 5, 11, 9, 15], [9, 6, 9, 7, 10]])
