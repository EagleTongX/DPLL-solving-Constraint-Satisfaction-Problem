import sys
import copy

def dp(formulas):
	atoms = set()
	for f in formulas:
		for literal in f:
			atoms.add(abs(int(literal)))

	atoms = list(atoms)
	value = {}
	
	return dp1(atoms, formulas, value)


def dp1(atoms, formulas, value):
	while True:
		#check whether all clauses are satisfied
		if len(formulas) == 0:
			# success: all clauses are satisfied
			for atom in atoms:
				if atom not in value:
					value[atom] = True
			return value

		#failure: if empty clause in formulas
		if [] in formulas:
			return None

		# easy case1: find pure literal
		pure_literal = None
		for atom in atoms:
			contain_pure = False
			contain_pure_neg = False
			for f in formulas:
				if atom in f:
					contain_pure = True
				elif -1 * atom in f:
					contain_pure_neg = True
				if contain_pure and contain_pure_neg:
					break
			if contain_pure and not contain_pure_neg:
				pure_literal = atom
				break

			if contain_pure_neg and not contain_pure:
				pure_literal = -1 * atom
				break
	
		# easy case2: check single literal			
		single_literal = None
		for f in formulas:
			if len(f) == 1:
				single_literal = f[0]
				break

		#pure literal elimination	
		if pure_literal:
			value = obviousAssign(pure_literal, value)
			for f in formulas:
				if pure_literal in f:
					formulas.remove(f)

		#single literal force assignment
		elif single_literal:
			value = obviousAssign(single_literal,value)
			formulas = propagate(abs(single_literal),formulas,value)
			break
		else:
			break

	#hard case
	for atom in atoms:
		if atom not in value:
			formula_new = copy.deepcopy(formulas)
			value_new = copy.deepcopy(value)
			value_new[atom] = True
			formula_new = propagate(atom, formula_new, value_new)
			value_new = dp1(atoms,formula_new, value_new)

			if value_new is not None:
				return value_new
			else:
				value[atom] = False
				formulas = propagate(atom,formulas,value) 
				return dp1(atoms, formulas, value)

def propagate(atom,formulas,value):
	formulas_new = []
	for f in formulas:
		if atom in f and value[atom] == True or -1 * atom in f and value[atom] == False:
			pass
		elif atom in f and value[atom] == False:
			f.remove(atom)
		elif -1 * atom in f and value[atom] == True:
			f.remove(-1 * atom)
		formulas_new.append(f)

	return formulas_new


def obviousAssign(literal,value):
	if literal > 0:
		value[literal] = True
	elif literal < 0:
		value[abs(literal)] = False
	return value

def result(value):
	res = []
	if not value:
		print("No Solution")
	else:
		for k,v in value.items():
			if v == True:
				res.append([k,"T"])
			else: 
				res.append([k, "F"])

	res.sort(key = lambda x: x[0])
	for r in res:
		print("%d\t%s" % (r[0],r[1]))

	print(0)

def main():
	formulas = []	
	with open("input.txt")as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip().split()
			if line[0] == "0":
				break
			else:
				formulas.append([int(e) for e in line])
	
	return result(dp(formulas))

if __name__=='__main__':
	main()
