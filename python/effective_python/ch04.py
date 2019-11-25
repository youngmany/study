from urllib.parse import parse_qs

# 간결한 문법으로 많은 로직을 표현식 한 줄로 쉽게 작성 할 수 있음.
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

# print(repr(my_values))
print(my_values)

opacity1 = my_values.get('opacity')
print(opacity1)

# 빈 문자열, 빈 리스트, 0을 모두 암시적으로 False로 평가하는 점을 활용한 예제
# 첫 번째 서브 표현식이 False일 때 or 연산자 뒤에 오는 서브 표현식을 평가한 값이 된다.
red = my_values.get('red', [''])[0] or 0 # 리스트 '5' 값이 있음 암시적으로 True
green = my_values.get('green', [''])[0] or 0 # 딕셔너리 자체에 변수는 있고 안에 빈 값 빈 문자열 (값이 없음) False
opacity = my_values.get('opacity', [''])[0] or 0 # 딕셔너리에 아예 값이 없음 원래는 None, But 두번째 인수 [''] 반환  green과 같은 동작
print('Red: %r' % red)
print('Green: %r' % green)
print('Opacity: %r' % opacity)


# 형변환 한다면 아래와 같이 사용 가능
red_1 = int(my_values.get('red', [''])[0] or 0)
print(red_1)

# 위의 코드를 삼항 표현식 적용
# red_2 = my_values.get('red', [''])
red_2 = my_values.get('opacity', [''])
red_2 = int(red_2[0]) if red_2[0] else 0
print(red_2)

# 삼항식을 펼치면 아래와 같음
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

# 반복해서 사용해야 하므로 아래와 같은 헬퍼 함수로 만들자
def get_first_int(values, key, default=0):
    found = my_values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')


"""
표현식이 복잡해지면 작은 조각으로 분할하고 로직을 헬퍼 함수로 옮기는 방안을 고려해야함.
짧은 코드 보단 가독성을 생각하자.

같은 로직을 반복해야한다면 헬퍼 함수를 쓰자
"""