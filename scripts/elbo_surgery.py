import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib.lines import Line2D
import matplotlib.mlab as mlab
import matplotlib.cm as cm
from matplotlib import rc, rcParams

RED = '#d62728'
BLUE = '#1f77b4'
GREEN = '#2ca02c'

rc('text', usetex=True)
rc('font', family='serif', weight='bold')


def figure_1():
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    delta = 0.05
    x = np.arange(-5.0, 5.0, delta)
    y = np.arange(-5.0, 5.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, -1.0, -1.0)
    CS = plt.contour(X, Y, Z1, 5, cmap=cm.BuGn, label=r'$q(z_1 | x_1)$')
    center1 = plt.Circle((-1, -1), 0.05, color=BLUE, fill=True, linestyle='--', lw=0.25, alpha=1)
    plt.gca().add_artist(center1)
    CS.collections[-2].set_label(r'$q(z_1 | x_1)$')

    Z2 = mlab.bivariate_normal(X, Y, 2.0, 2.0, 0.0, 0.0)
    CS2 = plt.contour(X, Y, Z2, 5, cmap=cm.Reds)
    CS2.collections[-2].set_label(r'$p(z)$')

    # points = np.random.randn(2, 10000) - 1
    # plt.scatter(x=points[0], y=points[1], s=5, alpha=0.05, label=r'$q(z | x_1)$', color=BLUE)
    # r1 = plt.Circle((-1, -1), 1, color=BLUE, fill=False, linestyle='--', lw=1.5, alpha=1)
    # r2 = plt.Circle((-1, -1), 1.5, color=BLUE, fill=False, linestyle='--', lw=1.5, alpha=0.8)
    # r3 = plt.Circle((-1, -1), 2, color=BLUE, fill=False, linestyle='--', lw=1.5, alpha=0.5)
    # plt.gca().add_artist(r1)
    # plt.gca().add_artist(r2)
    # plt.gca().add_artist(r3)

    # points = np.random.randn(2, 10000) * 2
    # plt.scatter(x=points[0], y=points[1], s=5, alpha=0.05, label=r'$p(z)$', color=GREEN)
    # r1 = plt.Circle((0, 0), 2, color=GREEN, fill=False, linestyle='--', lw=1.5, alpha=1)
    # r2 = plt.Circle((0, 0), 3, color=GREEN, fill=False, linestyle='--', lw=1.5, alpha=0.8)
    # r3 = plt.Circle((0, 0), 4, color=GREEN, fill=False, linestyle='--', lw=1.5, alpha=0.5)
    # plt.gca().add_artist(r1)
    # plt.gca().add_artist(r2)
    # plt.gca().add_artist(r3)

    # plt.gca().add_line(Line2D([0, -1], [0, -1], linewidth=0.5, color=RED))
    # plt.contour(points[0], points[1])

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    Z3 = mlab.bivariate_normal(X, Y, 1.0, 1.0, -1.0, -1.0)
    Z4 = mlab.bivariate_normal(X, Y, 1.0, 1.0, -0.3, 1.1)
    CS3 = plt.contour(X, Y, (Z3 + Z4)/2., 5, cmap=cm.BuGn)
    CS3.collections[-2].set_label(r'$\frac{1}{2}(q(z_1 | x_1) + q(z_2 | x_2))$')
    center2 = plt.Circle((-1, -1), 0.05, color=BLUE, fill=True, linestyle='--', lw=0.25, alpha=1)
    plt.gca().add_artist(center2)
    center3 = plt.Circle((-0.3, 1.1), 0.05, color=BLUE, fill=True, linestyle='--', lw=0.25, alpha=1)
    plt.gca().add_artist(center3)

    Z2 = mlab.bivariate_normal(X, Y, 2.0, 2.0, 0.0, 0.0)
    CS4 = plt.contour(X, Y, Z2, 5, cmap=cm.Reds)
    CS4.collections[-2].set_label(r'$p(z)$')

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.legend()

    plt.savefig('figure_1.png', dpi=300)

    plt.show()

def figure_2():
    plt.figure(figsize=(5, 5))

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    delta = 0.05
    x = np.arange(-5.0, 5.0, delta)
    y = np.arange(-5.0, 5.0, delta)
    X, Y = np.meshgrid(x, y)
    Zs = []
    for i in range(10):
        mu_x, mu_y = np.random.randn(), np.random.randn()
        Zs.append(mlab.bivariate_normal(X, Y, 1.0, 1.0, mu_x, mu_y))
        center = plt.Circle((mu_x, mu_y), 0.05, color=BLUE, fill=True, linestyle='--', lw=0.25, alpha=1)
        plt.gca().add_artist(center)

    Z = sum(Zs)
    CS = plt.contour(X, Y, Z/10., 10, cmap=cm.BuGn)
    # plt.gca().pcolormesh(x, y, Z1, vmin=Z1.min(), vmax=Z1.max()*2, cmap='BuGn')
    CS.collections[-2].set_label(r'$\frac{1}{10}\left(\sum_{i = 1}^{10}q(z_i | x_i)\right)$')

    Z2 = mlab.bivariate_normal(X, Y, 2.0, 2.0, 0.0, 0.0)
    CS2 = plt.contour(X, Y, Z2, 5, cmap=cm.Reds)
    CS2.collections[-2].set_label(r'$p(z)$')

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.legend()

    plt.savefig('figure_2.png', dpi=300)

    plt.show()

figure_2()