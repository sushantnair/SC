import numpy as np
import matplotlib.pyplot as plt

def triangular_mf(x, a, b, c):
    if x <= a:
        return 0
    elif a <= x <= b:
        return (x - a)/(b - a)
    elif b <= x <= c:
        return (c - x)/(c - b)
    else:
        return 0
    
def triangular_run():
    # Define the parameters
    print('Hit enter key for default values of a, b and c for Triangular Membership Function.')
    v_ch = input('Otherwise, enter any character.\nEnter your choice: ')
    if len(v_ch) < 1:
        a = 2
        b = 6
        c = 10
        x_range = 12
    else:
        a = int(input('Enter value of a: '))
        b = int(input('Enter value of b: '))
        c = int(input('Enter value of c: '))
        x_range = int(input('Enter range of x-axis: '))
    # Generate x values for the plot
    x_values = np.linspace(0, x_range, 100)
    # Calculate the membership values for each x value
    y_values = [triangular_mf(x, a, b, c) for x in x_values]
    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Membership value for x')
    plt.title('Triangular Membership Function')
    # Annotate the points on the x-axis
    plt.annotate(f'a={a}', xy=(a, 0), xytext=(a - 0.5, 0.1), ha='right')
    plt.annotate(f'b={b}', xy=(b, 0), xytext=(b - 0.5, 0.9), ha='right')
    plt.annotate(f'c={c}', xy=(c, 0), xytext=(c - 0.5, 0.1), ha='right')
    plt.show()
    x = (b + c)/2
    μ = max(min(((x - a)/(b - a)), ((c - x)/(c - b))), 0)
    print(f'For x = {x}, μ(x, a, b, c, d) = {μ:.2f}')

def trapezoidal_mf(x, a, b, c, d):
    if x <= a:
        return 0
    elif a <= x <= b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    else:
        return 0
    
def trapezoidal_run():
    # Define the parameters
    print('Hit enter key for default values of a, b and c for Trapezoidal Membership Function.')
    v_ch = input('Otherwise, enter any character.\nEnter your choice: ')
    if len(v_ch) < 1:
        a = 2
        b = 4
        c = 8
        d = 10
        x_range = 12
    else:
        a = int(input('Enter value of a: '))
        b = int(input('Enter value of b: '))
        c = int(input('Enter value of c: '))
        d = int(input('Enter value of d: '))
        x_range = int(input('Enter range of x-axis: '))
    # Generate x values for the plot
    x_values = np.linspace(0, x_range, 100)
    # Calculate the membership values for each x value
    y_values = [trapezoidal_mf(x, a, b, c, d) for x in x_values]
    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Membership value for x')
    plt.title('Trapezoidal Membership Function')
    # Annotate the points on the x-axis
    plt.annotate(f'a={a}', xy=(a, 0), xytext=(a - 0.5, 0.1), ha='right')
    plt.annotate(f'b={b}', xy=(b, 0), xytext=(b - 0.5, 0.1), ha='right')
    plt.annotate(f'c={c}', xy=(c, 0), xytext=(c - 0.5, 0.1), ha='right')
    plt.annotate(f'd={d}', xy=(d, 0), xytext=(d - 0.5, 0.1), ha='right')
    plt.show()
    x = (a + b)/1.6
    μ = max(min(((x - a)/(b - a)), 1, ((d - x)/(d - c))), 0)
    print(f'For x = {x}, μ(x, a, b, c, d) = {μ:.2f}')

def gaussian_mf(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean)/sigma) ** 2)

