import unittestclass 
MyTestCase(unittest.TestCase):
  def test_something(self):        
    self.assertEqual(True, False)    
  def test_Array(self):        
    array=range(1,10,1) # range(x:int, y:int=0,step:int =1)        
    print()        
    print("use range(1,10,1) set array =%s" %array)        
    print("array[:-2] = %s"%array[:-2])        
    print("array[::-2] =%s"%array[::-2])        
    print("array[::2]=%s"%array[::2])        
    print("array[9::-2] =%s" % array[9::-2])        
    print("array[8::-2] =%s" % array[8::-2])        
    print("array[7::-2] =%s" % array[7::-2])        
    print("array[7:0:-2] =%s" % array[7:0:-2])        
    print("array[7:1:-2] =%s" % array[7:1:-2])        
    arrTemp2=[x for x in range(1,10)]        
    print("use arrTemp2=[x for x in range(1,10)] set arrTemp2 =%s"% arrTemp2)        
    arrTemp3 = [[x for x in range(1, 5)] for y in range(1,5)]        
    print("use arrTemp3 = [[x for x in range(1, 5)] for y in range(1,5)]")        
    print("arrTemp3 =%s" % arrTemp3)
if __name__ == '__main__':    
  unittest.main()


#-----output--
#array[x:y:z]  x is start, y is end and not include self, z is step, if step>0, searched and displayed from front to back, if step <0: back to front
use range(1,10,1) set array =[1, 2, 3, 4, 5, 6, 7, 8, 9]
array[:-2] = [1, 2, 3, 4, 5, 6, 7]
array[::-2] =[9, 7, 5, 3, 1]
array[::2]=[1, 3, 5, 7, 9]
array[9::-2] =[9, 7, 5, 3, 1]
array[8::-2] =[9, 7, 5, 3, 1]
array[7::-2] =[8, 6, 4, 2]
array[7:0:-2] =[8, 6, 4, 2]

array[7:1:-2] =[8, 6, 4]use arrTemp2=[x for x in range(1,10)] set arrTemp2 =[1, 2, 3, 4, 5, 6, 7, 8, 9]
use arrTemp3 = [[x for x in range(1, 5)] for y in range(1,5)]
arrTemp3 =[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
