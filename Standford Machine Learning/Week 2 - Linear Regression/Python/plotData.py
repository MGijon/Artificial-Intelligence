import matplotlib.pyplot as plt
import numpy as np

def plotData(x, y):
    """Simple scatter plot."""
    plt.scatter(x=x, y=y)
    plt.show()

def plotRegresionLine(x, y, theta):
    """Simple scatter plot, original points along with Regression Line."""
    plt.scatter(x=x, y=y)

    x_ = np.linspace(start=min(x), stop=max(x), num=500)

    def RegresionLine(x, theta):
        """Returns the y coordinates of a Regression Line."""
        values = []
        for element in x:
            values.append(theta[0] + theta[1] * element)
        return values

    plt.scatter(x=x_, y=RegresionLine(x=x_, theta=theta))
    plt.title('Fitted Regression Line')
    plt.show()

def plotJ(x, y, z):
    """Function to plot the Cost Function."""
    plt.contour(x, y, z)
    plt.show()
