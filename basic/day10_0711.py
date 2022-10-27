txt = "Hello, welcome to my world."
e=[]

for i in range(len(txt)):
    e.append(txt.find("e",len(txt[i])))
print(e)


# txt = "Hello, welcome to my world."
#
# eList = []
# chkIdx = 0
# while chkIdx >= 0:
#     chkIdx = txt.find("e",chkIdx)
#     if chkIdx == -1:
#         break
#     eList.append(chkIdx)
#     chkIdx += 1
#
# print(eList)
#
# print(f"")
