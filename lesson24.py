# exam-18.11.2024
# 1 - duris-1
# a=[1,2]
# print(a)
# # 2 - duris-1
# a=[]
# a.insert(0,'you')
# print(a)
# # 3-duris 
# a=[1,3,5]
# a.insert(3,'mee')
# print(a)
# 4 - duris -1
# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# a.pop(5)
# print(a)
# a.remove(1)
# print(a)
# 5-duris -1
# a=[]
# for i in range(1,11):
#     print(i) - iterator
# b=[i for i in range(1,21) ]
# print(b) - generator
# 6-duris -1
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# new=[x for x in a if x%2==1]
# print(new)
# 7-duris -1 
# a=[1,2,3,4,5]
# plus=sum(a)
# print('qosindisi',plus)
# 8-duris -1
# a=[1,2,2,4,5,5,7,8,8]
# print(set(a))
# b=[i for i in a if i%2!=0]
# print(b) 
# 9-duris-1
# a=(1,2,3,4,5,6,7,8)
# print(a)
# 10-1
# a=(1,3,5,3,7)
# b=a.count(3)
# print(b)
# 11-1
# a={
#     'a':1,
#     'b':2,
#     'c':3
# }
# print(a)
# 12-1
# a={
#     0:'world',
#     1:'hello'
# }
# b=a.keys()
# print(b)
# 13-1
# a={1,2,3,4,5,6,7,8}
# a.add('len')
# print(a)
#14-1
# a={1,1,2,3,3,4,5,5}
# b={6,7,7,8,9,9,8}
# a.intersection(b)
# print(a)
# b.difference(a)
# print(b)
# 15-1
# a={1,2,3}
# b={4,5,6}
# c={1,2,7}
# a.difference(b)
# print(a)
# b.difference(c)
# print(b)
# 16-1
# a=[1,2,3,4]
# b=(5,6,7)
# c={8,9,10}
# d=(list(b))
# e=(list(c))
# f=(a+d+e)
# print(f)
# 17-1
# a={
#     'alllaniyaz':2010,
#     'dawletyar':2008,
#     'gulshiyra':2008
# }
# for name ,age in a.items():
    # print(f'name:{name},age-{age}')
# 18 -1
# school={
#     'maykalxoz':42,
#     'raddomda':31,
#     'bozawida':51
# }
# for user, info in school.items():
#     print(f'User:{user}')
#     for key, value in school.items():
#         print(f'{key}:{value}')
#     print()
# #19-0,5
# numbers = [5,2,3,1,6,8,7,[[0,2,[21,'hello',12],3]]]
# b=numbers[7][0][2][1]
# print(b)
# 20
# nums=[10,2,1,5,3,4,7,9,8,6,7,7,7]
# a=set(nums)
# b=list(a)
# print(b)
# b.sort(reverse=True)
# print(b)