def twoNumberSum(array, targetSum):
	''' 
	for i in range(len(array)-1):
		fst_num = array[i]
		for j in range(i+1,len(array)):
			snd_num = array[j]
			if fst_num + snd_num==targetSum:
				
				return(sorted([array[j],array[i]]))
				
	#print(sorted([array[j],array[i]]))			
	return []
		
	'''
	
    # Write your code here.i
	
	arr = []
	for num in array:
		pt = targetSum - num
		if pt in arr:
			return(sorted([pt,num]))
		else:
			arr.append(num)
	return []
