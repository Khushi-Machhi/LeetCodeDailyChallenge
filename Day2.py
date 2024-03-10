#2540. Minimum Common Value

def getCommon(self,nums1,nums2):
  nums1_set=set(nums1)
  for i in nums2:
    if i in nums1_set:
      return i
  return -1
  
getCommon([1,4,7,9],[3,7,8])
