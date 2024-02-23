import math

def valuecalculator(inputs, weight_list, vertex, z_or_y):
    in_val = 0
    n = 3
    print('Calculating the input net...')
    for i in range(0, n):
        if z_or_y == 0:
            if i < n-1:
                print(f"x{i+1} * v{vertex}{i+1}", end = ' + ')
            else:
                print(f"v0{vertex} ", end = ' = ')
        else:
            if i < n-1:
                print(f"z{i+1} * w{vertex}{i+1}", end = ' + ')
            else:
                print("w0 ", end = ' = ')
    for i in range(0, n):
        if i < n-1:
            print(f"{inputs[i]:.4f} * {weight_list[i]}", end = ' + ')
            in_val += inputs[i] * weight_list[i]
        else:
            print(f"{weight_list[i]} ", end = ' = ')
            in_val += weight_list[i]
    print(f'{in_val:.1f}')
    calc_val = 1 / (1 + math.exp(-in_val))
    if z_or_y == 0:
        print(f'z{vertex} = {calc_val:.4f}')
    else:
        print(f'y = {calc_val:.4f}')
    return calc_val

def errorcomputer(y, t, α, λ, w, z):
    print('Computing error term...')
    f_dash_y = y * (1 - y)
    print(f'f\'(yink) = f(yin)[1 - f(yin)]\n         = {y:.4f}[1 - {y:.4f}]\n         = {f_dash_y:.4f}')
    del_k = (t - y) * f_dash_y
    print(f'δk = (tk - yk) * f\'(yink)\n   = ({t:.4f} - {y:.4f}) * {f_dash_y:.4f}\n   = {del_k:.4f}')
    print('Finding changes in weights between hidden and output layer...')
    w_new_list = list()
    for i in range(0, len(w)):
        if i < (len(w) - 1):
            w_new = w[i] + α * del_k * z[i]
            print(f'w{i+1}new = w{i+1}old + α * δ{i} * z{i+1}\n      = {w[i]} + {α} * {del_k:.4f} * {z[i]:.4f}\n      = {w_new:.4f}')
            w_new_list.append(w_new)
        else:
            w_new = w[i] + α * del_k
            print(f'w0new = w0old + α * δ{i}\n      = {w[i]} + {α} * {del_k:.4f}\n      = {w_new:.4f}')
            w_new_list.append(w_new)
    print('Computing error signal terms of hidden layer...')
    del_z_list = list()
    for i in range(1, len(w)):
        del_z = (z[i-1] * (1 - z[i-1])) * del_k * w[i-1]
        print(f'δz{i+1} = [z{i+1} * (1 - z{i+1})] * δk * w{i+1}\n    = [{y:.4f} * (1 - {y:.4f})] * {del_k:.4f} * {w[i-1]}\n    = {del_z:.4f}')
        del_z_list.append(del_z)
    return_list = [w_new_list, del_z_list]
    return return_list

def weighttrainer(α, del_z, x, v, vertex):
    v_new_list = list()
    n = len(x)
    for i in range(0, len(v)):
        if i < n:
            v_new = v[i] + α * del_z[vertex-1] * x[i]
            print(f'v{vertex}{i+1}new = v{vertex}{i+1}old + α * δz{vertex} * x{i+1}\n       = {v[i]} + {α} * {del_z[vertex-1]:.4f} * {x[i]:.4f}\n       = {v_new:.4f}')
            v_new_list.append(v_new)
        else:
            v_new = v[i] + α * del_z[vertex-1]
            print(f'v0{vertex}new = v0{vertex}old + α * δz{vertex}\n       = {v[i]} + {α} * {del_z[vertex-1]:.4f}\n       = {v_new:.4f}')
            v_new_list.append(v_new)
    return v_new_list

def ebpta_epoch(v1, v2, w, x, α, t, λ, n):
    print(f'\nV1[v11, v12, v01]:\n{v1}\nV2[v21, v22, v02]:\n{v2}\nW[w1, w2, w0]:\n{w}\nα: {α}\nt: {t}\nλ: {λ}\nX1: {x[0]}\nX2: {x[1]}')
    z1 = valuecalculator(x, v1, vertex = 1, z_or_y = 0)
    z2 = valuecalculator(x, v2, vertex = 2, z_or_y = 0)
    z = [z1, z2]
    y = valuecalculator(z, w, vertex = '', z_or_y = 1)
    w_and_z_list = errorcomputer(y, t, α, λ, w, z)
    w_new = w_and_z_list[0]
    del_z = w_and_z_list[1]
    v1_new = weighttrainer(α, del_z, x, v = v1, vertex = 1)
    v2_new = weighttrainer(α, del_z, x, v = v2, vertex = 2)
    print_values(v1_new, v2_new, w_new)
    n -= 1
    print(f'{n} Epochs remaining...')
    if n == 0:
        return [v1_new, v2_new, w_new]
    else:
        return ebpta_epoch(v1_new, v2_new, w_new, x, α, t, λ, n)
    
def print_values(v1, v2, w):
    print('v1: ', end=' ')
    for i in range(0, 3):
        print(f'{v1[i]:.4f}', end = '  ')
    print('\nv2: ', end=' ')
    for i in range(0, 3):
        print(f'{v2[i]:.4f}', end = '  ')
    print('\nw : ', end=' ')
    for i in range(0, 3):
        print(f'{w[i]:.4f}', end = '  ')

def main():
    v1 = list()
    v2 = list()
    w = list()
    x = list()
    while(True):
        ch = int(input('Enter \'1\' if you want to enter values of matrices manually.\nOtherwise, enter \'2\' to get default values.\nEnter choice: '))
        if ch == 1:
            print('Enter weights')
            for i in range(1, 3):
                input_v1 = float(input(f'Enter v1{i}: '))
                v1.append(input_v1)
                input_v2 = float(input(f'Enter v2{i}: '))
                v2.append(input_v2)
                input_w = float(input(f'Enter w{i}: '))
                w.append(input_w)
            print('Enter biases')
            input_v1 = float(input(f'Enter v01: '))
            v1.append(input_v1)
            input_v2 = float(input(f'Enter v02: '))
            v2.append(input_v2)
            input_w = float(input(f'Enter w0: '))
            w.append(input_w)
            print('Enter inputs')
            for i in range(0, 2):
                input_x = float(input(f'Enter x{i+1}: '))
                x.append(input_x)
            α = float(input('Enter the value of α: '))  # alt + 224
            t = int(input('Enter the value of t: '))
            λ = int(input('Enter the value of λ: '))
        elif ch == 2:
            v1 = [0.6, -0.1, 0.3]
            v2 = [-0.3, 0.4, 0.5]
            w = [0.4, 0.1, -0.2]
            x = [0, 1]
            α = 0.25  # alt + 224
            t = 1
            λ = 1
        else:
            print('\nInvalid choice! Please enter either \'1\' or \'2\' only.')
        v1_new = list()
        v2_new = list()
        w_new = list()
        new = list()
        n = int(input('Enter the number of epochs: '))
        new = ebpta_epoch(v1, v2, w, x, α, t, λ, n)
        v1_new = new[0]
        v2_new = new[1]
        w_new = new[2]
        print('\nLearning completed! The final weights by Error Back Propogation Training Algorithm are: ')
        print_values(v1_new, v2_new, w_new)
        cont = input('\nDo you want to run the program again?\nPress any character if so. Otherwise, hit enter key.\nEnter choice: ')
        if len(cont) < 1:
            break
if __name__ == "__main__":
    main() 