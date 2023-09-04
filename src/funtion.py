# def square(Length,width):
#     return(Length*width)
    
# sq = square(2,3)
# print(sq)

def addition(*n):
    sum = 0
    d = []
    for num in n :
        sum += num
        Num = str(num).split('.')
        print('Num', Num)
        dec = len(Num[1])
        d.append(dec)
        print('dec',dec)
    min_d = min(d)
    print(min_d)
    print('sum', sum)
    return round(sum, min_d)
    # return sum
    
sum = addition(1.45,12.3412)
print(sum)

# def info(**kwargs):
#     for k,v in kwargs.items():
#         print(k, ':', v)
# info(name = 'Cat', age = '3', color = 'white')



# sub = lambda n,m: n - m    
# print(sub(6,3))

# lst = ['Python','Java','C++','C++', 'C']
# # lst = [3,6,3,23,7,6,9]
# def remove_dup(l):
#     unique = set(l)
#     u = list(unique)
#     u.sort()

#     return u

# print(lst)
# print(remove_dup(lst))


# def type_dt(data):
#     dt = str(type(data))
#     if 'Str' in dt:
#         print('string')
#     elif 'int' in dt:
#         print('interger')
#     elif 'float' in dt:
#         print('floating point number')
#     elif 'complex' in dt:
#         print('complex number')
# print(type(23))   
# print(type("23"))  
# print(type(23.12))
# print (type_dt(23))

