import random,math,pylab

#VOlume of a sphere of dim dimension
def V_sph(dim):
    return math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0)


d_max = 20
#d = 1 corresponds to V_sph(1) = 2
d = range(d_max + 1)

delta = 0.1
power = range(8)
n_runs = 10

for k in range(len(power)):
	n_trials = 10**power[k]
	V_dmax_sph   = 0.0
	V_dmax_2_sph = 0.0
	for j in range(n_runs):
		Q_list = []
		for dim in d:
			#For 0 and 1 
			if dim < 2: 
				V_sph_1 = 2
			else:
				dimensions = dim - 1
				#Coordinates vector
				x = []
				#Initialize to zero
				x = [0.0]*dimensions
				Qd = 0.0
				old_radius_square = 0.0
				n_hits = 0
				for i in range(n_trials):
					#Instead of modifying all components of x at a time, as we did in markov_pi.py,
					#modify only one component at each iteration i (with i=0, 1, 2,...., n_trials).
					k = random.randint(0, dimensions - 1)
					x_old_k = x[k]
					x_new_k = x_old_k + random.uniform(-delta, delta)
					new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
				
				    #del_x, del_y,del_z = random.uniform(-delta, delta), random.uniform(-delta, delta),random.uniform(-delta, delta)
					alpha = random.uniform(-1.0,1.0)
				    #Inside (d-1) unit sphere?
				    #I dont have to rest x[dimensions-1]**2 because I never sum it.
					if new_radius_square < 1.0:
						x[k] = x_new_k
						old_radius_square = new_radius_square
					if old_radius_square+alpha**2 < 1.0: 
						n_hits += 1
					#print k,new_radius_square,x[dimensions-1],new_radius_square+x[dimensions-1]**2,math.sqrt(new_radius_square+x[dimensions-1]**2)
					
				#print 4.0 * n_hits / float(n_trials)
				#Updated once for each j (nruns)
				#print 2.0*n_hits/float(n_trials)
				Q_list.append (2.0*n_hits/float(n_trials) )
				if (dim == d_max):
					inter = V_sph_1*reduce(lambda x,y:x*y,Q_list)
					V_dmax_sph   += inter
					V_dmax_2_sph += inter*inter

	Vave  = V_dmax_sph/float(n_runs)
	Vave2 = V_dmax_2_sph/float(n_runs)
	Vteo  = V_sph(d_max)
	error = math.sqrt( Vave2 - Vave**2)/math.sqrt(n_runs)
	difference = Vave - Vteo
	print 'ntrials =',n_trials,'Volume V(',d_max,') ave = ',Vave,'Volume V(',d_max,') teo = ',Vteo,'Error = ',error,'Difference = ',difference
