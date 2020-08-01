import matplotlib.pyplot as plt
import numpy as np
from inspect import getsourcelines


# noggrannhet=int(input("noggrannhet:"))


def plottaren(funktion, start=0, slut=5, noggrannhet=1000, plot=True, block=True, legend=None):
    x = np.linspace(start, slut, noggrannhet)

    if funktion.__class__.__name__ == "str":
        y = eval(funktion)
        label = format(funktion)

    elif funktion.__class__.__name__ == "function":
        y = funktion(x)
        label = getsourcelines(funktion)

    else:
        raise AttributeError(f"Got {funktion} but this is not a parameter nor a string")

    if legend is not None:
        label = legend

    if plot:
        plt.figure(figsize=(10, 5))
        plt.title('En funktion')
        plt.xlabel('Tid')
        plt.ylabel('Sträcka')
        plt.plot(x, y, 'g', label=label)
        plt.legend()
        plt.grid(True)
        plt.show(block=block)

    return y


plottaren("x**2", block=False)
plottaren(lambda x: x ** 2, legend="x^2")


