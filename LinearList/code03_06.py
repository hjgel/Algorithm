## 함수 선언 부분 ## 
def print_poly(p_x, t_x) :
	# term = len(p_x) - 1	# 최고차항 숫자 = 배열길이-1
	poly_Str = "P(x) = "
	
	for i in range(len(p_x)) :
		coef = p_x[i]	# 계수
		term = t_x[i]   # 지수
		
		# if coef == 0:
		# 	term = term - 1
		# 	continue 
		if coef >= 0 and i != 0:		
			poly_Str += "+"	
		poly_Str += f"{coef}x^{term} "
		term -= 1

	return poly_Str


def calc_Poly(x_Val, p_x, t_x) :
	ret_Value = 0
	# term = len(p_x) - 1	# 최고차항 숫자 = 배열길이-1  
	                       
	for i in range(len(px)) :
		coef = p_x[i]	# 계수
		term = t_x[i]   # 지수
		ret_Value += coef * x_Val ** term
		# term -= 1

	return ret_Value

tx = [4, 2, 0] # exponent
px = [7, -4, 5] # coefficient


## 메인 코드 부분 ## 
if __name__ == "__main__" :

	p_str = print_poly(px, tx)
	print(p_str)

	xValue = int(input("X 값-->"))

	pxValue = calc_Poly(xValue, px, tx)
	print(pxValue)

