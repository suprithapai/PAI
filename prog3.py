# Python3 program to Find elements of a 
# list by indices present in another list

def findElements(lst1, lst2):
	return [lst1[i] for i in lst2]
			
# Driver code
lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
print(findElements(lst1, lst2))
