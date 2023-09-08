import common
import math #note, for this lab only, your are allowed to import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()

	voteing = common.init_space(2000, 2000)
	
	for y in range(common.constants.WIDTH):
		for x in range(common.constants.HEIGHT):
			if image[y][x] == 0:
				m = -10.0
				while m < 10.0:
					b = -m*x+y
					shifted_m = int((m + 10) * 100)
					if b >= -1000 and b < 1000:
						voteing[shifted_m][int(b) + 1000] += 1
					m += 0.01

	m_max = 0
	b_max = 0
	v_max = 0
	
	for m in range(2000):
		for b in range(2000):
			if voteing[m][b] > v_max:
				v_max = voteing[m][b]
				m_max = m/100.0 - 10.0
				b_max = b - 1000
	
	line.m= m_max
	line.b= b_max
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	num_circles = 0

	voteing = common.init_space(200, 200)

	for y in range(common.constants.WIDTH):
		for x in range(common.constants.HEIGHT):
			if image[y][x] == 0:
				for a in range(200):
					if (x-a)**2 <= 900:
						b = y - math.sqrt(900 - (x-a)**2)
						voteing[a][int(b)] += 1


	for a in range(200):
		for b in range(200):
			if voteing[a][b] > 50:
				num_circles+=1

	return num_circles
				