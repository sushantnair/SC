import matplotlib.pyplot as plt
def fuzzy_union(aa, ba, ca, da, ab, bb, cb, db):
    A = {"a": aa, "b": ba, "c": ca, "d": da}
    B = {"a": ab, "b": bb, "c": cb, "d": db}
    Y = {}
    print('Fuzzy Set A is', A)
    print('Fuzzy Set B is', B)
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        if A_value > B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print('Fuzzy Set Union is Y', Y)
    visualize(Y, op="Union")

def fuzzy_intersection(aa, ba, ca, da, ab, bb, cb, db):
    A = {"a": aa, "b": ba, "c": ca, "d": da}
    B = {"a": ab, "b": bb, "c": cb, "d": db}
    Y = {}
    print('Fuzzy Set A is', A)
    print('Fuzzy Set B is', B)
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        if A_value < B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print('Fuzzy Set Intersection is Y', Y)
    visualize(Y, op="Intersection")

def fuzzy_compliment(aa, ba, ca, da):
    A = {"a": aa, "b": ba, "c": ca, "d": da}
    Y = {}
    print('Fuzzy Set A is', A)
    for A_key in A:
        Y[A_key] = 1 - A[A_key]
    print('Fuzzy Set Compliment is Y', Y)
    visualize(Y, op="Compliment")

def fuzzy_difference(aa, ba, ca, da, ab, bb, cb, db):
    A = {"a": aa, "b": ba, "c": ca, "d": da}
    B = {"a": ab, "b": bb, "c": cb, "d": db}
    Y = {}
    print('Fuzzy Set A is', A)
    print('Fuzzy Set B is', B)
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        B_value = 1 - B_value
        if A_value < B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print('Fuzzy Set Difference is Y', Y)
    visualize(Y, op = "Difference")
        

def visualize(Y, op):
    plt.bar(Y.keys(), Y.values())
    plt.xlabel('Elements')
    plt.ylabel('Degree of Membership')
    plt.title(f'Fuzzy Set {op}')
    plt.show()

def main():
    while(True):
        print('Enter 1 for Default Values\nOtherwise, enter any character')
        ch_in = input('Enter your choice: ')
        if ch_in == '1':
            aa = 0.2
            ba = 0.3
            ca = 0.6
            da = 0.6
            ab = 0.9
            bb = 0.9
            cb = 0.4
            db = 0.5
        else:
            aa = float(input('Enter value for key \'a\' of Fuzzy Set A: '))
            ba = float(input('Enter value for key \'b\' of Fuzzy Set A: '))
            ca = float(input('Enter value for key \'c\' of Fuzzy Set A: '))
            da = float(input('Enter value for key \'d\' of Fuzzy Set A: '))
            ab = float(input('Enter value for key \'a\' of Fuzzy Set B: '))
            bb = float(input('Enter value for key \'b\' of Fuzzy Set B: '))
            cb = float(input('Enter value for key \'c\' of Fuzzy Set B: '))
            db = float(input('Enter value for key \'d\' of Fuzzy Set B: '))
        print('Enter:\n0 for all Fuzzy Operations')
        print('1 for Fuzzy Set Union')
        print('2 for Fuzzy Set Intersection')
        print('3 for Fuzzy Set Compliment')
        print('4 for Fuzzy Set Difference')
        ch_op = int(input('Enter choice: '))
        if ch_op == 0:
            fuzzy_union(aa, ba, ca, da, ab, bb, cb, db)
            fuzzy_intersection(aa, ba, ca, da, ab, bb, cb, db)
            fuzzy_compliment(aa, ba, ca, da)
            fuzzy_difference(aa, ba, ca, da, ab, bb, cb, db)
        elif ch_op == 1:
            fuzzy_union(aa, ba, ca, da, ab, bb, cb, db)
        elif ch_op == 2:
            fuzzy_intersection(aa, ba, ca, da, ab, bb, cb, db)
        elif ch_op == 3:
            fuzzy_compliment(aa, ba, ca, da)
        elif ch_op == 4:
            fuzzy_difference(aa, ba, ca, da, ab, bb, cb, db)
        else:
            print('Please enter correct choice of operation and try again.')
        print('Press any character to run the program again.')
        print('Otherwise, hit enter key.')
        ch_cont = input('Enter your choice: ')
        if len(ch_cont) < 1:
            break

if __name__ == "__main__":
    main()    