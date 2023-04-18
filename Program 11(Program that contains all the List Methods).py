name = ['rohan', 'ayush', 'raju']
print("This is the default list:", name)

#Appending the list using append()
name.append('venu')
print("The list after appending is:",name)



#Inserting a element at specified position
name.insert(2,"Hemanth")
print("The list after inserting a element",name)



#Extending the list using extend method
data=["Yogi","Alex"]
name.extend(data)
print("The list after extending becomes", name)


#Length method
print("The length of the list is", len(name))

#Reverse the list
num=[1,2,1,1,3,4,5]
num.reverse()
print("This is the reversed list:",num )


#Count Method
print("This is the list:",num)
a=int(input("Enter the number you want to count:"))
count=num.count(a)
print("The number you entered ",a,"occurs",count,"times in the list")
#Pop method
print("This is list before popping:",num)
popped_num=num.pop(2)
print("The popped num from list is:", popped_num)
print("The list after pop is:", num)


#remove method
b=int(input("Enter the number you want to remove from list:"))
removed_num=num.remove(b)
print("The list after removing is:", num)


#Sort method
print("List before sorting is:", num)
num.sort()
print("List after sorting:",num)

#Clear Method
print("List before clearing:", num)
num.clear()
print("List after clearing:", num)



