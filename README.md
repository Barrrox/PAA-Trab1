# Trabalho 1 PAA

Alunos:
- André Gustavo Franco
- João Vitor da Silva
- Matheus Barros





- Custo assintótico BinGreedy:
126 - atrib+index+op = 3 * n
127 - atrib = 1
130 - atrib = 1
133 - atrib = 1
136 - atrib+index+op = 3 * n
137 - laço = 2n + 2
138 - 4*index+atrib+op+t.logico+op=8n (pior caso 7n)
140 - atrib = 1
143 - laço = 3n + 3
146 - atrib = 1 * n
147 - atrib = 1 * n
149 - laço = (2n + 2) * n
150 - t.logico+index = 2 * n * n
151 - atrib + index = 2 * n * n
152 - atrib = 1 * n * n
155 - t.logico = 1 * n
156 - op = 1 (pior caso isso nunca acontece)
159 - t.logico+index+op = 3 * n
161 - 2*index+atrib = 3 * n
162 - soma+atrib = 2 * n
165 - soma+atrib+index = 3 * n
168 - soma+atrib+index = 3 * n
172 - index+atrib = 2 * n
173 - soma+atrib = 2 * n
176 - retorno+index = 2

T(n) = 7n^2 + 42n + 11

O(n^2)





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
