#list
list = [60,80,90,98]
print(list)


#change list
list = [60,80,90,98]
list[1] =89 
print(list)

#add new item
list = [60,80,90,98]
list.append("55")
print(list)
print(len(list))


#program to sum all items 
a = [60,80,90,98]
sum(a)
print(sum(a))


list_html =[60,70,80,90]
list_python =[65,79,80,99]
def common_item(list_html,list_python):
    result = True
    for value in list_html:
        for item in list_python:
            if value == item:
                result = True
                return result
print(common_item(list_html,list_python))
