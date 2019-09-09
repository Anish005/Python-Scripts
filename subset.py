#create a class subset
class subset:
   #Method sort() is used to pass an empty list and sorted list is taken from the user to findsubset
    def sort(self, s1):  
        return self.findsubset([], sorted(s1))  
   #Method findsubset() is used to compute all the possible subsets of the list
    def findsubset(self, curr, s1):  
        if s1:  
            return self.findsubset(curr, s1[1:]) + self.findsubset(curr + [s1[0]], s1[1:])  
        return [curr]  
a=[]
n=int(input("Enter number of elements of list: "))
for i in range(0,n):
    b=int(input("Enter element: "))
    a.append(b)
print("Subsets: ")
print(subset().sort(a))