def gaussian_run():
    # Define the parameters
    print('Hit enter key for default values of mean and sigma for Gaussian Membership Function.')
    v_ch = input('Otherwise, enter any character.\nEnter your choice: ')
    if len(v_ch) < 1:
        mean = 10
        sigma = 3
        x_range = 20
    else:
        mean = int(input('Enter value of mean: '))
        sigma = int(input('Enter value of sigma: '))
        x_range = int(input('Enter range of x-axis: '))
    # Generate x values for the plot
    x_values = np.linspace(0, x_range, 100)
    # Calculate the membership values for each x value
    y_values = [gaussian_mf(x, mean, sigma) for x in x_values]
    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Membership value for x')
    plt.title('Gaussian Membership Function')
    # Annotate the points on the x-axis
    plt.annotate(f'mean={mean}', xy=(mean, 1), xytext=(mean - 1, 0.9), ha='right')
    plt.show()
    x = 0.9 * mean
    μ = np.exp(-0.5 * ((x - mean)/sigma) ** 2)
    print(f'For x = {x}, μ(x, a, b, c, d) = {μ:.2f}')

def generalized_mf(x, a, b, c):
    return 1 / (1 + ((x - c) / a) ** (2 * b))

def generalized_run():
    # Define the parameters
    print('Hit enter key for default values of a, b and c for Generalized Membership Function.')
    v_ch = input('Otherwise, enter any character.\nEnter your choice: ')
    if len(v_ch) < 1:
        a = 2
        b = 3
        c = 10
        x_range = 20
    else:
        a = int(input('Enter value of a: '))
        b = int(input('Enter value of b: '))
        c = int(input('Enter value of c: '))
        x_range = int(input('Enter range of x-axis: '))
    # Generate x values for the plot
    x_values = np.linspace(0, x_range, 100)
    # Calculate the membership values for each x value
    y_values = [generalized_mf(x, a, b, c) for x in x_values]
    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Membership value for x')
    plt.title('Generalized Membership Function')
    # Annotate the points on the x-axis
    plt.annotate(f'c={c}', xy=(c, 1), xytext=(c - 1, 0.9), ha='right')
    plt.show()
    x = 0.8 * c
    μ = 1 / (1 + ((x - c) / a) ** (2 * b))
    print(f'For x = {x}, μ(x, a, b, c) = {μ:.2f}')

def sigmoid_mf(x, a, b):
    return 1 / (1 + np.exp(-a * (x - b)))

def sigmoid_run():
    # Define the parameters
    print('Hit enter key for default values of a and b for Sigmoid Membership Function.')
    v_ch = input('Otherwise, enter any character.\nEnter your choice: ')
    if len(v_ch) < 1:
        a = 2
        b = 6
        x_range = 12
    else:
        a = int(input('Enter value of a: '))
        b = int(input('Enter value of b: '))
        x_range = int(input('Enter range of x-axis: '))
    # Generate x values for the plot
    x_values = np.linspace(0, x_range, 100)
    # Calculate the membership values for each x value
    y_values = [sigmoid_mf(x, a, b) for x in x_values]
    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Membership value for x')
    plt.title('Sigmoid Membership Function')
    # Annotate the points on the x-axis
    plt.annotate(f'b={b}', xy=(b, 0.5), xytext=(b - 1, 0.5), ha='right')
    plt.show()
    x = a + b
    μ = 1 / (1 + np.exp(-a * (x - b)))
    print(f'For x = {x}, μ(x, a, b) = {μ:.2f}')

def main():
    print('Enter:\n0 for All Membership Functions')
    print('1 for Triangular Membership Function')
    print('2 for Trapezoidal Membership Function')
    print('3 for Gaussian Membership Function')
    print('4 for Generalized Membership Function')
    print('5 for Sigmoid Membership Function')
    mf_ch = int(input('Enter your choice: '))
    if mf_ch == 0:
        triangular_run()
        trapezoidal_run()
        gaussian_run()
        generalized_run()
        sigmoid_run()
    elif mf_ch == 1:
        triangular_run()
    elif mf_ch == 2:
        trapezoidal_run()
    elif mf_ch == 3:
        gaussian_run()
    elif mf_ch == 4:
        generalized_run()
    elif mf_ch == 5:
        sigmoid_run()

if __name__ == "__main__":
    main()