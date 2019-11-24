import numpy as np


def Input(Aij):
    # Part - 1 : Taking Inputs
    print("\nNetwork Optimimzation Programming Assignment #3")
    print("\nAuction Algorithm")
    max_a = 0
    if(Aij == []):  # Manual Input
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
        n = len(Aij[0])
        m = len(Aij)
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
        Ji.remove(max(Ji))
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
        print("\nCurrent Assignment: ", S)

        # Selecting the person i to assign
        assigned = []  # list to  keep track of persons that are assigned
        for i in range(len(S)):
            assigned.append(S[i][0])
        if len(assigned) == len(q):
            if len(p) == len(q):
                print("\nFinal Assignment for the Symmetric Problem is-")
                print(S)
            return
        unass = [person for person in [i+1 for i in range(len(q))] if person not in assigned]


# Input([])
Input([[8, 2, 10, 16], [10, 8, 12, 13], [17, 5, 11, 9], [9, 6, 9, 7]])
# Input([[8, 7, 6, 5], [5, 8, 7, 6], [6, 7, 5, 8], [7, 5, 8, 6]])
