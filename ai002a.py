#!/usr/bin/env python3
#
#  ai002a.py
#  
#  Copyright 2025 Marcel <Marcel@DESKTOP-5BJ7NC2>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import tkinter as tk
from tkinter import messagebox
import math

# Constantes
HUMANO = 'X'
AI = 'O'

# Inicializa tabuleiro
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Verifica Vencedor
def eh_vencedor(jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Verifica se o tabuleiro esta completo
def estah_cheio():
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

# Minimax com backtrack
def minimax(eh_vez_ai):
    if eh_vencedor(AI): return 1
    if eh_vencedor(HUMANO): return -1
    if estah_cheio(): return 0

    if eh_vez_ai:
        melhor = -math.inf
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = AI
                    placar = minimax(False)
                    tabuleiro[i][j] = ' '
                    melhor = max(melhor, placar)
        return melhor
    else:
        melhor = math.inf
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = HUMANO
                    placar = minimax(True)
                    tabuleiro[i][j] = ' '
                    melhor = min(melhor, placar)
        return melhor

# Acha melhor movimento do AI
def acha_melhor_movimento():
    melhor_placar = -math.inf
    movimento = (-1, -1)
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = AI
                placar = minimax(False)
                tabuleiro[i][j] = ' '
                if placar > melhor_placar:
                    melhor_placar = placar
                    movimento = (i, j)
    return movimento

# UI com Tkinter
class jogo_da_velha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha - com Minimax AI")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.cria_tabuleiro()

    def cria_tabuleiro(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=' ', font='Arial 24', width=5, height=2,
                                command=lambda x=i, y=j: self.movimento_humano(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def movimento_humano(self, x, y):
        if tabuleiro[x][y] == ' ':
            tabuleiro[x][y] = HUMANO
            self.buttons[x][y]['text'] = HUMANO
            if self.verifica_fim_jogo(): return
            self.root.after(200, self.movimento_ai)

    def movimento_ai(self):
        i, j = acha_melhor_movimento()
        if i != -1:
            tabuleiro[i][j] = AI
            self.buttons[i][j]['text'] = AI
            self.verifica_fim_jogo()

    def verifica_fim_jogo(self):
        if eh_vencedor(HUMANO):
            messagebox.showinfo("Game Over", "Você Venceu!!")
            self.inicia_tabuleiro()
            return True
        elif eh_vencedor(AI):
            messagebox.showinfo("Game Over", "O AI Venceu!!")
            self.inicia_tabuleiro()
            return True
        elif estah_cheio():
            messagebox.showinfo("Game Over", "EMPATOU!!!")
            self.inicia_tabuleiro()
            return True
        return False

    def inicia_tabuleiro(self):
        global tabuleiro
        tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ' '

# Execução do Jogo
if __name__ == '__main__':
    root = tk.Tk()
    jogo = jogo_da_velha(root)
    root.mainloop()


def main(args):
    return 0


