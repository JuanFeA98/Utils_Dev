import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def line_chart(X, y, theme='base', title='Titulo del gráfico', eje_x = 'Variable X', eje_y = 'Variable Y',save=False, path=None):
    fig, ax = plt.subplots(figsize=(12, 5))
    
    if theme == 'dark':
        fig.patch.set_facecolor('#21252b') 
        ax.set_facecolor('#282c34') 

        font_color='white'
    else:
        font_color='black'

    plt.title(title, color=font_color, weight=1000, fontsize=15)

    plt.xlabel(eje_x, color=font_color, fontsize=13)
    plt.ylabel(eje_y, color=font_color, fontsize=13)

    plt.xticks(fontsize=10, color=font_color, weight=1000)
    plt.yticks(fontsize=10, color=font_color, weight=500)

    plt.plot(X, y, marker='o')
    plt.grid(linewidth=0.2)

    if save:
        plt.savefig(path)
    else:
        plt.show()


if __name__ == '__main__':
    pass