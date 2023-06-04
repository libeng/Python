import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

easings = ['Back',
           'Bounce',
           'Circ',
           'Cubic',
           'Elastic',
           'Expo',
           'Quad',
           'Quart',
           'Quint',
           'Sine']
mode = ['easeIn', 'easeOut', 'easeInOut']
path = ".\\Easings\\figures\\"


def test():
    for i in range(len(easings)):
        for j in range(len(mode)):

            fig, ax = plt.subplots()

            ax.set_xlim(0, 1)
            ax.set_ylim(-1, 2)

            line, = ax.plot([], [])

            ax2 = ax.twinx()
            ax2.set_ylim(-0.5, 1.5)

            def value(x):
                res = np.zeros_like(x)
                for z in range(len(x)):
                    res[z] = getattr(eval(easings[i]), mode[j] + easings[i])(x[z])
                return res

            def update(frame):
                x = np.arange(0, frame / 100, 0.01)
                y = value(x)
                line.set_data(x, y)
                return line,

            ani = animation.FuncAnimation(fig=fig, func=update, frames=100, blit=True)
            ani.save(path + easings[i] + '\\' + mode[j] + easings[i] + '.gif', fps=100)
            plt.close(fig)
