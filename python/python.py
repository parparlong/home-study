a = "jpbbu"
print(a.find('p'))

a1 = [1,2,3]
# print("여기부터","hi" / 3)

# 상자의 느낌으로 리스트 순서에 맞춰서 수정가능
a = [1,2,3]
a[2] =  4
print(a)

# 리스트에 있는 값을 삭제할수있다.
del a[1]
print(a)

# 리스트를 더할수도있다.
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 리스트 길이구하기
b = [4,5,6]
print("b의길이",len(b))

# 리스트 곱하기 가능
b = [4,5,6]
print(b * 3)

# 리스트와 문자열 더하기
b = [4,5,6]
print(str(b[2]) + "hi")

# 슬라이싱을 이용하여 2번째부터 삭제가능
a = [1,2,3,4,5]
del a[2:]
print(a)

# 리스트에 값추가
a = [1,2,3,4,5]
a.append(4)
print("여기",a)

#리스트에 값추가  (리스트에 값 형태로 추가)
a.extend([2000,3000,4000])
print("extend :", a)


print("-"*50)
#리스트에 리스트추가 (리스트에 리스트형태로 추가)
a = [1,2,3,4,5]
a.append([4,5])
print("여기",a)


# 리스트 오름차순정렬
a = [20,5,65,78,22]
b = ["a","c","b"]
a.sort()
b.sort()
print(a)
print(b)

# 리스트 내림차순순정렬
a.reverse()
print(a)

# 인덱스반환 해당값에 인덱스번호를 가져옴
a = [20,5,65,78,22,75,75,78,78]
print(a.index(22)) 

# 인덱스 번호에 값 추가 
a.insert(1,400)
print(a)

# 첫번째에 걸리는값 삭제
a.remove(5)
print(a)

# 해당 인덱스 값 삭제 및 출력확인
print(a.pop(2))

# 값 계수 확인
print(a.count(78))

# 형변환
a = [1,2,3,4,5]
b = (6,7,8,9,10)
c = list(b)
d = tuple(a)
print(type(c)) 
b = b + b
print(b) 

# 딕셔너리 키벨류 형태 중괄호 사용
dic = {'name': 'kim', 'age':30, 'phone':'010-2215-6095'}
print(type(dic))
print(dic)
 
#  키와 벨류 추가
dic['추가1'] = '추가됬음'
print(dic)

# 키 벨류 삭제
del dic['age']
print(dic)

# 조회
print(dic['name'])