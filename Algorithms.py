from fractions import gcd, Fraction
from math import floor, sqrt
from collections import Counter
import itertools

#modular inversion
def inversed_el(fig, mod):    #fig and mod can be not prime
	if gcd(fig, mod)!=1:
		print("Reversed element does not exist cause given figure is not mutually simple with module")
	else:
		remainder = None
		factor = None
		table = [[], [0, 1], [1]]
		while remainder!=0:
			remainder = mod%fig
			factor = mod//fig
			mod = fig
			fig  = remainder
			table[0].append(factor)

		table[2].append(table[0][0])    #special step

		for i in range(1,len(table[0])):
			table[1].append(table[0][i]*table[1][i]+table[1][i-1])
			table[2].append(table[0][i]*table[2][i]+table[2][i-1])

		if table[1][len(table[1])-2]*table[2][len(table[2])-1]-table[1][len(table[1])-1]*table[2][len(table[2])-2]==1:
			return (-table[2][len(table[2])-2]+table[2][len(table[2])-1])
		else:
			return (table[2][len(table[2])-2])


#solving congruency a*x=b (mod m)
def linear_congr(a, b, mod):
	divisor = gcd(a, mod)

	if divisor==1:
		x = (b*inversed_el(a, mod))%mod
		return x
	else:
		if b%divisor!=0:
			print("This equation has no solution")
		else:   #if divisor divides b then this equation has eval('divisor') answers
			answers = []
			a = int(a/divisor)
			b = int(b/divisor)
			mod = int(mod/divisor)

			x = (b*inversed_el(a, mod))%mod

			for answer in range(divisor):
				answers.append(x+answer*mod)
			return answers

#checks if given number is prime
def is_prime(n):
	if n == 1:
		warn = "1  is not a prime number"
		return warn
	else:
		d = 2
		while n % d != 0:
			d += 1
		return d == n

#factorization of given number
def factorize(n):
   ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       ans.append(n)
   return ans

#calculates Legendre symbol
def legendre_symbol(a,p):
	if is_prime(p) and gcd(a,p)==1:
		l_s = (a**(int((p-1)/2)))%p
		return l_s == 1

#Euler function is a function which calculates the amount of mutually simple numbers with the given number
def euler_func(num):
	factor = factorize(num)
	primes = set(factor)  #for this function we need only different primes, so throw away the ones which repeat
	res = num
	for prime in primes:
		res = res*(1-Fraction(1, prime))		
	return res

#Möbius function is a function which returns:
#						0 if given number can be divided by number in second power
#						1 if it can be divided by even amount of prides
#						-1 if it can be divided by odd amount of prides
def mebius_func(num):
	factor = factorize(num)
	amount_of_divs = 0
	for prime in factor:
		if factor.count(prime)>1:
			return 0
		else:
			amount_of_divs+=1
	return (-1)**amount_of_divs

#method for solving congruency x^2=a (mod p)
def tonelli_shanks(a,p):
	if is_prime(p):
		if legendre_symbol(a,p):

			#represent p-1 = 2^s*q
			s = 0
			var = p-1
			while var%2 == 0:
				s+=1
				var = int(var/2)

			q = int((p-1)/2**s)

			#find quadratic non-residue
			z=1
			while legendre_symbol(z,p):
				z+=1

			c = pow(z, q, p)
			r = pow(a, int((q+1)/2), p)
			t = pow(a, q, p)
			m = s

			while t%p != 1:
				i = 1
				while (t**2**i)%p != 1:
					i+=1

				b = c**2**(m-i-1)%p
				r = (r*b)%p
				t = (t*b**2)%p
				c = (b**2)%p
				m = i

			return [r, -r]

		else:
			print("This congruency has no solution")
	else:
		print("Module must be a prime number")
		
#sys_list = [[a1, mod1], [a2, mod2], ...]
# !!! each equation of system has to be represented as x = a (mod m), use solution for linear_congr if not
def sys_of_linear_congrs(sys_list):
	mod = 1
	#list_of_temp_mods = []
	#list_of_reversed_mods = []
	res_list = []

	for i in range(0, len(sys_list)):
		mod *= sys_list[i][1]

	for counter in range(0, len(sys_list)):
		temp_mod = 1
		for md2 in sys_list:
			if sys_list.index(md2) != counter:
				temp_mod *= md2[1]
		#list_of_temp_mods.append(temp_mod)
		#list_of_reversed_mods.append(inversed_el(temp_mod%sys_list[counter][1],sys_list[counter][1]))
		res_list.append(temp_mod*inversed_el(temp_mod%sys_list[counter][1],sys_list[counter][1])*sys_list[counter][0])

	answer = sum(res_list)%mod
	return answer

