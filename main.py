from encoder import *
from flask import request, render_template, redirect, flash, url_for, Flask
from forms import *

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

app.run('0.0.0.0',8080)
message = [1,2,3,2,1,3]

code = encode(3,[0,2,3],message)
print(code)