lst = [2,7,11,13]
# for i in range(len(lst)):
#     for j in range(i):
#         if lst[i] + lst[j] == 9:
#             print(j, i)        
#             print(lst[j], lst[i]) 

# # cách 2
dict = {}
tong = 6
for i in range(len(lst)):
    if ((tong - lst[i]) in dict): # just key
        print([dict[tong - lst[i]], i])
        break
    dict[lst[i]] = i


    # 2 : 0
    # key : value
    # từ : giải nghĩa
