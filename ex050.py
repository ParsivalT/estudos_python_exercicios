impar = 0
contador = 0 
for c in range(0,7):
    n = int(input('Digite Um numero: '))
    i = n % 2
    if i == 0:
        contador += 1
        impar += n 

print(impar)
print(contador)
