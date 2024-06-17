shopping_list= ["milk","bread","butter","poha"]
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list=["milk","bread","butter","poha","anitha"]
shopping_list.append("hello")
shopping_list.insert(2,"jam")
shopping_list.extend(["chips","salt"])
shopping_list.remove("hello")
shopping_list.pop()
print(shopping_list.index("milk"))
shopping_list.reverse()
shopping_list.sort()
print(shopping_list)
print(shopping_list.index("milk"))
shopping_list[0]="RK"
print(shopping_list)