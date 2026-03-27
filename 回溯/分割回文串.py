res = []
def func(num,i,k):
    if k == length - 1:
        lst = num.split(",")
        for i in lst:
            if i != i[::-1]:
                return
        res.append(lst)
        return
    func(num[:i+1] + "," + num[i+1:],i + 2,k + 1)
    func(num,i + 1,k + 1)

nums = input()
length = len(nums)
func(nums,0,0)
output = '[[' + '], ['.join([', '.join(sublist) for sublist in res]) + ']]'
print(output)
