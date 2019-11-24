def Input():
    # Part - 1 : Taking Inputs
    print("\nNetwork Optimimzation Programming Assignment #3")
    print("\nAuction Algorithm")
    n = int(input("\nNo of Persons : "))
    m = int(input("\nNo of Objects : "))
    print("\nEnter the Benefit(aij) martix Aij :")
    Aij = []
    max_a = 0
    for i in range(n):
        Aij.append([int(x) for x in input().split()])
        if max_a < max(Aij[i]):
            max_a = max(Aij[i])
        if len(Aij[i]) != m:
            print("\nError: Expected ", m, " values in a row")
            return

    # Part - 2 : Initial Assignment
    S = []                         # Starting with empty assignment
    p = [0 for i in range(m)]      # price Variable for each object
    q = [max_a for i in range(n)]  # profit variable for each person

    # print(max_a)
    Forward_Auction(Aij, S, p, q)


def Forward_Auction(Aij, S, p, q):
    # Part - 3 : Forward Auction

    # Selecting the person i to assign
    for i in range(len(q)):


def Reverse_Auction():
    # Part - 4 : Reverse Auction
    ...


Input()
