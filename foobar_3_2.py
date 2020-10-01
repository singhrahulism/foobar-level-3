# Program
import copy

def case1(funcM1, funcF1) :
    fm1 = copy.deepcopy(funcM1)
    ff1 = copy.deepcopy(funcF1)
    fm1 = fm1+ff1
    return [fm1, ff1]

def case2(funcM2, funcF2) :
    fm2 = copy.deepcopy(funcM2)
    ff2 = copy.deepcopy(funcF2)
    ff2 = ff2+fm2
    return [fm2, ff2]

m = int(input('\n Enter m : '))
f = int(input('\n Enter f : '))

lstTemp = []
lst = [[1, 1]]
flag = int(0)
counter = int(0)

while True :
    flag = 0
    counter = counter+1
    for i in range(len(lst)) :
        lstTemp.append(case2(lst[i][0], lst[i][1]))
        lstTemp.append(case1(lst[i][0], lst[i][1]))
    lst.clear()
    lst = copy.deepcopy(lstTemp)
    lstTemp.clear()
    for element in lst :
        if element == [m,f] :
            flag = 1
            break
    if flag :
        break
    if (m+f) < ((2*counter)+1) :
        flag = 0
        break
if flag :
    print('\n Minimum Generations : ', counter, '\n')
else :
    print('\n Minimum Generations : impossible\n')