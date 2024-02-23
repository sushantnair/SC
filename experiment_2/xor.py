list_of_rows_z1 = list()
list_of_rows_z2 = list()
list_of_rows_y = list()
alpha = int(input('Enter the value of learning rate (a): '))
def epoch(w1, w2, row, perceptron, flag):
    if row > 4:
        print('Next Epoch is getting generated now...')
        row = 1
    if flag == False:
        if perceptron == 'z1':
            if row == 1:
                x1 = 0
                x2 = 0
                t = 0
            elif row == 2:
                x1 = 0
                x2 = 1
                t = 0
            elif row == 3:
                x1 = 1
                x2 = 0
                t = 1
            elif row == 4:
                x1 = 1
                x2 = 1
                t = 0
            a = alpha
            w11 = w1
            w21 = w2
            w11_new = w11 + int(a * t * x1)
            w21_new = w21 + int(a * t * x2)
            Δw11 = w11_new - w11
            Δw21 = w21_new - w21
            z1_in = x1 * w11 + x2 * w21
            # Threshold Activation Function
            if z1_in >= 0:
                z1_out = 1
            else:
                z1_out = 0
            list_of_rows_z1.append((x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
            if z1_out == t:
                flag = True
            print(row, (x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
            row += 1
            epoch(w11_new, w21_new, row, perceptron, flag)
        elif perceptron == 'z2':
            if row == 1:
                x1 = 0
                x2 = 0
                t = 0
            elif row == 2:
                x1 = 0
                x2 = 1
                t = 1
            elif row == 3:
                x1 = 1
                x2 = 0
                t = 0
            elif row == 4:
                x1 = 1
                x2 = 1
                t = 0
            a = alpha
            w12 = w1
            w22 = w2
            w12_new = w12 + int(a * t * x1)
            w22_new = w22 + int(a * t * x2)
            Δw12 = w12_new - w12
            Δw22 = w22_new - w22
            z2_in = x1 * w12 + x2 * w22
            # Threshold Activation Function
            if z2_in >= 0:
                z2_out = 1
            else:
                z2_out = 0
            list_of_rows_z2.append((x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
            if z2_out == t:
                flag = True
            row += 1
            epoch(w12_new, w22_new, row, perceptron, flag)
        elif perceptron == 'y':
            if row == 1:
                z1 = 0
                z2 = 0
                t = 0
            elif row == 2:
                z1 = 0
                z2 = 1
                t = 1
            elif row == 3:
                z1 = 1
                z2 = 0
                t = 1
            elif row == 4:
                z1 = 0
                z2 = 0
                t = 0
            a = alpha
            v1 = w1
            v2 = w2
            v1_new = v1 + int(a * t * v1)
            v2_new = v2 + int(a * t * v2)
            Δv1 = v1_new - v1
            Δv2 = v2_new - v2
            y_in = z1 * v1 + z2 * v2
            # Threshold Activation Function
            if y_in >= 0:
                y_out = 1
            else:
                y_out = 0
            row += 1
            list_of_rows_y.append((z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
            if y_out == t:
                flag = True
            row += 1
            epoch(v1_new, v2_new, row, perceptron, flag)
    elif flag == True:
        if perceptron == 'z1':
            if row == 1:
                x1 = 0
                x2 = 0
                t = 0
            elif row == 2:
                x1 = 0
                x2 = 1
                t = 0
            elif row == 3:
                x1 = 1
                x2 = 0
                t = 1
            elif row == 4:
                x1 = 1
                x2 = 1
                t = 0
            # a = alpha
            w11 = w1
            w21 = w2
            w11_new = w11 
            w21_new = w21 
            Δw11 = 0
            Δw21 = 0
            z1_in = x1 * w11 + x2 * w21
            # Threshold Activation Function
            if z1_in >= 0:
                z1_out = 1
            else:
                z1_out = 0
            list_of_rows_z1.append((x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
            row += 1
            if row < 4:
                epoch(w11_new, w21_new, row, perceptron, flag)
            else:
                return list_of_rows_z1
        elif perceptron == 'z2':
            if row == 1:
                x1 = 0
                x2 = 0
                t = 0
            elif row == 2:
                x1 = 0
                x2 = 1
                t = 1
            elif row == 3:
                x1 = 1
                x2 = 0
                t = 0
            elif row == 4:
                x1 = 1
                x2 = 1
                t = 0
            # a = alpha
            w12 = w1
            w22 = w2
            w12_new = w12 
            w22_new = w22 
            Δw12 = 0
            Δw22 = 0
            z2_in = x1 * w12 + x2 * w22
            # Threshold Activation Function
            if z2_in >= 0:
                z2_out = 1
            else:
                z2_out = 0
            list_of_rows_z2.append((x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
            row += 1
            if row < 4:
                epoch(w21_new, w22_new, row, perceptron, flag)
            else:
                return list_of_rows_z2
        elif perceptron == 'y':
            if row == 1:
                z1 = 0
                z2 = 0
                t = 0
            elif row == 2:
                z1 = 0
                z2 = 1
                t = 1
            elif row == 3:
                z1 = 1
                z2 = 0
                t = 1
            elif row == 4:
                z1 = 0
                z2 = 0
                t = 0
            # a = alpha
            v1 = w1
            v2 = w2
            v1_new = v1
            v2_new = v2 
            Δv1 = 0
            Δv2 = 0
            y_in = z1 * v1 + z2 * v2
            # Threshold Activation Function
            if y_in >= 0:
                y_out = 1
            else:
                y_out = 0
            list_of_rows_y.append((z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
            row += 1
            if row < 4:
                epoch(v1_new, v2_new, row, perceptron, flag)
            else:
                return list_of_rows_y
    else:
        print('#')
def main():
    print('XOR Gate using Perceptron')
    print('Training perceptron Z1...')
    z1_list = epoch(w1 = 0, w2 = 0, row = 1, perceptron = 'z1', flag = False)
    w11 = 1 #z1_list[-1][5]
    w21 = 1 #z1_list[-1][6]
    print(f'The final value of w11 and w21 is {w11} and {w21}\nPerceptron Z1 has been successfully trained!')
    # for the first time, assumption is made that the weights 
    # for perceptron z1 is 0 i.e., w11 = w21 = 0
    # further, the values of x1, x2 and t depend on the type of perceptron, 
    # so that type is sent as a parameter
    # also, until the value of z1out is equal to t, 
    # the flag will be False
    # when the flag becomes True, then that is the last epoch 
    # and suppose for that epoch we are in row 2 when 
    # the flag becomes True then for rows 3 and 4 the values of 
    # w1 and w2 remain constant with Δw1 = Δw2 = 0
    # finally, the function returns the values of row, x1, x2, t, 
    # w11, w21, Δw11, Δw21 as a list for that row in the 
    # epoch table when the perceptron is trained properly, 
    # so that the values of w11 and w21 can be used to calculate
    # weights for perceptron y and the rest of the data can be 
    # printed as a neat table. 
    # a list of tuples is generated like the one below:
    # [(1, 0, 0, 0, 0, 0, 0, 0), (2, 0, 1, 1, -1, 1, -1, 1), ..., 
    # (4, 1, 1, 0, final value of w11, final value of ww21, 0, 0)]
    # we have to extract those final values
    print('Training perceptron Z2...')
    z2_list = epoch(w1 = 0, w2 = 0, row = 1, perceptron = 'z2', flag = False)
    w12 = 1 #z2_list[-1][5]
    w22 = 1 #z2_list[-1][6]
    print(f'The final value of w12 and w22 is {w12} and {w22}\nPerceptron Z2 has been successfully trained!')
    print('Training perceptron Y...')
    w1 = w11 + w21
    w2 = w12 + w22
    y_list = epoch(w1 = w1, w2 = w2, row = 1, perceptron = 'y', flag = False)
    v1 = y_list[-1][5]
    v2 = y_list[-1][6]
    # change the values of w1 and w2 based on the last values of w1 and w2
    print(f'The final value of v1 and v2 is {v1} and {v2}\nPerceptron Y has been successfully trained!\nNeural Network successfully trained!')
if __name__ == "__main__":
    main()  