def solution(l) :
    lstTrip = []
    lstTemp = []
    l.sort()
    count = int(0)
    count = int(0)
    i = int(0)
    length = len(l)
    for i in range(length-2) :
        for j in range(i+1, length) :
            if l[j]%l[i] == 0 :
                for k in range(j+1, length) :
                    if l[k]%l[j] == 0 :
                        lstTrip.append([l[i], l[j], l[k]])
                        count = count+1
    print('\n Initial Count : ' count)
    count = 0
    for subLst in lstTrip 
        if subLst not in lstTemp :
            lstTemp.append(subLst)
            count = count+1
    print('\n lsTrip : ', lstTrip)
    print('\n lsTemp : ', lstTemp)  
    return count

print('\n count : ', solution([1, 2, 3, 4, 5, 5, 6, 7, 6, 5, 4, 6, 5]), '\n')
