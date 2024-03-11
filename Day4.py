# 791. Custom Sort String
def customSortString(order, s):
  # list_s = list(s)
  # r = ""
  # for i in order:
  #     for j in list_s:
  #         if i in list_s:
  #             r=r+i
  #             list_s.remove(i)   
  # for i in list_s:
  #     r=r+i
  # return r

  list_s = list(s)
  list_o = list(order)
  r = list()
  for i in list_o:
      for j in list_s:
          if i in list_s:
              r.append(i)
              list_s.remove(i)   
  for i in list_s:
    r.append(i)
  return ("".join(r))

        
  # final = ""
  # for i in order:
  #     count = s.count(i) 
  #     final += (count * i) 
  # for i in s: 
  #     if i not in order:
  #         final += i
  # return final
  customSortString("cba","abcd" )
