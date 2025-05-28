
# Classificador de Elegibilidade de Crédito

Este repositório contém um modelo treinado para classificar solicitações de crédito com base em variáveis financeiras e demográficas dos solicitantes.
Em 28/05/2025 foram incluídos os gráficos de Decision Tree e de importância das variáveis para a Elegibilidade de Crédito.

---
## ✅ Modelo Escolhido

- ****Tipo****: KNN (K-Nearest Neighbors)
- ****Biblioteca****: 'sklearn.neighbors.KNeighborsClassifier'
- ****Valor de K****: 5
- ****Acurácia no conjunto de teste (596 amostras)****: ****80,5%****
- ****Normalização utilizada****: 'StandardScaler' da 'sklearn.preprocessing'

---
## 📊 Variáveis utilizadas

A ordem das variáveis selecionadas como entrada do modelo é:

```

["salario_anual", "total_dividas", "score", "idade"]

```
 
> A variável 'credito_solicitado' não foi considerada porque não agregou desempenho ao modelo.

---
## 🔢 Codificação das Classes

O campo 'elegibilidade' (alvo) está mapeado conforme abaixo:

- '1' → ****Não Elegível**** (Negado)
- '2' → ****Elegível com Análise****
- '3' → ****Elegível****

---
## 📦 Arquivos entregues

	| Arquivo               | Descrição                                       |
	|-----------------------|-------------------------------------------------|
	| 'modelo_knn.joblib'   | Modelo KNN treinado                             |
	| 'scaler.joblib'       | Objeto 'StandardScaler' usado para normalização |

---
## 🧪 Exemplo real de previsão

****Entrada (X)****:

- 'salario_anual': ****65397.00****
- 'total_dividas': ****33706.00****
- 'score': ****0.908****
- 'idade': ****23****

****Saída prevista (y)****:

- '3' → ****Elegível****

---
## 📌 Observações

- Outliers foram removidos da variável 'score' (valores > 1).
- Os dados foram normalizados para garantir uma melhor performance do modelo.
- O modelo foi validado com 20% dos dados.

---
## 👨‍💻 Autor

Marcel Miranda.
