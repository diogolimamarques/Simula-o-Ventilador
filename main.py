from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np


# VELOCIDADE DA ROTAÇÂO
vel_vent = 1
# ESPESSURA DA LINHA
linha = 3

# INSTÂNCIA DA PLOTAGEM
fig = plt.figure()
ax = plt.subplot(111, projection='polar')

# CLASSE DO UPDATER

class LinkAnimator:
    def __init__(self, ax, link_size=15):
        self._ax = ax
        self._link_size = link_size
        self._link = self._ax.plot([0, 0], [0, 15], lw=linha)[0]

    def __call__(self, theta):
        self._link.set_data([theta] * 2, [0, 15])
        return self._link,


animator = LinkAnimator(ax, link_size=15)
# INTERVALOS DOS ANGULOS
theta = np.linspace(0, 2*np.pi, 90)
theta = theta*(2**vel_vent/2)
anim = FuncAnimation(fig, animator, frames=theta, blit=True, repeat=True, interval = 8)

# EXIBIR
while(i >= 0):
    plt.show()

def toggle_plot():
    fig.set_visible(not fig.get_visible())
    plt.draw()
