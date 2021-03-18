# list1 = [["Mrinmoy","5"],["Manika","8"],[ "Ratan","9"],["Urmila","15"] ]
# dic1 = dict(list1)
# for item in dic1:
#     print(item)
#
# # for item, age in dic1.items():
# #     print(item,"age is",age)

items = [int,float,"Mrinmoy", 5,9,52,654,482,7,6,2]
for item in items:
    if str(item).isnumeric() and item>=6:
      print(item)