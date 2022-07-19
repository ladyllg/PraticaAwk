import csv

ficheiro = open('alunos.csv', 'rt')
reader = csv.reader(ficheiro, delimiter=',', quoting=csv.QUOTE_NONE)
next(reader) # Pula cabeçalho

print("**** QUESTAO 1 *****")
for linha in reader:
    if linha[0] == '21751911' or linha[0] == '21552409':
        print(linha[0], linha[1])

ficheiro.seek(0)
next(reader) # Pula cabeçalho
print("\n**** QUESTAO 2 *****")
for linha in reader:
    if ' DE ' in linha[1]:
        print(linha[0], linha[1])
    if ' DA ' in linha[1]:
        print(linha[0], linha[1])
    if ' DO ' in linha[1]:
        print(linha[0], linha[1])

ficheiro.seek(0)
next(reader) # Pula cabeçalho
print("\n**** QUESTAO 3 *****")
notas_10 = 0; notas_0 = 0; notas_9 = 0;
for linha in reader:
    if (linha[2] == '10' or linha[3] == '10' or linha[4] == '10'):
        notas_10 += 1

    if linha[2] == '9' or linha[3] == '9' or linha[4] == '9':
        notas_9 += 1
    
    if linha[2] == '0' or linha[3] == '0' or linha[4] == '0':
        notas_0 += 1 

print("Notas 10: ", notas_10)
print("Notas 9 : ", notas_9)
print("Notas 0 : ", notas_0)

ficheiro.seek(0)
next(reader) # Pula cabeçalho
print("\n**** QUESTAO 4 *****")
notas_total = 0

while(notas_total < 1000):
    linha = next(reader)
    print(linha[0])
    notas_total += (int(linha[2]) + int(linha[3]) + int(linha[4]))

        


