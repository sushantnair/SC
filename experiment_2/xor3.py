list_of_rows_z1 = list()
list_of_rows_z2 = list()
list_of_rows_y = list()
flag_z1 = False
flag_z2 = False
flag_y = False
alpha = float(input('Enter the value of learning rate (a): '))

def epoch(w1, w2, row, perceptron):
    global flag_z1, flag_z2, flag_y
    if row > 4:
        print('New Epoch...')
        row = 1
    if flag_z1 == False and perceptron == 'z1':
        print('Flag false and perceptron Z1')
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
        z1_in = x1 * w11_new + x2 * w21_new
        if z1_in >= 0:
            z1_out = 1
        else:
            z1_out = 0
        list_of_rows_z1.append((x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
        if z1_out == t:
            flag_z1 = True
            print('Flag true', (x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
        else:
            print('Flag false', (x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
        return epoch(w11_new, w21_new, row + 1, perceptron)

    elif flag_z2 == False and perceptron == 'z2':
        print('Flag false and perceptron Z2')
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
        z2_in = x1 * w12_new + x2 * w22_new
        if z2_in >= 0:
            z2_out = 1
        else:
            z2_out = 0
        list_of_rows_z2.append((x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
        if z2_out == t:
            flag_z2 = True
            print('Flag true', (x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
        else:
            print('Flag false', (x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
        return epoch(w12_new, w22_new, row + 1, perceptron)

    elif flag_y == False and perceptron == 'y':
        print('Flag false and perceptron Y')
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
        y_in = z1 * v1_new + z2 * v2_new
        if y_in >= 0:
            y_out = 1
        else:
            y_out = 0
        list_of_rows_y.append((z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
        if y_out == t:
            flag_y = True
            print('Flag true', (z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
        else:
            print('Flag false', (z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
        return epoch(v1_new, v2_new, row + 1, perceptron)

    elif flag_z1 == True and perceptron == 'z1':
        print('Flag true and perceptron Z1')
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
        w11 = w1
        w21 = w2
        w11_new = w11
        w21_new = w21
        Δw11 = 0
        Δw21 = 0
        z1_in = x1 * w11 + x2 * w21
        if z1_in >= 0:
            z1_out = 1
        else:
            z1_out = 0
        list_of_rows_z1.append((x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
        if row < 4:
            print('More rows to go', (x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
            return epoch(w11_new, w21_new, row + 1, perceptron)
        else:
            print('Last row', (x1, x2, t, z1_in, z1_out, w11, w21, Δw11, Δw21))
            return list_of_rows_z1

    elif flag_z2 == True and perceptron == 'z2':
        print('Flag true and perceptron Z2')
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
        w12 = w1
        w22 = w2
        w12_new = w12
        w22_new = w22
        Δw12 = 0
        Δw22 = 0
        z2_in = x1 * w12 + x2 * w22
        if z2_in >= 0:
            z2_out = 1
        else:
            z2_out = 0
        list_of_rows_z2.append((x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
        if row < 4:
            print('More rows to go', (x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
            return epoch(w12_new, w22_new, row + 1, perceptron)
        else:
            print('Last row', (x1, x2, t, z2_in, z2_out, w12, w22, Δw12, Δw22))
            return list_of_rows_z2

    elif flag_y == True and perceptron == 'y':
        print('Flag true and perceptron Y')
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
        v1 = w1
        v2 = w2
        v1_new = v1
        v2_new = v2
        Δv1 = 0
        Δv2 = 0
        y_in = z1 * v1 + z2 * v2
        if y_in >= 0:
            y_out = 1
        else:
            y_out = 0
        list_of_rows_y.append((z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
        if row < 4:
            print('More rows to go', (z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
            return epoch(v1_new, v2_new, row + 1, perceptron)
        else:
            print('Last row', (z1, z2, t, y_in, y_out, v1, v2, Δv1, Δv2))
            return list_of_rows_y

def main():
    print('XOR Gate using Perceptron')
    print('Tuple structure (for Z1): X1, X2, t, Z1_IN, Z1_OUT, W11, W21, ΔW11, ΔW21')
    print('Training perceptron Z1...')
    z1_list = epoch(w1 = 1, w2 = 1, row = 1, perceptron = 'z1')
    #for tuple in z1_list:
    #    print(tuple)
    w11 = z1_list[-1][5]
    w21 = z1_list[-1][6]
    print(f'The final value of w11 and w21 is {w11} and {w21}\nPerceptron Z1 has been successfully trained!')
    print('Tuple structure (for Z2): X1, X2, t, Z2_IN, Z2_OUT, W12, W22, ΔW12, ΔW22')
    print('Training perceptron Z2...')
    z2_list = epoch(w1 = 1, w2 = 1, row = 1, perceptron = 'z2')
    #for tuple in z2_list:
    #    print(tuple)
    w12 = z2_list[-1][5]
    w22 = z2_list[-1][6]
    print(f'The final value of w12 and w22 is {w12} and {w22}\nPerceptron Z2 has been successfully trained!')
    print('Tuple structure (for Y): Z1, Z2, t, Y_IN, Y_OUT, V1, V2, ΔV1, ΔV2')
    print('Training perceptron Y...')
    w1 = w11 + w21
    w2 = w12 + w22
    y_list = epoch(w1 = w1, w2 = w2, row = 1, perceptron = 'y')
    #for tuple in y_list:
    #    print(tuple)
    v1 = y_list[-1][5]
    v2 = y_list[-1][6]
    print(f'The final value of v1 and v2 is {v1} and {v2}\nPerceptron Y has been successfully trained!')
    print('Neural Network successfully trained!')

if __name__ == "__main__":
    main()