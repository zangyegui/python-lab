#需要改写的片段
# result = []
# for x in [1,2,3,4,5,6]:
#     if x % 2 == 0:
#         result.append(x)
result = [x for x in range(1,7) if x % 2 == 0]
print(result)