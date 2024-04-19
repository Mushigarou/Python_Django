def	my_var():
	i = 42
	print(f"{i} has a type {type(i)}")
	s = "42"
	print(f"{s} has a type {type(s)}")
	s1 = "quarante-deux"
	print(f"{s1} has a type {type(s1)}")
	t = True
	print(f"{t} has a type {type(t)}")
	l = [42]
	print(f"{l} has a type {type(l)}")
	d = {42 : 42}
	print(f"{d} has a type {type(d)}")
	tup = (42,)
	print(f"{tup} has a type {type(tup)}")
	tup = set()
	print(f"{tup} has a type {type(tup)}")

if __name__ == "__main__":
    my_var()