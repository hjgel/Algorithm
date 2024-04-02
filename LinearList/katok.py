## 함수 선언 부분
def find_and_insert_data(friend, k_count):
    findPos = -1 
    for i in range(len(katok)): # 0부터 katok의 길이 전만큼
        pair = katok[i]  # pair을 카톡에 있는 친구로 바꿈. 
        if k_count >= pair[1]: # pair[1]번 인덱스가 k_count보다 크다면 변경.
            findPos = i # findPos를 i(인덱스)로 바꿔줌. 
            break
    if findPos == -1: # 만약 findPos가 -1이면
        findPos = len(katok) # findPos를 katok의 길이로 변경
    
    insert_data(findPos, (friend, k_count)) # 하고 넘겨줌. 
    
def insert_data(position, friend):
    if position < 0 or position > len(katok): # 인덱스 범위를 넘기면 돌음
        print("데이터를 삽입할 범위를 지났습니다.")
        return
    
    katok.append(None) # katok의 인덱스를 넓혀줌 
    kLen = len(katok) 

    for i in range(kLen -1, position, -1): # 마지막 인덱스부터 position이 되기 전까지 돌림
        katok[i] = katok[i-1] # 바꿔주는 작업
        katok[i-1] = None # 바꿔주는 작업 
    
    katok[position] = friend

## 전역 변수 선언 부분
katok = [('다현', 200),('정연', 150),('쯔위', 90),('사나', 20),('지효', 15)]

## 메인 코드 부분
if __name__ == "__main__":

    while True:
        data = input("추가할 친구-->")
        count = int(input("카톡 횟수-->"))
        find_and_insert_data(data, count)  # 친구랑, 횟수를 넘겨줌 
        print(katok)