import numpy as np
def sgn(num):
    if num >= 0:
        return 1
    else:
        return -1
def netcalculator(w, c, x, i):
    w_transpose = w.T
    print(f'The transpose of w{i} is', w_transpose)
    net = np.dot(w_transpose, x)
    print(f'Net{i} is {net[0][0]:.3f}')
    w_return = w + sgn(net[0][0]) * x
    print(f'w{i+1} is', w_return)
    return w_return
def print_weights(w):
    print('\nLearning completed! The final weights by Hebbian Learning Rule are ', end = '')
    element_no = 1
    for element in w:
        if element_no == 1 or element_no == 2:
            print(f'{element[0]:.3f}', end = ', ')
        elif element_no == 3:
            print(f'{element[0]:.3f}', end = ' and ')
        else:
            print(f'{element[0]:.3f}')
        element_no+=1
def main():
    inputs_x1 = list()
    inputs_x2 = list()
    inputs_x3 = list()
    inputs_w1 = list()
    while(True):
        ch = int(input('Enter \'1\' if you want to enter values of matrices manually.\nOtherwise, enter \'2\' to get default values.\nEnter choice: '))
        if ch == 1:
            while(True):
                print('The value of n must be greater than or equal to 2 and less than or equal to 4.')
                n = int(input('Enter the value of n for n × 1 matrices of x1, x2, x3 and w1: '))
                if (n >= 2 and n <= 4):
                    break
                else:
                    continue
            for i in range(0, n):
                input_x1 = float(input(f'Enter element at row {i+1}, column 1 of matrix x1: '))
                inputs_x1.append(input_x1)
                input_x2 = float(input(f'Enter element at row {i+1}, column 1 of matrix x2: '))
                inputs_x2.append(input_x2)
                input_x3 = float(input(f'Enter element at row {i+1}, column 1 of matrix x3: '))
                inputs_x3.append(input_x3)
                input_w1 = float(input(f'Enter element at row {i+1}, column 1 of matrix w1: '))
                inputs_w1.append(input_w1)
            c = int(input('Enter the value of learning constant c: '))
            x1 = np.array(inputs_x1).reshape(n, 1)
            x2 = np.array(inputs_x2).reshape(n, 1)
            x3 = np.array(inputs_x3).reshape(n, 1)
            w1 = np.array(inputs_w1).reshape(n, 1)
            print(f'\nX1: {x1}\nX2: {x2}\nX3: {x3}\nW1: {w1}')
            w2 = netcalculator(w = w1, c = c, x = x1, i = 1)
            w3 = netcalculator(w = w2, c = c, x = x2, i = 2)
            w4 = netcalculator(w = w3, c = c, x = x3, i = 3)
            print_weights(w4)
        elif ch == 2:
            c = int(input('Enter the value of learning constant c: '))
            x1 = np.array([[1], [-2], [1.5], [0]])
            x2 = np.array([[1], [-0.5], [-2], [-1.5]])
            x3 = np.array([[0], [1], [-1], [1.5]])
            w1 = np.array([[1], [-1], [0], [0.5]])
            print(f'\nX1: {x1}\nX2: {x2}\nX3: {x3}\nW1: {w1}')
            w2 = netcalculator(w = w1, c = c, x = x1, i = 1)
            w3 = netcalculator(w = w2, c = c, x = x2, i = 2)
            w4 = netcalculator(w = w3, c = c, x = x3, i = 3)
            print_weights(w4)
        else:
            print('\nInvalid choice! Please enter either \'1\' or \'2\' only.')
        cont = input('\nDo you want to run the program again?\nPress any character if so. Otherwise, hit enter key.\nEnter choice: ')
        if len(cont) < 1:
            break
if __name__ == "__main__":
    main() 
# Python runs successfully! Haribol