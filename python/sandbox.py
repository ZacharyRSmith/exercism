def danny_bub2(list):
    for i in range(len(list)//2):
        # 0 - 
        for j in range(i, (len(list) - 1) - i): 
            if list[j] > list[j + 1]:  # if lt > rt, swap
                list[j], list[j + 1] = list[j + 1], list[j]      
        for k in range((len(list) - 2) - i, i, -1): 
            if list[k] < list[k - 1]: 
                list[k], list[k - 1] = list[k - 1], list[k]
    print(list)
danny_bub2([2,3,1])