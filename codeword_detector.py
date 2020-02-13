from f_four import F_Four
from ecc_bio_interface import *


def make_one_vector(multivector):
	one_vector = []
	for double_vector in multivector:
		element=0
		for j in double_vector:
			element=j
		one_vector.append(element)
	return one_vector


def matrixmult (A, B):
	rows_A = len(A)
	cols_A = len(A[0])
	rows_B = len(B)
	cols_B = len(B[0])
	if cols_A != rows_B:
		print("Cannot multiply the two matrices. Incorrect dimensions.")
		return
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
	C = [[F_Four(0) for row in range(cols_B)] for col in range(rows_A)]
	A_new = []
	for vec in A:
		row = []
		for i in vec:
			row.append(F_Four(i))
		A_new.append(row)
	B_new = []
	for vec in B:
		row = []
		for i in vec:
			row.append(F_Four(i))
		B_new.append(row)

	for i in range(rows_A):
		for j in range(cols_B):
			#if isinstance(C[i][j],int):
			for k in range(cols_A):
				intermediate = F_Four(A_new[i][k] * B_new[k][j])
				C[i][j] = intermediate +C[i][j]
	return C
# transpose :: Matrix a -> Matrix a
def transpose(m):
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m

def vec_mat(vec,M):
	vec_res =[]
	transposed =list(zip(*M))
	transposed_new = []
	for vecs in transposed:
		els = []
		for i in vecs:
			els.append(F_Four(i))
		transposed_new.append(els)
	vec_new = []
	for i in vec:
		vec_new.append(F_Four(i))
	for i in range(len(transposed_new)):
		summa=F_Four(0)
		for j in range(len(transposed_new[0])):
			umnoj = vec_new[j] * transposed_new[i][j]
			summa = summa + F_Four(umnoj)
			summa = F_Four(summa)
		vec_res.append(summa.n)
	return vec_res


def rref( M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == F_Four(0):
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return

        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        if isinstance(lv,int):
            lv = F_Four(lv)
        row = []
        for mrx in M[r]:
            if isinstance(mrx,int):
                mrx = F_Four(mrx)
            row.append(mrx/lv)
        M[r]=row
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                row1 = []
                if isinstance(lv,int):
                    lv=F_Four(lv)
                for rv, iv in zip(M[r],M[i]):
                    if isinstance(rv,int):
                        rv=F_Four(rv)
                    if isinstance(iv,int):
                        iv=F_Four(iv)
                    row1.append(iv - lv*rv)
                M[i] = row1

        lead += 1

def check_whether_codeword(list1):
	for x in list1:
		if x!= 0:
			return False
	return True

def perform_calculation_to_check(mtx_after_rref,codewords):
	list_of_cws=[]
	list_of_non_cws=[]
	for vector in codewords:
		res=vec_mat(vector,transpose(mtx_after_rref))
		if check_whether_codeword(res):
			print("------------#################------------------")
			list_of_cws.append(vector)
			print(str(mapper(vector)),"is a", "codeword".upper())
			print("------------#################------------------")

		else:
			list_of_non_cws.append(vector)
			print(mapper(vector), "is not a codeword")

	return (list_of_cws, list_of_non_cws)

def g_to_h(matrix,n,k):
	matrix_P = matrix[len(matrix)-(n-k):len(matrix)]
	for i in


mtx = [[1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1]]

mtx_new = []
for i in mtx:
    row = []
    for j in i:
        row.append(F_Four(j))
    mtx_new.append(row)

rref(mtx_new)
print("Systematic:",mtx_new)
mtx_after_rref = [[0,0,1,0,1,1,1,0,0], [1, 0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 1]]

b=[2, 1, 0, 0, 3, 1, 2, 1, 3]
c = [3, 1, 0, 1, 1, 1, 1, 3, 1]
res=matrixmult(mtx_after_rref,[[3],[1], [0], [1], [1], [1], [1], [3], [1]])
flag = check_whether_codeword(res)
if flag:
	print(b,"is a Codeword")
else:
	print("Not codeword")
print(res)
h_mat = [[0,0,1,0,1,1,1,0,0], [1, 0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 1]]
g_mat = [[1, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1]
]
rref(g_mat)
print("resultat",matrixmult(g_mat,transpose(h_mat)))
print(vec_mat(c,transpose(h_mat)))
