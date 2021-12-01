
def adder (num):
    num = num + 10
    return num

list1 = [x for x in range(10)]
print(list1)

list1 = list(map(adder, list1))
print(list1)


x = int(input())
y = int(input())
z = int(input())
n = int(input())


new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

#same as the following
#for i in range(x+1):
#    for j in range(y+1):
#        for k in range(z+1):
#            new_list.append([i,j,k])



print(new_list)