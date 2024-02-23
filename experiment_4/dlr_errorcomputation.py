import numpy as np
i = 1
def netcalculator(w, d, c, x, l):
    global i
    w_transpose = w.T
    print(f'w{i}_transpose is {w_transpose}')
    net = np.dot(w_transpose, x)
    print(f'Net{i} is {net[0][0]:.3f}.')
    o = 2 / (1 + np.exp(-l * net)) - 1
    print(f'o{i} is {o[0][0]:.3f}')
    f_dash_net = 0.5 * (1 - o * o)
    print(f'f\'(net{i}) is {f_dash_net[0][0]:.3f}')
    w_return = c * (d - o) * f_dash_net * x + w
    print(f'w{i+1} is', w_return)
    i = i + 1
    return w_return

def main():
    # Initialize empty lists to store user inputs
    user_inputs_x1 = []
    user_inputs_x2 = []
    user_inputs_x3 = []
    user_inputs_w1 = []
    # Extending the capability of the network by making the matrices as n × 1 matrices instead of strictly 4 × 1 matrices
    n = int(input('Enter the value of n for X1, X2, X3 and W1 n × 1 matrices: '))
    # Get user input for each element
    for i in range(n):
        user_input_x1 = float(input(f"Enter element {i + 1} for x1: "))
        user_inputs_x1.append(user_input_x1)
        user_input_x2 = float(input(f"Enter element {i + 1} for x2: "))
        user_inputs_x2.append(user_input_x2)
        user_input_x3 = float(input(f"Enter element {i + 1} for x3: "))
        user_inputs_x3.append(user_input_x3)
        user_input_w1 = float(input(f"Enter element {i + 1} for w1: "))
        user_inputs_w1.append(user_input_w1)
    
    d1 = int(input('Enter the desired target value 1: '))
    d2 = int(input('Enter the desired target value 2: '))
    d3 = int(input('Enter the desired target value 3: '))
    c1 = int(input('Enter the first learning constant value: '))
    c2 = int(input('Enter the second learning constant value: '))
    l = int(input('Enter the lambda value: '))

    # Convert the list of user inputs into a NumPy array
    x1 = np.array(user_inputs_x1).reshape(n, 1)
    x2 = np.array(user_inputs_x2).reshape(n, 1)
    x3 = np.array(user_inputs_x3).reshape(n, 1)
    w1 = np.array(user_inputs_w1).reshape(n, 1)

    '''# x1 = [1, -2, 0, -1]
    x1 = np.array([[1], [-2], [0], [-1]])
    # x2 = [0, 1.5, -0.5, -1]
    x2 = np.array([[0], [1.5], [-0.5], [-1]])
    # x3 = [-1, 1, 0.5, -1]
    x3 = np.array([[-1], [1], [0.5], [-1]])
    # w1 = [1, -1, 0, 0.5]
    w1 = np.array([[1], [-1], [0], [0.5]])
    d1 = -1
    d2 = -1
    d3 = 1
    c1 = 0.1
    c2 = 0.5
    l = 1'''
    print(f'X1: {x1}\nX2: {x2}\nX3: {x3}\nW1: {w1}\nlambda: {l}')
    # calulating w2, w3 and w4 when c = c1
    w2_c1 = netcalculator(w = w1, d = d1, c = c1, x = x1, l = l)
    w3_c1 = netcalculator(w = w2_c1, d = d2, c = c1, x = x2, l = l)
    w4_c1 = netcalculator(w = w3_c1, d = d3, c = c1, x = x3, l = l)
    print(f'Learning Completed! The final weights for c = {c1} are:')
    i = 0
    for element in w4_c1:
        if i == 0 or i == 1:
            print(f'{element[0]:.3f}', end = ", ")
        elif i == 2:
            print(f'{element[0]:.3f}', end = " and ")
        else:
            print(f'{element[0]:.3f}')
        i+=1
    # calculating w2, w3 and w4 when c = c2
    w2_c2 = netcalculator(w = w1, d = d1, c = c2, x = x1, l = l)
    w3_c2 = netcalculator(w = w2_c2, d = d2, c = c2, x = x2, l = l)
    w4_c2 = netcalculator(w = w3_c2, d = d3, c = c2, x = x3, l = l)
    print(f'Learning Completed! The final weights for c = {c2} are:')
    i = 0
    for element in w4_c2:
        if i == 0 or i == 1:
            print(f'{element[0]:.3f}', end = ", ")
        elif i == 2:
            print(f'{element[0]:.3f}', end = " and ")
        else:
            print(f'{element[0]:.3f}')
        i+=1
    error = w4_c2 - w4_c1
    print('The error in different learning rate is', error)
if __name__ == "__main__":
    main()