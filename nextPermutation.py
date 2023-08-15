def NextPerm(nums):
        ptInf=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                ptInf=i
                toSwap=i-1
                break
        if ptInf==0:
            nums=nums.sort()
        else:
            min=nums[ptInf]-nums[toSwap]
            for i in range(ptInf,len(nums)):
                if nums[i]-nums[toSwap]<=min and nums[i]>nums[toSwap]:
                    minPt=i
            nums[toSwap],nums[minPt]=nums[minPt],nums[toSwap]
            print(nums)
            #sort from toSwap to last index
            for i in range(toSwap+1,len(nums)):
                for j in range(toSwap+1,len(nums)-1):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
