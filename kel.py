print("="*40)
print("Program Pengurangan Matriks ordo 3x3")
print("Kelas : 15.1A.05")
print("NAMA : Ridai Alinza Putra    (15230257)")
print("NAMA : Sandi Apriliansyah    (15230711)")
print("NAMA : Nurmalisa Al Hawa     (15230257)")
print("NAMA : Anisya Septianur      (15230257)")
print("NAMA : Fauzan Abdurrahman    (15230257)")
print("NAMA : Azzam Ade Prakoso     (15230257)")
print("="*40)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]


C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Penjumlahan matriks
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

print("\nMatriks A:")
for row in A:
    print(row)

print("\nMatriks B:")
for row in B:
    print(row)

print("\nHasil Penjumlahan Matriks A dan B:")
for row in C:
    print(row)
