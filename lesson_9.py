import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cbook
from matplotlib.ticker import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
fig, ax = plt.subplots(figsize=(8, 6))

def f(x, a, b):
    if x != 0:
        return (pow(x,b) + pow(a,b)) / pow(x,b)
    else:
        return '!'

def raz(a, b):
    for i in range(-50, 50):
        if f(i, a, b) == '!':
            return i

#1

xleft1 = np.linspace(raz(1, 1) - 50, raz(1, 1) - 1)
xright1 = np.linspace(raz(1, 1) + 1, raz(1, 1) + 50)
yleft1 = [f(i, 1, 1) for i in xleft1]
yright1 = [f(i, 1, 1) for i in xright1]
plt.plot(xleft1, yleft1, label=r'$f(x)=\frac{x^{1} + 1^{1}}{x^{1}}$', color='red')
plt.plot(xright1, yright1, color='red')

xleft2 = np.linspace(raz(2, 1) - 50, raz(2, 1) - 1)
xright2 = np.linspace(raz(2, 1) + 1, raz(2, 1) + 50)
yleft2 = [f(i, 2, 1) for i in xleft2]
yright2 = [f(i, 2, 1) for i in xright2]
plt.plot(xleft2, yleft2, label=r'$f(x)=\frac{x^{1} + 2^{1}}{x^{1}}$', color='blue')
plt.plot(xright2, yright2, color='blue')

xleft3 = np.linspace(raz(1, 2) - 50, raz(1, 2) - 1)
xright3 = np.linspace(raz(1, 2) + 1, raz(1, 2) + 50)
yleft3 = [f(i, 1, 2) for i in xleft3]
yright3 = [f(i, 1, 2) for i in xright3]
plt.plot(xleft3, yleft3, label=r'$f(x)=\frac{x^{2} + 1^{2}}{x^{2}}$', color='green')
plt.plot(xright3, yright3, color='green')

plt.xlabel('x')  # для оси x
plt.ylabel('y')  # для оси y
plt.title('график')  # заголовок
plt.legend()

plt.grid(which='major', linewidth=1)
plt.grid(which='minor', color='grey' ,linewidth=0.5)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.tick_params(which='major', length=10, width=2)
plt.tick_params(which='minor', length=5, width=1)

plt.ylim(0, 2)
plt.xlim(-50, 50)

plt.show()

#2
fig, ax = plt.subplots(figsize=(8, 6))

x1, x2, y1, y2 = 247, 248, 0.99, 1.01  
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])


def f(x, a, b):
    if x != 0:
        return (pow(x,b) + pow(a,b)) / pow(x,b)
    else:
        return '!'

def raz(a, b):
    for i in range(-50, 50):
        if f(i, a, b) == '!':
            return i

for i in ax, axins:
    xright1 = np.linspace(raz(1, 1) + 1, raz(1, 1) + 250)
    yright1 = [f(i, 1, 1) for i in xright1]
    i.plot(xright1, yright1, label=r'$f(x)=\frac{x^{1} + 1^{1}}{x^{1}}$', color='red')

    xright2 = np.linspace(raz(2, 1) + 1, raz(2, 1) + 250)
    yright2 = [f(i, 2, 1) for i in xright2]
    i.plot(xright2, yright2, label=r'$f(x)=\frac{x^{1} + 2^{1}}{x^{1}}$', color='blue')

    xright3 = np.linspace(raz(1, 2) + 1, raz(1, 2) + 250)
    yright3 = [f(i, 1, 2) for i in xright3]
    i.plot(xright3, yright3, label=r'$f(x)=\frac{x^{2} + 1^{2}}{x^{2}}$', color='green')

    i.grid(which='major', linewidth=1)
    i.grid(which='minor', color='grey' ,linewidth=0.5)
    i.xaxis.set_minor_locator(AutoMinorLocator())
    i.yaxis.set_minor_locator(AutoMinorLocator())
    i.tick_params(which='major', length=10, width=2)
    i.tick_params(which='minor', length=5, width=1)

plt.xlabel('x')  # для оси x
plt.ylabel('y')  # для оси y
plt.title('график')  # заголовок
plt.legend()

plt.ylim(0.5, 2)
plt.xlim(0, 250)

ax.indicate_inset_zoom(axins, edgecolor="grey")

plt.show()

#3
fig, ax = plt.subplots(figsize=(8, 6))

x1, x2, y1, y2 = -247, -248, 0.99, 1.01
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])


def f(x, a, b):
    if x != 0:
        return (pow(x,b) + pow(a,b)) / pow(x,b)
    else:
        return '!'

def raz(a, b):
    for i in range(-50, 50):
        if f(i, a, b) == '!':
            return i

for i in ax, axins:
    xleft1 = np.linspace(raz(1, 1) - 250, raz(1, 1) - 1)
    yleft1 = [f(i, 1, 1) for i in xleft1]
    i.plot(xleft1, yleft1, label=r'$f(x)=\frac{x^{1} + 1^{1}}{x^{1}}$', color='red')

    xleft2 = np.linspace(raz(2, 1) - 250, raz(2, 1) - 1)
    yleft2 = [f(i, 2, 1) for i in xleft2]
    i.plot(xleft2, yleft2,label=r'$f(x)=\frac{x^{1} + 2^{1}}{x^{1}}$', color='blue')

    xleft3 = np.linspace(raz(1, 2) - 250, raz(1, 2) - 1)
    yleft3 = [f(i, 1, 2) for i in xleft3]
    i.plot(xleft3, yleft3, label=r'$f(x)=\frac{x^{2} + 1^{2}}{x^{2}}$', color='green')

    i.grid(which='major', linewidth=1)
    i.grid(which='minor', color='grey' ,linewidth=0.5)
    i.xaxis.set_minor_locator(AutoMinorLocator())
    i.yaxis.set_minor_locator(AutoMinorLocator())
    i.tick_params(which='major', length=10, width=2)
    i.tick_params(which='minor', length=5, width=1)

