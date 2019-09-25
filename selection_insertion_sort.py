class s_i_sort:
        def __init__(self,list):
                self.list = list
                
        def selection_sort(self):
                length = len(self.list)
                for i in range(length):
                        for j in range(i+1,length,1):
                                if self.list[i] > self.list[j]:
                                        self.list[i],self.list[j] = self.list[j],self.list[i]
                                else:
                                        continue
                        print("The sorted list is:", self.list)
                        
        def insertion_sort(self):
                length = len(self.list)
                for i in range(1,length,1):
                        key = self.list[i]
                        j = i - 1
                        while j >= 0 and self.list[j] > key:
                                self.list[j],self.list[j+1] = self.list[j+1], self.list[j]
                                j = j - 1
                        self.list[j+1] = key
                        print("The sorted list is:", self.list)

                

list = [14,46,43,27,57,41,45,21,70]
sort = s_i_sort(list)
sort.selection_sort()
sort.insertion_sort()
