# Condition

unitprice = 10
if unitprice < 15 and unitprice > 10:
    dis = 2
elif unitprice <= 10:
    dis = 1
else:
    dis = 5

quantity = 90
total  = unitprice * quantity *(100 - dis)/100
print("Total price is", total)

lst = ['Python','Java','C++']
if 'Python' not in lst:
    lst.append('Python')
elif  'Java' not in lst:
    lst.append('Java')
else:
    lst.append('C')
print(lst)

# while unitprice != 6:
#     print()
#     unitprice -= 1
#     print(unitprice)

# i =0     
# while i < 3:
#     num = int(input('Number:'))
#     if num == 0 :
#         continue
#     if num == 1 :
#         break
#     sq = str(num * num)
#     print ('Square:' + sq)
#     i += 1
# else:
#     print('Done')
    
# for
# lst = ['Python','Java','C++', 5 , 3 ,6]
# for element in lst:
#     if element  == "Python":
#         print(element)
#         continue
#     elif element == 5:
#         break
#     print(element.capitalize) 
    
# for num in range(12,15):
#     for i in [1,2,3]:
#         print(i,num)



        
    
    