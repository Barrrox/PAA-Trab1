# Trabalho 1 PAA

Alunos:
- André Gustavo Franco
- João Vitor da Silva
- Matheus Barros




























- Custo assintótico FB:
12 - atrib = 1
13 - atrib = 1
17 - laço = 3 * 2^n + 2
22 - atrib = 1 * 2^n
23 - atrib = 1 * 2^n
24 - atrib = 1 * 2^n
27 - laço = (2n + 2) * 2^n
28 - t.logico = 2 * n * 2^n
29 - soma+atrib+index = 3 * n * 2^n
32 - t.logico = 1 * n * 2^n
33 - op = 1 (pior caso isso nunca acontece)
35 - soma+atrib+index = 3 * n * 2^n
36 - op+index = 2 * n * 2^n
39 - t.logico = 1 * 2^n
40 - atrib = 1 * 2^n (pior caso isso sempre acontece)
41 - atrib = 1 * 2^n (pior caso isso sempre acontece)

T(n) = 13n * 2^n + 11 * 2^n + 4
T(n) = 2^n(13n + 11) + 4

O(n * 2^n)