plt.xlabel('x')  # для оси x
plt.ylabel('y')  # для оси y
plt.title('график')  # заголовок
plt.legend()

plt.ylim(0.5, 2)
plt.xlim(-250, 0)

ax.indicate_inset_zoom(axins, edgecolor="grey")

plt.show()
#4
fig, ax = plt.subplots(1, 3, figsize=(15, 5))



def f(x, a, b):
    if x != 0:
        return (pow(x,b) + pow(a,b)) / pow(x,b)
    else:
        return '!'

def raz(a, b):
    for i in range(-50, 50):
        if f(i, a, b) == '!':
            return i

for i in range(3):
    xobsh1 = np.linspace( -100, 100)
    yobsh1 = [f(i, 1, 0) for i in xobsh1]
    ax[i].plot(xobsh1, yobsh1, 'b--', label=r'$f(x)=\frac{x^{0} + 1^{0}}{x^{0}}$' )

    xobsh2 = np.linspace(-100, 100)
    yobsh2 = [f(i, 1, -1) for i in xobsh2]
    ax[i].plot(xobsh2, yobsh2, 'r--', label=r'$f(x)=\frac{x^{-1} + 1^{-1}}{x^{-1}}$' )


    ax[i].grid(which='major', linewidth=1)
    ax[i].grid(which='minor', color='grey' ,linewidth=0.5)
    ax[i].xaxis.set_minor_locator(AutoMinorLocator())
    ax[i].yaxis.set_minor_locator(AutoMinorLocator())
    ax[i].tick_params(which='major', length=10, width=2)
    ax[i].tick_params(which='minor', length=5, width=1)

    ax[i].set_ylim(0.5, 4)
    ax[i].set_xlim(-100, 100)



xleft11 = np.linspace(raz(1, 0.5) - 100, raz(1, 0.5) - 1)
xright11 = np.linspace(raz(1, 0.5) + 1, raz(1, 0.5) + 100)
yleft11 = [f(i, 1, 0.5) for i in xleft11]
yright11 = [f(i, 1, 0.5) for i in xright11]
ax[0].plot(xleft11, yleft11, label=r'$f(x)=\frac{x^{0.5} + 1^{0.5}}{x^{0.5}}$', color='black')
ax[0].plot(xright11, yright11, color='black')

xleft12 = np.linspace(raz(1, 0.8) - 100, raz(1, 0.8) - 1)
xright12 = np.linspace(raz(1, 0.8) + 1, raz(1, 0.8) + 100)
yleft12 = [f(i, 1, 0.8) for i in xleft12]
yright12 = [f(i, 1, 0.8) for i in xright12]
ax[0].plot(xleft12, yleft12, label=r'$f(x)=\frac{x^{0.8} + 1^{0.8}}{x^{0.8}}$', color='green')
ax[0].plot(xright12, yright12, color='green')

ax[0].legend()


xleft21 = np.linspace(raz(1, -0.5) - 100, raz(1, -0.5) - 1)
xright21 = np.linspace(raz(1, -0.5) + 1, raz(1, -0.5) + 100)
yleft21 = [f(i, 1, -0.5) for i in xleft21]
yright21 = [f(i, 1, -0.5) for i in xright21]
ax[1].plot(xleft21, yleft21, label=r'$f(x)=\frac{x^{-0.5} + 1^{-0.5}}{x^{-0.5}}$', color='black')
ax[1].plot(xright21, yright21, color='black')

xleft22 = np.linspace(raz(1, -0.8) - 100, raz(1, -0.8) - 1)
xright22 = np.linspace(raz(1, -0.8) + 1, raz(1, -0.8) + 100)
yleft22 = [f(i, 1, -0.8) for i in xleft22]
yright22 = [f(i, 1, -0.8) for i in xright22]
ax[1].plot(xleft22, yleft22, label=r'$f(x)=\frac{x^{-0.8} + 1^{-0.8}}{x^{-0.8}}$', color='green')
ax[1].plot(xright22, yright22, color='green')

ax[1].legend()


xleft31 = np.linspace(raz(1, -1.5) - 100, raz(1, -1.5) - 1)
xright31 = np.linspace(raz(1, -1.5) + 1, raz(1, -1.5) + 100)
yleft31 = [f(i, 1, -1.5) for i in xleft31]
yright31 = [f(i, 1, -1.5) for i in xright31]
ax[2].plot(xleft31, yleft31, label=r'$f(x)=\frac{x^{-1.5} + 1^{-1.5}}{x^{-1.5}}$', color='black')
ax[2].plot(xright31, yright31, color='black')

xleft32 = np.linspace(raz(1, -2.5) - 100, raz(1, -2.5) - 1)
xright32 = np.linspace(raz(1, -2.5) + 1, raz(1, -2.5) + 100)
yleft32 = [f(i, 1, -2.5) for i in xleft32]
yright32 = [f(i, 1, -2.5) for i in xright32]
ax[2].plot(xleft32, yleft32, label=r'$f(x)=\frac{x^{-2.5} + 1^{-2.5}}{x^{-2.5}}$', color='green')
ax[2].plot(xright32, yright32, color='green')

ax[2].legend()

plt.show()