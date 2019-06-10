def search(nums,target):
    for i,v in enumerate(nums):
        print(i,v)
        if v==target:
            print('pp',i)
            break
        elif v>target:
            print(i)
            break
        else:
            print(len(nums)-1)
            break

a = search([1,3,5,6],5)

print(a)