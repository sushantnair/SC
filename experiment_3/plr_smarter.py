import numpy as np
def sgn(num):
    if num >= 0:
        return 1
    else:
        return -1
i = 1
def netcalculator(w, d, c, x):
    global i
    w_transpose = w.T
    print(f'w{i}_transpose is {w_transpose}')
    net = np.dot(w_transpose, x)
    print(f'Net{i} is {net[0][0]}.')
    if sgn(d) == sgn(net[0][0]):
        print(f'Correction is not performed as d{i} = sgn({net[0][0]})')
        w_return = w
        print(f'w{i+1}: {w_return}')
    else:
        print(f'Correction is performed as d{i} != sgn({net[0][0]})')
        w_return = w + c * (d - sgn(net[0][0])) * x
        print(f'w{i+1}: {w_return}')
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
    c = int(input('Enter the learning constant value: '))

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
    w1 = np.array([[1], [-1], [0], [0.5]])'''
    print(f'X1: {x1}\nX2: {x2}\nX3: {x3}\nW1: {w1}\nc: {c}')
    w2 = netcalculator(w = w1, d = d1, c = c, x = x1)
    w3 = netcalculator(w = w2, d = d2, c = c, x = x2)
    w4 = netcalculator(w = w3, d = d3, c = c, x = x3)
    print(f'Learning Completed! The final weights are:')
    i = 0
    for element in w4:
        if i == 0 or i == 1:
            print(f'{element[0]:.1f}', end = ", ")
        elif i == 2:
            print(f'{element[0]:.1f}', end = " and ")
        else:
            print(f'{element[0]:.1f}')
        i+=1
if __name__ == "__main__":
    main()