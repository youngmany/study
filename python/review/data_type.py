# ** 제곱
# // 몫
# complex 복소수
# abs 절대값

# 숫자, 데이터 타입
n, m = divmod(100, 8)
print(n, m)

# 문자
raw_str = r'C:\A\B\C'
print(raw_str)

# Multi Line
a = \
    """
    Young
    Many
    K_K
    """
print(a)

str_t = "abcdefg"

print('a' in str_t)
print('z' not in str_t)

# 문자열 함수
a = 'apple'
b = 'orange'
c = 'adasd-ffadasd-131233'

print(a.islower())
print(a.endswith('e'))
print(a.capitalize())
print(c.replace("-", ""))
print(list(reversed(b)))

a = 'youngmany'

print(a[0:4:2])
print(a[1:-2])
print(a[::-1])

# 리스트 (순서 O 중복 O 수정 O 삭제 O)
y = [5, 2, 3, 1, 4]
 
y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2, 12)
print(y)

y.remove(2)
# del y[2]

y.pop()

add = [11, 22]

# y.extend(add) 뒤에 붙이기
# y.append(add) 리스트 끝에 삽입 

# 튜플 (순서 O 중복 O 수정 X 삭제 X)

# 딕셔너리 (순서 X 중복 X 수정 O 삭제 O)

a = {
    'name': 'Youngmany',
    'age': 1
}

print(a['name'])
print(a.get('name'))
print(a.get('age'))
# print(a['addr'])
print(a.get('addr')) # None

print(a.keys())
print(list(a.keys()))
print(a.values())
print(a.items())

# 집합 (순서 X 중복 X 추가 O 제거 O)

m_set = set([1, 4, 5, 6, 6])
print(m_set)

m_list = tuple(m_set)
print(m_list)
m_tuple = tuple(m_set)
print(m_tuple)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 조건
# 산술 > 관계 > 논리

# 반복 시퀀스 있는 자료형은 다 가능
# 문자열 리스트 튜플 집합 사전
# iterable return function: range, reversed, enumerate, filter, map, zip (정리)

value_list = ['a', 'b', 'c']
for i, v in enumerate(value_list):
    print(i, v)
