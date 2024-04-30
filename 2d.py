matriks=([0,0,0,0],[0,0,0,0],[0,0,
0,0],[0,0,0,0])
#isi matriks 4x4
for i in range(4):
    for j in range(4):
        if i==j:
            matriks[i][j]=0
        if i<j:
            matriks[i][j]=0
        if i>j:
            matriks[i][j]=0
#cetak bentuk matriks
for i in range(4): 
    print(matriks[i])
