def Input():
    # Part - 1 : Taking Inputs
    print("\nNetwork Optimimzation Programming Assignment #3")
    print("\nAuction Algorithm")
    n = int(input("\nNo of Persons :"))
    m = int(input("\nNo of Objects :"))
    print("\nEnter the Benefit(aij) martix Aij :")
    Aij = []
    for i in range(n):
        Aij.append([int(x) for x in input().split()])
        if len(Aij[i]) != m:
            print("\nError: Expected ", m, " values in a row")
            break

    # Part -2 : Iniitial Assignment
    S = []
    p = [0 for i in range[m]]
    q = [0 for i in range[n]]


Input()
