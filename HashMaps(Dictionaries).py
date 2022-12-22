# Hashtables uses hashfuctions to generate the position to insert a value.
class HashTable:
    def __init__(self):
      self.Max=100
      self.arr=[[] for i in range(self.Max)]

    def get_hash(self,key):
        ascii_num=0
        for char in key:
            ascii_num+=ord(char)
        return ascii_num % 100

      # standard operators
    def __setitem__(self, key, value):
        ascii_num=self.get_hash(key)
        found=False

        # check to update value if a key matches.
        for idx,element in enumerate(self.arr[ascii_num]):
            if len(element)==2 and element[0]==key:
                self.arr[ascii_num][idx]=(key,value)
                found=True
                break
        if not found:
            # insert if the key is unique
            self.arr[ascii_num].append((key,value))




    def __getitem__(self, key):
        ascii_num = self.get_hash(key)
        return self.arr[ascii_num]

    def __delitem__(self, key):
        ascii_num = self.get_hash(key)
        self.arr[ascii_num]=None



if __name__=='__main__':
    ht=HashTable()
    ht["march 9"]=9
    ht["march 25"]=459
    ht["march 6"]=78
    print(ht.arr)





