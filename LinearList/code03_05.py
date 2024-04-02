## 함수 선언 부분 ## 
def print_poly(p_x) :
	term = len(p_x) - 1	# 최고차항 숫자 = 배열길이-1
	poly_Str = "P(x) = "
	
	for i in range(len(px)) :
		coef = p_x[i]	# 계수
		
		if coef == 0:
			term = term - 1
			continue 
		
		if coef >= 0 and i != 0:		
			poly_Str += "+"	
		poly_Str += f"{coef}x^{term} "
		term -= 1

	return poly_Str


def calc_Poly(x_Val, p_x) :
	ret_Value = 0
	term = len(p_x) - 1	# 최고차항 숫자 = 배열길이-1
	
	for i in range(len(px)) :
		coef = p_x[i]	# 계수
		ret_Value += coef * x_Val ** term
		term -= 1

	return ret_Value


## 전역 변수 선언 부분 ## 
px = [7, -4, 0, 5]			# = 7x^3 -4x^2 +0x^1 +5x^0 
# px = [-7, 0, 3]

## 메인 코드 부분 ## 
if __name__ == "__main__" :

	p_str = print_poly(px)
	print(p_str)

	xValue = int(input("X 값-->"))

	pxValue = calc_Poly(xValue, px)
	print(pxValue)

	
