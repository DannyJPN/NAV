from matplotlib import pyplot as plt, animation


class PendulumRender:

    def render(self, time_step: float, x1: list, x2: list, y1: list, y2: list):
        fig = plt.figure()
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4, 4), ylim=(-4, 4))
        ax.set_aspect('equal')
        ax.grid()

        line, = ax.plot([], [], 'o-', lw=2)
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

        def init():
            line.set_data([], [])
            time_text.set_text('')
            return line, time_text

        def animate(i):
            thisx = [0, x1[i], x2[i]]
            thisy = [0, y1[i], y2[i]]

            line.set_data(thisx, thisy)
            return line, time_text

        ani = animation.FuncAnimation(fig, animate, range(1, len(x1)), interval=time_step * 1000, blit=True,
                                      init_func=init)
        plt.show()
