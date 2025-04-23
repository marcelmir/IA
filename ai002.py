#!/usr/bin/env python3
#
#  ai002.py
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

import os
import sys

# Define o tamanho do tabuleiro e a posição dos obstáculos
linhas, colunas = 6, 8
inicio = (5, 0)
fim = (0,7)
obstaculos = {(3, 1), (0, 4), (4, 0), (1, 2), (2, 3), (2,4),
			  (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)}

# Direcoes: cima, baixo, esquerda, direita
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def limpa_console():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def mostra_matriz(caminho_atual = None):
	for i in range(linhas):
		linha = ''
		for j in range(colunas):
			posicao = (i, j)
			if posicao == inicio:
				linha += ' I '
			elif posicao == fim:
				linha += ' F '
			elif posicao in obstaculos:
				linha += ' X '
			elif caminho_atual and posicao in caminho_atual:
				linha += ' * '
			else:
				linha += ' . '
		print(linha)
	print()
	
def eh_valido(x, y, visitado):
	return (0 <= x < linhas and 0 <= y < colunas and
			(x, y) not in obstaculos and (x, y) not in visitado)
			
def backtrack(x, y, visitado, caminho, todos_caminhos):
	if (x, y) == fim:
		todos_caminhos.append(caminho[:])
		return
		
	for dx, dy in direcoes:
		nx, ny = x + dx, y + dy
		if eh_valido(nx, ny, visitado):
			visitado.add((nx, ny))
			caminho.append((nx, ny))
			backtrack(nx, ny, visitado, caminho, todos_caminhos)
			caminho.pop()
			visitado.remove((nx, ny))
			
def encontra_melhor_caminho():
	visitado = set()
	visitado.add(inicio)
	caminho = [inicio]
	todos_caminhos = []
	backtrack(inicio[0], inicio[1], visitado, caminho, todos_caminhos)
	
	if not todos_caminhos:
		return None
	return min(todos_caminhos, key=len)
	
def mostra_caminho_passo_a_passo(melhor_caminho):
	caminho_atual = []
	for passo in melhor_caminho:
		caminho_atual.append(passo)
		limpa_console()
		print('Pressione <enter> para avançar cada passo...')
		mostra_matriz(caminho_atual)
		input()
		

def main(args):
	print('Layout do Tabuleiro Inicial')
	mostra_matriz()
	
	melhor_caminho = encontra_melhor_caminho()
	
	if melhor_caminho:
		print('Melhor Caminho Encontrado!!')
		print('Apresentação do caminho Passo-a-Passo...')
		input('Pressione <enter> para iniciar...')
		mostra_caminho_passo_a_passo(melhor_caminho)
		print('Caminho completado!!')
	else:
		print('Não há caminhos possíveis entre o inicio e o fim!!!')
	
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
