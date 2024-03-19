# given n data points, {(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)}
# we can construct a polynomial with at most n-1 degrees, which fits all the points

# first consider how to fit {(x_1, 1), (x_2, 0), ..., (x_n, 0)}
# f_1(x)= (x-x_2)...(x-x_n) (1 / (x_1-x_2)...(x1-x_n)) will do
# similarlly, we can write f_i(x) which fit {(x_1, 0), ...,(x_i, 1), ...,(x_n, 0)}
# and we do a linear comnination of all these polynomials f_i(x) where coefficients are y_i

import matplotlib.pyplot as plt

def lagrange_interpolate(datapoints, xx):
    x, y = zip(*datapoints)
    yy = 0
    for i in range(0, len(datapoints)):
        f_i = y[i] 
        for j in range(0, len(datapoints)):
            if i == j:
                continue
            f_i *= (xx - x[j])/(x[i]-x[j])
        yy += f_i
    return yy


def plot_points(datapoints):
    # Sort the list of tuples based on the first element (x value)
    datapoints = sorted(datapoints, key=lambda x: x[0])

    # Unzip the list of tuples into two lists, x and y
    x, y = zip(*datapoints)
    
    x_min, x_max = x[0], x[-1]
    n = 500
    step = (x_max - x_min)/n
    xx = [x_min + i*step for i in range(n+1)]
    yy = [lagrange_interpolate(datapoints, xi) for xi in xx]


    plt.style.use('dark_background')

    # Plot the points
    plt.scatter(x, y, marker='*', s=50)
    # Plot interpolated points
    plt.scatter(xx, yy, alpha=0.1, s=10)
    
    # Add labels and show the plot
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title('Lagrange interpolation')
    
    #save plot with transparent background
    plt.savefig('../assets/img/interpolate.png', transparent=True)
    plt.show()


# Example usage
#datapoints = [(0, 0), (1, 1), (2, 4), (3, 9)]
datapoints = [(0, 0), (3, 7), (5, 2), (8, 11)]
plot_points(datapoints)
