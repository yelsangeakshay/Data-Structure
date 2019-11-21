def threeNumberSum(array, targetSum):
    # Write your code here.

	lst = []
	array.sort()
	
	for i in range(len(array)-2):
		L = i+1
		R = len(array)-1
		while(L<R):
			temp_sum = array[i] + array[L] + array[R]
			if temp_sum == targetSum:
				lst.append([array[i],array[L],array[R]])
				L += 1
				R -= 1
			elif temp_sum < targetSum:
				L += 1
			elif temp_sum > targetSum:
				R -= 1
	
	return lst

