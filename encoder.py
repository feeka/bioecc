from f_four import F_Four


def mapper(message):
	ecc_message = []
	map_of_DNA = {'A':0,'C':1,'T':2,'G':3}	
	for i in message:
		ecc_message.append(map_of_DNA.get(i))
	return ecc_message

	
def vec_mat(vec,M):
	vec_res =[]
	print(M)

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



def make_polynom(degree,positions):
	polynom=[]
	j=0
	for i in range(degree+1):

		if i == positions[j]:
			polynom.append(1)
			if j!=len(positions)-1:
				j = j+1
		else:
			polynom.append(0)
	
	polynom.reverse()

	return polynom


def construct_generator_matrix(msg_length,polynom):
	generator_matrix = []
	for i in range(msg_length):
		generator_matrix.append(polynom)
	g_m =[]
	for i in range(len(generator_matrix)):
		g_m.append([0]*i + generator_matrix[i] + [0]*(msg_length-i-1))
		
	return g_m

def encode(degree,positions,message):
	polynom = make_polynom(degree,positions)
	gen_mat = construct_generator_matrix(len(message),polynom)
	code = vec_mat(message,gen_mat)
	return code