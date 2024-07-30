# *args es una tupla
def add(*nums):
    sum = 0
    nums = list(nums)
    nums[0] = 0
    for i in nums:
        sum += i
    return sum

#print(add(1,2,3,3))

# **kwargs a diccionario
# kwargs = key word arguments

def hello(**nombres):
    print('Hola :D', end=' ')
    for key, value in nombres.items():
        print(value, end=' ')

hello(title='Mr', h2='Bro', h1='Caba', h3='Fire')