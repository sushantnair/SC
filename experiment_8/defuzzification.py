'''
1. Lambda cut method                                        - done
2. weighted Average     - Weighted Average Method (5)       - done
3. Height of maxima     - Max membership method (1)         - not applicable as height is not unique  
4. First of maxima                                          - done
5. Last of maxima                                           - done
6. Mean of maxima       - Mean of Maximum (4)               - done
7. Centre of centroid   - Centre of Gravity or Centroid (2) - done
8. Centre of sum        - Centre of Sums (3)                - done
Centre of Largest Area (6) is not included 
'''
import matplotlib.pyplot as plt
import numpy as np

def lambda_cut(x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    # Define the lambda (λ) value
    lambda_value = 0.5  # Adjust this value as needed
    # Find the x-values where the membership function crosses the lambda value
    lambda_cut_points = x_aggregated[y_aggregated >= lambda_value]
    # Calculate the defuzzified value as the mean of lambda-cut points
    defuzzified_value_l = np.mean(lambda_cut_points)
    print(f"Defuzzified value using Lambda-Cut method (λ = {lambda_value}): {defuzzified_value_l:.2f}")
    # Plot the aggregated membership function
    plt.figure(figsize=(8, 6))
    plt.plot(x_aggregated, y_aggregated, label='Aggregated Membership')
    plt.axhline(lambda_value, color='red', linestyle='--', label=f'λ-Cut Line (λ = {lambda_value})')
    # Find and mark the Lambda-Cut points on the graph
    lambda_cut_mask = y_aggregated >= lambda_value
    lambda_cut_points = x_aggregated[lambda_cut_mask]
    plt.scatter(lambda_cut_points, [lambda_value] * len(lambda_cut_points), color='green', label='λ-Cut Points')
    # Calculate the defuzzified value and mark it on the graph
    defuzzified_value_l = np.mean(lambda_cut_points)
    plt.axvline(defuzzified_value_l, color='blue', linestyle='--', label=f'Defuzzified (λ-Cut): {defuzzified_value_l:.2f}')
    plt.title('Lambda-Cut Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def weighted_average(a, b, c, d, e, f, α, β, γ, x_aggregated, y_aggregated):
    print('------------------------------------------------------')
    # Calculate the weighted sum of the centers of each fuzzy set
    center_c1 = (a + b) / 2
    center_c2 = (c + d) / 2
    center_c3 = (e + f) / 2
    print('Centers of curves are', center_c1, center_c2, center_c3)
    weighted_center = (center_c1 * α + center_c2 * β + center_c3 * γ)
    # Calculate the defuzzified value using the Weighted Average method
    defuzzified_value_wa = weighted_center / (α + β + γ)
    print(f"Defuzzified value using Weighted Average method: {defuzzified_value_wa:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(defuzzified_value_wa, color='red', linestyle='--', label=f'Defuzzified (Weighted Average): {defuzzified_value_wa:.2f}')
    plt.title('Weighted Average Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def height_of_maxima(a, b, c, d, e, f, x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    c1 = (a, b)
    c2 = (c, d)
    c3 = (e, f)
    # Find the maximum of the three pairs
    max_pair = max([c1, c2, c3], key=lambda pair: max(pair))
    val1, val2 = max_pair
    if val1 == val2:
        maxima_value = val1
        print(f"Height of Maxima (HoM) value: {maxima_value:.2f}")
        plt.figure(figsize=(6, 5))
        plt.plot(x_aggregated, y_aggregated)
        plt.axvline(maxima_value, color='red', linestyle='--', label=f'Maxima Value ({maxima_value:.2f})')
        plt.title('Height of Maxima (HoM) Defuzzification')
        plt.xlabel('Values')
        plt.ylabel('Membership')
        plt.ylim(0.0, max(α, β, γ) + 0.2)
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Height of Maxima (HoM) method is not applicable as height values (e and f) are not the same.")
        print("Consider using First of Maxima (FoM) or Last of Maxima (LoM) methods.")
    print('------------------------------------------------------')

def first_of_maxima(x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    # Find the x-values at which the maximum membership value occurs
    max_membership_indices = np.where(y_aggregated == np.max(y_aggregated))[0]
    # Calculate the First of Maxima (FoM) and Last of Maxima (LoM) values
    if len(max_membership_indices) > 0:
        first_max_value = x_aggregated[max_membership_indices[0]]
    else:
        first_max_value = None
    print(f"Defuzzified value using First of Maxima method (FoM): {first_max_value:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(first_max_value, color='red', linestyle='--', label=f'Defuzzified (FoM): {first_max_value:.2f}')
    plt.title('First of Maxima Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def last_of_maxima(x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    max_membership_indices = np.where(y_aggregated == np.max(y_aggregated))[0]
    # Calculate the First of Maxima (FoM) and Last of Maxima (LoM) values
    if len(max_membership_indices) > 0:
        last_max_value = x_aggregated[max_membership_indices[-1]]
    else:
        last_max_value = None
    print(f"Defuzzified value using Last of Maxima method (LoM): {last_max_value:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(last_max_value, color='red', linestyle='--', label=f'Defuzzified (LoM): {last_max_value:.2f}')
    plt.title('Last of Maxima Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def mean_of_maxima(x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    # Find the x-values at which the maximum membership value occurs
    max_membership_indices = np.where(y_aggregated == np.max(y_aggregated))[0]
    max_membership_x_values = x_aggregated[max_membership_indices]
    # Calculate the average of x-values at maximum membership
    defuzzified_value_mom = np.mean(max_membership_x_values)
    print(f"Defuzzified value using MoM method: {defuzzified_value_mom:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(defuzzified_value_mom, color='red', linestyle='--', label=f'Defuzzified (MoM): {defuzzified_value_mom:.2f}')
    plt.title('MoM Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def center_of_centroid(x_aggregated, y_aggregated, α, β, γ):
    print('------------------------------------------------------')
    defuzzified_value_c = np.sum(x_aggregated * y_aggregated) / np.sum(y_aggregated)
    print(f"Defuzzified value using Centroid method: {defuzzified_value_c:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(defuzzified_value_c, color='red', linestyle='--', label=f'Defuzzified (Centroid): {defuzzified_value_c:.2f}')
    plt.title('Centroid Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def center_of_sum(a, b, c, d, e, f, p, q, r, x, y, z, α, β, γ, x_aggregated, y_aggregated):
    print('------------------------------------------------------')
    area_c1 = 0.5 * (((b - a) + (x - p)) * (α))
    area_c2 = 0.5 * (((d - c) + (y - q)) * (β))
    area_c3 = 0.5 * (((f - e) + (z - r)) * (γ))
    print('Areas of curves are', area_c1, area_c2, area_c3)
    center_c1 = (a + b) / 2
    center_c2 = (c + d) / 2
    center_c3 = (e + f) / 2
    print('Centers of curves are', center_c1, center_c2, center_c3)
    # Calculate the defuzzified value using the Center of Sum method
    defuzzified_value_cos = (center_c1 * area_c1 + center_c2 * area_c2 + center_c3 * area_c3) / (area_c1 + area_c2 + area_c3)
    print(f"Defuzzified value using Center of Sum method: {defuzzified_value_cos:.2f}")
    plt.figure(figsize=(6, 5))
    plt.plot(x_aggregated, y_aggregated)
    plt.axvline(defuzzified_value_cos, color='red', linestyle='--', label=f'Defuzzified (Center of Sum): {defuzzified_value_cos:.2f}')
    plt.title('Center of Sum Defuzzification')
    plt.xlabel('x')
    plt.ylabel('Membership')
    # Set the y-axis limit to start from 0.0
    plt.ylim(0.0, max(α, β, γ) + 0.2)
    plt.legend()
    plt.show()
    print('------------------------------------------------------')

def main():
    while(True):
        print('------------------------------------------------------')
        print('------------------------------------------------------')
        print('------------------------------------------------------')
        print('Welcome to Defuzzification Methods Program')
        print('\nEnter 1 for default values.\nAny value otherwise.')
        ch_val = input('Enter your choice: ')
        if ch_val == '1':
            a = 1
            b = 4
            p = 0
            x = 5
            c = 4
            d = 6
            q = 3
            y = 7
            e = 6
            f = 7
            r = 5
            z = 8
            α = 0.3
            β = 0.5
            γ = 1.0
        else:
            print('------------------------------------------------------')
            print('FOR GRAPH C1:')
            a = int(input('Enter value of top-left point (a): '))
            b = int(input('Enter value of top-right point (b): '))
            p = int(input('Enter value of bottom-left point (p): '))
            x = int(input('Enter value of bottom-right point (x): '))
            α = float(input('Enter value of membership (α): '))
            print('------------------------------------------------------')
            print('------------------------------------------------------')
            print('FOR GRAPH C2:')
            c = int(input('Enter value of top-left point (c): '))
            d = int(input('Enter value of top-right point (d): '))
            q = int(input('Enter value of bottom-left point (q): '))
            y = int(input('Enter value of bottom-right point (y): '))
            β = float(input('Enter value of membership (β): '))
            print('------------------------------------------------------')
            print('------------------------------------------------------')
            print('FOR GRAPH C3:')
            e = int(input('Enter value of top-left point (e): '))
            f = int(input('Enter value of top-right point (f): '))
            r = int(input('Enter value of bottom-left point (r): '))
            z = int(input('Enter value of bottom-right point (z): '))
            γ = float(input('Enter value of membership (γ): '))
            print('------------------------------------------------------')
        # Define the x values for the different segments of C1
        x1_c1 = np.linspace(p, a, 100)  # Linear increase from p to a
        x2_c1 = np.linspace(a, b, 100)  # Constant at 0.3 from a to b
        x3_c1 = np.linspace(b, x, 100)  # Linear decrease from b to x from 4 to 5
        # Define the corresponding y values for each segment of C1
        y1_c1 = np.linspace(0, α, 100)
        y2_c1 = np.full(100, α)
        y3_c1 = np.linspace(α, 0, 100)
        # Define the x values for the different segments of C2
        x1_c2 = np.linspace(q, c, 100)  # Linear increase from q to c
        x2_c2 = np.linspace(c, d, 100)  # Constant at 0.5 from c to d
        x3_c2 = np.linspace(d, y, 100)  # Linear decrease from d to y from 6 to 7
        # Define the corresponding y values for each segment of C2
        y1_c2 = np.linspace(0, β, 100)
        y2_c2 = np.full(100, β)
        y3_c2 = np.linspace(β, 0, 100)
        # Define the x values for the different segments of C3
        x1_c3 = np.linspace(r, e, 100)  # Linear increase from r to e
        x2_c3 = np.linspace(e, f, 100)  # Constant at 1 from e to f
        x3_c3 = np.linspace(f, z, 100)  # Linear decrease from f to z from 7 to 8
        # Define the corresponding y values for each segment of C3
        y1_c3 = np.linspace(0, γ, 100)
        y2_c3 = np.full(100, γ)
        y3_c3 = np.linspace(γ, 0, 100)
        # Plot the segments for C1
        plt.plot(x1_c1, y1_c1, label=f'C1: y = p to a ({p} to {a})')
        plt.plot(x2_c1, y2_c1, label=f'C1: y = a to b ({a} to {b})')
        plt.plot(x3_c1, y3_c1, label=f'C1: y = b to x ({b} to {x})')
        # Plot the segments for C2
        plt.plot(x1_c2, y1_c2, label=f'C2: y = q to c ({q} to {c})')
        plt.plot(x2_c2, y2_c2, label=f'C2: y = c to d ({c} to {d})')
        plt.plot(x3_c2, y3_c2, label=f'C2: y = d to y ({d} to {y})')
        # Plot the segments for C3
        plt.plot(x1_c3, y1_c3, label=f'C3: y = r to e ({r} to {e})')
        plt.plot(x2_c3, y2_c3, label=f'C3: y = e to f ({e} to {f})')
        plt.plot(x3_c3, y3_c3, label=f'C3: y = f to z ({f} to {z})')
        # Set custom tick values for the y-axis and x-axis
        plt.yticks([0, 0.25, 0.5, 0.75, 1])
        plt.xticks(range(1, 9))
        # Set labels and title
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Aggregation of C1, C2, and C3 (Union)')
        # Add horizontal dotted lines for y = alpha, y = beta, and y = gamma
        plt.axhline(y=α, color='r', linestyle='--', label=f'y = α ({α})')
        plt.axhline(y=β, color='g', linestyle='--', label=f'y = β ({β})')
        plt.axhline(y=γ, color='b', linestyle='--', label=f'y = γ ({γ})')
        # Set the y-axis limit to start from 0.0
        plt.ylim(0.0, max(α, β, γ) + 0.2)
        # Add a legend
        plt.legend()
        # Display the combined graph
        plt.grid(True)
        plt.show()
        x_aggregated = np.concatenate([x1_c1, x2_c1, x3_c1, x1_c2, x2_c2, x3_c2, x1_c3, x2_c3, x3_c3])
        y_aggregated = np.concatenate([y1_c1, y2_c1, y3_c1, y1_c2, y2_c2, y3_c2, y1_c3, y2_c3, y3_c3])
        print('Defuzzification Methods')
        print('Enter 0 for all Defuzzification Methods')
        print('Enter 1 for Lambda Cut Defuzzification Method')
        print('Enter 2 for Weighted Average Defuzzification Method')
        print('Enter 3 for Height of Maxima Defuzzification Method')
        print('Enter 4 for First of Maxima Defuzzification Method')
        print('Enter 5 for Last of Maxima Defuzzification Method')
        print('Enter 6 for Mean of Maxima Defuzzification Method')
        print('Enter 7 for Center of Centroid Defuzzification Method')
        print('Enter 8 for Center of Sum Defuzzification Method')
        ch_defuz = int(input('Enter your choice: '))
        if ch_defuz == 0:
            lambda_cut(x_aggregated, y_aggregated, α, β, γ)
            weighted_average(a, b, c, d, e, f, α, β, γ, x_aggregated, y_aggregated)
            height_of_maxima(a, b, c, d, e, f, x_aggregated, y_aggregated, α, β, γ)
            first_of_maxima(x_aggregated, y_aggregated, α, β, γ)
            last_of_maxima(x_aggregated, y_aggregated, α, β, γ)
            mean_of_maxima(x_aggregated, y_aggregated, α, β, γ)
            center_of_centroid(x_aggregated, y_aggregated, α, β, γ)
            center_of_sum(a, b, c, d, e, f, p, q, r, x, y, z, α, β, γ, x_aggregated, y_aggregated)
        elif ch_defuz == 1:
            lambda_cut(x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 2:
            weighted_average(a, b, c, d, e, f, α, β, γ, x_aggregated, y_aggregated)
        elif ch_defuz == 3:
            height_of_maxima(a, b, c, d, e, f, x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 4:
            first_of_maxima(x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 5:
            last_of_maxima(x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 6:
            mean_of_maxima(x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 7:
            center_of_centroid(x_aggregated, y_aggregated, α, β, γ)
        elif ch_defuz == 8:
            center_of_sum(a, b, c, d, e, f, p, q, r, x, y, z, α, β, γ, x_aggregated, y_aggregated)
        else:
            print('Please enter correct choice of Defuzzification Method and try again!')
        print('Enter any character to run the program again.')
        print('Otherwise, hit enter key.')
        ch_cont = input('Enter your choice: ')
        if len(ch_cont) < 1:
            break
        
if __name__ == "__main__":
    main()