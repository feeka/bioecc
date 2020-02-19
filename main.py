from repetition_code import *
#from flask import request, render_template, redirect, flash, url_for, Flask
#from forms import *
from ecc_bio_interface import *
from codeword_detector import *

"""
app = Flask(__name__)

ALGORITHMS=[
    {
        'name':'Encoder',
        'input': 'DNA string as a message',
        'output': 'Encoded word using polynomial',
        'route': 'revcompl',
        'info':'http://rosalind.info/problems/ba1c/'
    },
]
app.config['SECRET_KEY']="a286171ec581aac9872a89d13e6226a6"
def run_mapper(seq):
	return mapper(seq)

@app.route('/', methods=('GET', 'POST'))
def encoder():
	form = Encoder()
	if form.validate_on_submit():
		flash('Calculation successfully submitted','success')
		dna_seq = form.dna_seq.data
		message=run_mapper(dna_seq)
		degree= form.degree.data
		print(type(degree))
		positions=form.positions.data
		actual_positions = []

		for i in positions:
			actual_positions.append(int(i))
		print(actual_positions)
		result = encode(degree,positions,message)
		print(result)
		return render_template('encoder.html',title="Encoded word", form=form, result=result)
	return render_template('encoder.html',title="Encoder ", form=form)
"""
def read_from_file(filename):
    file1 = open(filename, 'r')
    g_m=[]
    for line in file1:
        g_m.append(list(line[1:len(line)-2]))
    gen_mat=[]
    for i in g_m:
        row =[]
        for j in i:
            if j=="," or j==" ":
                continue
            row.append(int(j))
        gen_mat.append(row)
    return gen_mat


#app.run('0.0.0.0',8080)
message1 = [1,2,3,2,1,3]
message2 = [2,3,3,1,1,3]
k= len(message1)
messages = []
messages.append(message1)
messages.append(message2)

codewords = []
polynom = [0,2,3]
degree = 3
g_m =[]
#--------------WE ENCODE MESSAGES-------------------#
codewords = encode_messages(messages,polynom,degree,g_m)
for i in codewords:
    print("c_"+str(codewords.index(i))+"=",i)
print("->",g_m)
n=len(codewords[0])
l = 2

#--------------WE CREATE REPETITION CODES-------------------#
repetition_code = repeat_codewords(codewords,l)

print("\n","--------------------------------------","\n")
for i in codewords:
    print(("c_"+str(codewords.index(i)))*2,"=",i)

# ----WE JOIN ALL CODEWORDS IN ONE SEQUENCE----#
joined_codewords = join_for_synthesis(codewords)

# ----WE MAP ECC SEQUENCE TO BIO SEQUENCE----#
dna_seq_to_synthesise = map_codewords(joined_codewords)
print(dna_seq_to_synthesise)

# ----WE PUT SEQUENCE THROUGH BIO-BOX----#
shuffle = synthesise_and_shuffle(dna_seq_to_synthesise,n)
print(shuffle)

# ----WE REMAP ALL n-MERS to OUR {0123}----#
shuffled_codewords = remap_shuffle(shuffle)
print(shuffled_codewords)
#----INTERMEDIATE STEP FOR FURTHER CALCULATION-----#
doubled_array = transpose_vector(shuffled_codewords)
h_mat = [[0,0,1,0,1,1,1,0,0], [1, 0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 1]]
for i in h_mat:
    print(i)
print("H_MAT: ",h_mat)
print(read_from_file("generator.txt"))
#---DETECT WHETHER CODEWORD----------------------#
perform_calculation_to_check(h_mat,shuffled_codewords)
