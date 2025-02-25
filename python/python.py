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

# 키만보아서 배열로 출력 
print(dic.keys())

# keys만 포문을 통해 출력 
dic = {'name': 'kim', 'age':30, 'phone':'010-2215-6095'}
for k in dic.keys():
    print(k)
#벨류만 뽑는방법
for k in dic.values():
    print(k) 
print(dic)
# 리스트가 생기고 각각에 항목마다 튜플에 넣어서 출력해준다
print(dic.items())

# 키와 벨류 모두 지우기
dic.clear()
print(dic)

# 키값에 맞는 벨류값 출력 
dic = {'name': 'kim', 'age':30, 'phone':'010-2215-6095'}
# 대괄호 사용시 키에 맞는값이 없으면 값이 없다고 에러가뜬다
print(dic['name'])
# get으로 가져오게 되면 값이 없다고 none만 출력 
# 두번째 전달인자값은 값이 없을때 출력되는 값을 넣을수있음
print(dic.get('ㅋㅋㅋㅋ',"값이없습니다"))

# 해당 딕셔너리 변수에 name이라는 키가 있는지 확인
print('name' in dic)

# 집합으로 묶은뒤 출력 set 타입
s1 = set([1,5,3,2])
print(s1) 
print(type(s1)) 
# 문자열을 집합에 넣으면 중복된글자 제거, 순서 뒤죽박죽인 
# 각문자마다 문자열 리스트로 출력 
s2 = set('Hellow')
print(s2)
# 집합자료형은 순서가 뒤죽박죽이기때문에 인덱싱등 사용불가 
# 그래서 list로 형변환하여 사용  
print('-'*50)
# print(s1[1]) 오류남
print(list(s1)[3])
print('-'*50)

# 2025-02-25
# 집합 자료형에서 교집합 값 구하기 
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2)
# 교집합 구하는 메소드
print(s1.intersection(s2))

# 집합 자료형에서 합집합 값 구하기 
# 모든값 + 중복값 삭제
print(s1|s2)
# 합집합 구하는 메소드
print(s1.union(s2))

# 집합 자료형에서 차집합 값 구하기 
# s1에서 중복값 제거후 남은것만
print(s1-s2)
print(s2-s1)
# 차집합 구하는 메소드
print(s2.difference(s1))

 
# 집합에 값1개추가
s1.add(7)
print(s1)
# 집합에 여러개의 값추가 
s1.update([8,9,10])
print(s1)
# 값 삭제
s1.remove(10)
print(s1)

# 리스트에서 중복값 삭제하고싶을떄
li = [1,2,3,4,4,4,4,5,6,7,7,8,9,8,9,]
s1 = set(li)
print(s1)
li = list(s1)
print(li)
print(type(li))

# 불자료형 --------------------------------------
a = True
b = False
print(type(a),type(b))
a = 1 == 2
print(a)

a = [1,2,3,4,5,6]
while a:
    print(a)
    a.pop()

print("-------------------------------")  
if [1,2,3]:
    print("참")
else:
    print("거짓")
a = bool([1,2,3])
print(a)

# 변수 (주소값) ------------------
# 얕은복사
b = a
print(id(a))
print(id(b))
print(a is b)

a = [1,2,3]
b = [4,5,6]
print(id(a))
print(id(b))

# 깊은복사 
a = [1,2,3]
b = a[:]
print(id(a))
print(id(b))


 