matriz=[[1, 5, 1],[2, 1, 2],[3, 0, 1],[1, 4, 4]]
#matriz_sliced=[matriz[0], sum(matriz[0]), matriz[1], sum(matriz[1]), matriz[2], sum(matriz[2]), matriz[3], sum(matriz[3])]


matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)
