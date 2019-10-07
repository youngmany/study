
# *args **kwargs
# *args 가변 Tuple
# **kwargs 가변 Dic
def test_func(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

test_func(1, 2)

# 중첩함수 (클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)

    func_in_func(200)

nested_func(100)

# 데코레이터

# hint

# lambda : 메모리 절약, 가독성(?), 코드 간결
# 함수는 객체 생성 -> 메모리 할당
# 람다는 즉시 실행 

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)
print(type(var_func))

lambda_mul_10 = lambda num: num * 10

def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda num: num * 100))