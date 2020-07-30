#__author:jack
#date 2019-12-09 17:55

#生成器

result = (i for i in range(10))
# print(result) #<generator object <genexpr> at 0x1026e94d0>

print(result.__next__())
print(next(result))
print("===========")
for i in result:
    print(i)

#StopIteration
#print(next(result))

def fun():
    print("1")
    yield "1"
    print("2")
    yield "2"
    print("3")
    yield "3"

print(fun) #<function fun at 0x1007a8e60>
print(fun()) #<generator object fun at 0x108c65550>

for i in fun():
    print(i)

