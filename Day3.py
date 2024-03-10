#349.Intersection of Two arrays

def intersection(self, nums1, nums2):
        resultList=list()
        nums1.sort()
        nums2.sort()
        i,j=0,0
        while (i<len(nums1) and j<len(nums2)):
            if nums1[i]>nums2[j]:
                j+=1
            else:
                if nums1[i]<nums2[j]:
                    i+=1
                else:
                    resultList.append(nums1[i])
                    i+=1
                    j+=1
        resultSet=set(resultList)
        final=list(resultSet)
        return final
