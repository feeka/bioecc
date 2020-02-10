from helper_math import LookUpTable

class F_Four:
	elements = {0:[0,0], 
				1: [0,1],
				2: [1,0],
				3: [1,1]}
	
	def __init__(self,n):
		self.n = n
		self.poly = self.elements.get(n)
		self.lut=LookUpTable()
	
	def perform_calculation(self,other,SIGN):
		str_res = str(self.n)+ SIGN + str(other.n)
		result = self.lut.get_table(SIGN).get(str_res)
		return result
		
	def __add__(self,other):
		return self.perform_calculation(other,"+")
	
	def __subt__(self,other):
		return self.perform_calculation(other,"-")
	
	def __mul__(self,other):
		return self.perform_calculation(other,"*")
	
	def __div__(self,other):
		return self.perform_calculation(other,"/")
	
	