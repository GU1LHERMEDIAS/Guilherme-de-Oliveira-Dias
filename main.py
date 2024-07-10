import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

print('\n========= STATISTICS ============\n')

# QUESTÃO 2
lista = [10, 20, 30, 40, 50]
media = statistics.mean(lista)
print("MÉDIA: ", media)

# QUESTÃO 3
lista2 = [3, 1, 4, 1, 5, 9, 2]
mediana = statistics.median(lista2)
print("MEDIANA: ", mediana)

# QUESTÃO 4
lista3 = [6, 1, 6, 7, 9, 6, 4]
moda = statistics.mode(lista3)
print("MODA: ", moda)

print('\n========= NUMPY ============\n')

# QUESTÃO 5
media = np.mean([4, 8, 15, 16, 23, 42])
print("MÉDIA: ", media)

# QUESTÃO 6
mediana = np.median([7, 5, 3, 1, 9, 11, 13])
print("MEDIANA: ", mediana)

print('\n========= CSV ============\n')

dados = pd.read_csv('dado.csv')
print(dados)

ano = np.array(dados['ano'])
vendas = np.array(dados['vendas'])

print('\n========= TKINTER ============\n')

def plot_data():
    fig, grafico = plt.subplots()
    grafico.plot(ano, vendas, marker='o', linestyle='-', color='r')

    grafico.set_xlabel('Ano')
    grafico.set_ylabel('Vendas')
    grafico.set_title('Vendas Anuais')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

janela = tk.Tk()
janela.title('Gráfico de Vendas')

btn = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
btn.pack(pady=20)

janela.mainloop()
