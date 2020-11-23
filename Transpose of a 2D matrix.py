A=[[1][2],[4][3],[5][6]]
B=[]
for i in range(len(A)):
   for j in range(len(A[0])):
       B[j][i] = A[i][j]

for b in B:
   print(b)
