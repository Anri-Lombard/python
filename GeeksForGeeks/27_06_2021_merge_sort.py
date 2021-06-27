def merge ( list1, list2 ):
   """Merge 2 sorted lists."""
   new_list = []
   while len(list1)>0 and len(list2)>0:
      if list1[0] < list2[0]:
         new_list.append (list1[0])
         del list1[0]
      else:
         new_list.append (list2[0])
         del list2[0]
   return new_list + list1 + list2

def merge_sort ( values ):
   """Sort values using merge sort algorithm."""
   if len(values)>1:
      sorted1 = merge_sort (values[:len(values)//2])
      sorted2 = merge_sort (values[len(values)//2:])
      return merge (sorted1, sorted2)
   else: return values
                
        