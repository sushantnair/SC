list_of_rows_z1 = list()
list_of_rows_z2 = list()
list_of_rows_y = list()
alpha = int(input('Enter the value of learning rate (a): '))

def activation_function(x):
    return 1 if x >= 0 else 0

def train_perceptron(inputs, target):
    weights = [0, 0]
    delta_weights = [0, 0]
    
    for x1, x2, t in inputs:
        x = [x1, x2]
        z_in = sum(xi * wi for xi, wi in zip(x, weights))
        z_out = activation_function(z_in)
        delta_w = [alpha * (t - z_out) * xi for xi in x]
        
        for i in range(len(weights)):
            weights[i] += delta_w[i]
            delta_weights[i] += delta_w[i]
        
        if z_out == t:
            break
    
    return weights, delta_weights

def main():
    inputs_z1 = [(0, 0, 0), (0, 1, 0), (1, 0, 1), (1, 1, 0)]
    inputs_z2 = [(0, 0, 0), (0, 1, 1), (1, 0, 0), (1, 1, 0)]
    inputs_y = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    
    print('XOR Gate using Perceptron')
    print('Training perceptron Z1...')
    w1, delta_w1 = train_perceptron(inputs_z1, target=0)
    print(f'Final weights w11 and w21: {w1}\nPerceptron Z1 trained successfully!')

    print('Training perceptron Z2...')
    w2, delta_w2 = train_perceptron(inputs_z2, target=0)
    print(f'Final weights w12 and w22: {w2}\nPerceptron Z2 trained successfully!')

    print('Training perceptron Y...')
    inputs_y_modified = [(z1, z2, t) for (z1, z2, t) in inputs_y]
    w_y, delta_w_y = train_perceptron(inputs_y_modified, target=0)
    print(f'Final weights v1 and v2: {w_y}\nPerceptron Y trained successfully!')
    print('Neural Network successfully trained!')

if __name__ == "__main__":
    main()