#sum of two points of elliptic curve (points have different coordinates)
def sum_of_points(x1, y1, x2, y2, mod):
	x3 = (((y1-y2)*inversed_el((x1-x2)%mod,mod))**2-x1-x2)%mod
	y3 = (-y1+(y1-y2)*inversed_el((x1-x2)%mod,mod)*(x1-x3))%mod
	return [x3, y3]

#not done yet
def point_ord(x, y, a, mod):
	acquired = -y%mod
	ord=1
	while y != acquired:
		x_coord = (((3*(x**2)+a)*inversed_el((2*y)%mod,mod))**2-2*x)%mod
		y_coord = (-y+(3*x**2+a)*inversed_el((2*y)%mod,mod)*(x-x_coord))%mod

		print(x_coord, y_coord)
		x=x_coord
		y=y_coord
		ord+=1
	return ord

#if char equation is x^n+a[n-1]x^(n-1)+a[n-2]x^(n-2)+...+a[1]x+a[0] then coefs_list=[a[0], a[1], ..., a[n-1]]
def shift_register(coefs_list, mod, sequence_list):
	if len(sequence_list)!=(len(coefs_list)-1):
		print('The sequence must contain {} elements'.format(len(coefs_list)-1))
	else:
		sn = [(-si)%mod for si in coefs_list[:-1]]  #sn = [-a[0], -a[1], ...]
		period=1
		res = sequence_list[1:]
		res.append(sum([sn[x]*sequence_list[x] for x in range(len(sn))])%mod)
		print(res)
		while sequence_list != res:
			last_reg = sum([sn[x]*res[x] for x in range(len(sn))])%mod
			res.remove(res[0])
			res.append(last_reg)
			period+=1
			print(res)
		print(period)

#lambda matrix for basis type=1
def lambda_matrix(mod):
	l_m = []
	for i in range(mod):
		line = []
		for j in range(mod):
			if (2**i+2**j)%(mod+1)==0 or (2**i+2**j)%(mod+1)==1:
				line.append(1)
			else:
				line.append(0)
		l_m.append(line)
	return l_m

#lambda matrix for basis type=2
def lambda_matrix2(mod):
	l_m = []
	for i in range(mod):
		line = []
		for j in range(mod):
			if (2**i+2**j)%(2*mod+1)==2*mod or (2**i+2**j)%(2*mod+1)==1 or (2**i-2**j)%(2*mod+1)==2*mod or (2**i-2**j)%(2*mod+1)==1:
				line.append(1)
			else:
				line.append(0)
		l_m.append(line)
	return l_m


#Silver–Pohlig–Hellman algorithm which computes a discrete logarithms in a finite abelian group (g^x=y mod p)
def SPH(g, y, p): #g is a generator, p is a prime number
	if is_prime(p) and is_generator(g):
		mods = factorize(p-1)
		only_diff_mods = set(mods)#some primes can repeat, we do not need them
		sys_list = []

		for prime in only_diff_mods:
			r_list = [g**(int((p-1)*j/prime))%p for j in range(prime)]
			x_list = []
			temp_y = y # we can not change y cause each time in loop it must have initial value
			
			for power in range(1, mods.count(prime)+1):
				for r_val in r_list:
					if temp_y**int((p-1)/prime**power)%p == r_val:
						x=r_list.index(r_val)
						x_list.append(x*prime**(power-1))
						break
						
				temp_y = (temp_y*inversed_el(g**(prime**(power-1)*r_list.index(r_val)), p))%p
							
			res = sum(x_list)%(prime**mods.count(prime))
			sys_list.append([res, prime**mods.count(prime)])

		return sys_of_linear_congrs(sys_list)
	else:
		print("Given module is not prime or g is not a generator")

# !notice that this function finds only the first (minimal) generator
# !generatos exist only for such modules: 2, 4, p^a, 2*p^a; where p is a prime
# !if generator exists, then there are euler_func(euler_func(mod)) different generators in total
def generator(mod):
	g=2
	if mod == 2:
		return 1
	elif mod == 4:
		return 3
	elif len(factorize(mod))>1:
		prime = factorize(mod)[1]
		useful_gen = generator(prime)
		t=0
		while (useful_gen+prime*t)**(prime-1)%prime**2 == 1:
			t+=1
		return useful_gen+prime*t	
	else:
		while g**int((mod-1)/2)%mod != mod-1:
			g+=1
		return g

