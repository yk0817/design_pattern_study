# 参考 
# https://github.com/faif/python-patterns/blob/master/behavioral/iterator.py

def count_to(count):
    array = [1,2,3,4,5]
    for number in array[:count]:
        yield number

count_to_two = lambda: count_to(2)
count_to_five = lambda: count_to(5)

print('count two:')
for number in count_to_two():
    print(number,end= ' ')
    
print('count five:')
for number in count_to_five():
    print(number,end= ' ')
    