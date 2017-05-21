from fractions import gcd, Fraction

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
	
	if is_prime(p):
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
		print("Given module is not prime")
		
# !notice that this function finds only the first (minimal) generator		
def generator(mod):
	g=2
	while g**int((mod-1)/2)%mod != mod-1:
		g+=1
	return g	
		
def is_generator(num, mod):
	return num**int((mod-1)/2)%mod == mod-1
		