# !generatos exist only for such modules: 2, 4, p^a, 2*p^a; where p is a prime		
def is_generator(num, mod):
	if len(factorize(mod))>1:
		prime = factorize(mod)[1]
		return num**(prime-1)%prime**2 != 1
	else:
		return num**int((mod-1)/2)%mod == mod-1

# Morrison-Brilhard factorization of n
def morr_br(n):
	if n < 1:
		print("error: input number less then 1")
		return None
	if is_prime(n):
		print("error: input number is prime")
		return None
	if sqrt(n).is_integer():
		print(n, "is square of", int(sqrt(n)))
		return int(sqrt(n))
	# filling column [-1]
	a = [None]
	p = [1]
	p2 = [1]
	# filling column [0]
	v = 1
	a.append(floor(sqrt(n)))
	u = a[-1]
	p.append(a[-1])
	p2.append((p[-1] ** 2) % n)
	# creates factor base table
	flag = True
	iterat = 0
	while flag:
		# if iterat > 8:
			# break
		iterat += 1
		# filling remaining columns
		v = (n - (u ** 2)) / v
		a.append(floor((sqrt(n) + u) / v))
		u = a[-1] * v - u
		p.append((a[-1] * p[-1] + p[-2]) % n)
		p2.append((p[-1] ** 2) % n)
		# using Absolutely-least residues
		for item in p2:
			if item > floor(n / 2):
				p2[p2.index(item)] -= n
		# fact - prime: factorization
		fact = {}
		for item in p2[1:]:
			tmp = factorize(abs(item))
			if item < 0:
				tmp.append(-1)
			fact[item] = Counter(tmp)
		# defines the length of combination
		for i in range(2, len(fact) + 1):
			combinations = itertools.combinations(p2[1:], i)
			res = None
			for comb in combinations:
				if p2[-1] in comb:
					# currently used members of factorization base
					curr_fact = {key: fact[key] for key in comb}
					# all primes of factoriztion base
					primes = curr_fact[comb[0]]
					# every member has the same fact base curr_fact
					for key, value in curr_fact.items():
						for item in value:
							if not item in primes:
								primes[item] = 0
					for key, value in curr_fact.items():
						for item in primes:
							if not item in value:
								value[item] = 0
					# res_fact is the summ of curr_fact
					res_fact = {}
					for item in primes:
						res_fact[item] = 0
						for key, value in curr_fact.items():
							res_fact[item] += value[item]
						if res_fact[item] % 2 != 0 and res_fact[item] > 0:
							res_fact = {}
							break
					if res_fact != {}:
						t = 1
						for key in curr_fact.keys():
							t *= p[p2.index(key)]
						t = t % n
						s = 1
						for key, value in res_fact.items():
							s *= key ** (value // 2)
						s = s % n
						res = gcd(abs(t - s), n)
						if res == 1 or res % n == 0:
							res_fact = {}
							curr_fact = {}
							primes = []
							continue
						# cleaning 0-values
						res_fact = {key: value for key, value in res_fact.items() if value != 0}
						# returns combination of p (not p^2)
						res_comb = [p[p2.index(item)] for item in comb]
						print("iterations:", iterat)
						print("a:", a)
						print("p:", p)
						print("p2:", p2)
						print("res_fact:", res_fact)
						print("combination:", res_comb)
						print("curr_fact", curr_fact)
						print("t:", t)
						print("s:", s)
						print("res:", res)
						flag = False
						return res
					res_fact = {}
					curr_fact = {}
					primes = []
				combinations = []
# 63967
# 6
# 27

# Ferma factoriztion of n
def ferma(n):
	x = floor(sqrt(n))
	print("x: ", x)
	if x ** 2 == n:
		print(n, "is square of", x)
		return x
	i = 0
	while True:
		print("iteration:", i)
		x += 1
		print("x:", x)
		if x == ((n + 1) / 2):
			print(n, "is prime")
			return None
		else:
			z = (x ** 2) - n
			print("z:", z)
		y = floor(sqrt(z))
		print("y:", y)
		print(y)
		if y ** 2 == z:
			print(n, "=", x + y, "*", x - y)
			return x + y, x - y
		i += 1
# 6
# 17878
# 18178
#ferma(18178)
