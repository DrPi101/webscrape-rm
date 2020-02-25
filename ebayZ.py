def kw():
        with open ("ebay_search.txt", "r") as fn:
            lines = fn.readlines()
   
        for line in lines:
         v = (line.split(","))
        
         print(v[0])


print(kw())
	

