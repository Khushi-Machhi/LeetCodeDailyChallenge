 # 2485. Find the Pivot Integer

    def pivotInteger(n):
        if n==1:
            return 1
        sum=n*(n+1)//2
        for i in range(n//2,n):
            s1=i*(i+1)//2
            s2=sum-s1+i
            if s1==s2:
                return i
        else:
            return -1
    pivotInteger(8)
