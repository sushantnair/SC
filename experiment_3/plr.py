import numpy as np
def sgn(num):
    if num >= 0:
        return 1
    else:
        return -1
def netcalculator(w1, d1, d2, d3, c, x1, x2, x3):
    w1_transpose = w1.T
    print(f'w1_transpose is {w1_transpose}')
    net1 = np.dot(w1_transpose, x1)
    print(f'Net1 is {net1[0][0]}.')
    #print(sgn(net1[0][0]))
    if sgn(d1) == sgn(net1[0][0]):
        print(f'Correction is not performed as d1 = sgn({net1[0][0]})')
        w2 = w1
        print(f'w2: {w2}')
    else:
        print(f'Correction is performed as d1 != sgn({net1[0][0]})')
        w2 = w1 + c * (d1 - sgn(net1[0][0])) * x1
        print(f'w2: {w2}')
    w2_transpose = w2.T
    print(f'w2_transpose is {w2_transpose}')
    net2 = np.dot(w2_transpose, x2)
    print(f'Net2 is {net2[0][0]}.')
    if sgn(d2) == sgn(net2[0][0]):
        print(f'Correction is not performed as d2 = sgn({net2[0][0]})')
        w3 = w2
        print(f'w3: {w3}')
    else:
        print(f'Correction is performed as d2 != sgn({net2[0][0]})')
        w3 = w2 + c * (d2 - sgn(net2[0][0])) * x2
        print(f'w3: {w3}')
    w3_transpose = w3.T
    print(f'w3_transpose is {w3_transpose}')
    net3 = np.dot(w3_transpose, x3)
    print(f'Net3 is {net3[0][0]}.')
    if sgn(d3) == sgn(net3[0][0]):
        print(f'Correction is not performed as d3 = sgn({net3[0][0]})')
        w4 = w3
        print(f'w4: {w4}')
    else:
        print(f'Correction is performed as d3 != sgn({net3[0][0]})')
        w4 = w3 + c * (d3 - sgn(net3[0][0])) * x3
        print(f'w4: {w4}')
    print(f'Learning Completed! The final weights are:')
    i = 0
    for element in w4:
        if i == 0 or i == 1:
            print(element[0], end = ", ")
        elif i == 2:
            print(element[0], end = " and ")
        else:
            print(element[0])
        i+=1

def main():
    # x1 = [1, -2, 0, -1]
    
    # Initialize empty lists to store user inputs
    user_inputs_x1 = []
    user_inputs_x2 = []
    user_inputs_x3 = []
    user_inputs_w1 = []

    # Get user input for each element
    for i in range(4):
        user_input_x1 = float(input(f"Enter element {i + 1} for x1: "))
        user_inputs_x1.append(user_input_x1)
        user_input_x2 = float(input(f"Enter element {i + 1} for x2: "))
        user_inputs_x2.append(user_input_x2)
        user_input_x3 = float(input(f"Enter element {i + 1} for x3: "))
        user_inputs_x3.append(user_input_x3)
        user_input_w1 = float(input(f"Enter element {i + 1} for w1: "))
        user_inputs_w1.append(user_input_w1)

    # Convert the list of user inputs into a NumPy array
    x1 = np.array(user_inputs_x1).reshape(4, 1)
    x2 = np.array(user_inputs_x2).reshape(4, 1)
    x3 = np.array(user_inputs_x3).reshape(4, 1)
    w1 = np.array(user_inputs_w1).reshape(4, 1)

    # x2 = [0, 1.5, -0.5, -1]
    # x2 = np.array([[0], [1.5], [-0.5], [-1]])
    # x3 = [-1, 1, 0.5, -1]
    # x3 = np.array([[-1], [1], [0.5], [-1]])
    # w1 = [1, -1, 0, 0.5]
    # w1 = np.array([[1], [-1], [0], [0.5]])
    d1 = -1
    d2 = -1
    d3 = 1
    c = 0.1
    print(f'X1: {x1}\nX2: {x2}\nX3: {x3}\nW1: {w1}\nc: {c}')
    netcalculator(w1, d1, d2, d3, c, x1, x2, x3)
if __name__ == "__main__":
    main()