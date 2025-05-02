A = [1,2,3,4,5,6,7,8,9,10]
X = int(input("Digite um numero: "))

M = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(A)):
    M[i] =  A[i] * X

print(M)