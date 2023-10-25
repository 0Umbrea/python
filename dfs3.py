#目标和

def total(nums,target):
    count=0
    def search(i,x):
        nonlocal count
        if i==len(nums):
            if x==target:
                count+=1
        else:
            search(i+1,x+nums[i])
            search(i+1,x-nums[i])
    search(0,0)
    return count

nums=[1,1,1,1,1]
print(total(nums,3))