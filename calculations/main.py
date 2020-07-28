import matplotlib.pyplot as plt
import numpy as np




# def plottaren(funktion, start, slut, noggrannhet):
#     x1 = np.linspace(start, slut, noggrannhet)
#     y = np.zeros(noggrannhet)
    for i, x in enumerate(x1):
        y[i] = eval(funktion)
#     plt.figure()
#     plt.plot(y)
#     plt.show()
#
#
# plottaren("x**2", 0, 10, 100)



def plottaren2(funktion, start, slut, noggrannhet):
    x = np.linspace(start, slut, noggrannhet)
    y = funktion
    fig = plt.figure(figsize=(10, 5))
    # Add a title
    plt.title('En funktion')
    # Add X and y Label
    plt.ylabel('Tid')
    plt.ylabel('Sträcka')
    plt.plot(x, y, 'g', '-.')
    plt.legend()
    plt.show()


plottaren2('x ** 2', 0, 10, 100)




# y = 1/(2 * np.pi)**0.5 * np.exp(-x**2 / 2)
