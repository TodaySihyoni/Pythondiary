# 리스트 내포
#for 내포

nums = [i for i in range(10)]
print(nums)

nums2 = [300, 2000, 1000]
double_nums  = [i * 2.3 for i in nums2]
print(double_nums)

# if 사용

nums3 = [i for i in range(20) if i % 2 == 0 ]
print(nums3)

nums4 = [300, 100, 200, 900, 399]
double_nums2 = [i * 2 for i in nums4 if i >= 240 ]
print(double_nums2)