def moves(a):
    odd = 0
    even = 0
    numList = len(a)
    half = numList // 2 # 몫 구하기

    if numList % 2: # odd
        for i in range(half):
            if a[i] % 2:
                odd += 1
            else:
                even += 1

        if odd is even:
            return odd+1

        return odd
    
    else:   # even
        for i in range(half, numList):
            if a[i] % 2:
                odd += 1
            else:
                even += 1
                
        return even