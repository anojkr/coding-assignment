#For reference - https://www.youtube.com/watch?v=jaNZ83Q3QGc 

def coin_change_problem(denom, sums):
	combination = [0]*sums
	combination.insert(0,1) 

	for coin in denom:
		for i in range(1,sums+1):
			if i>=coin:
				combination[i] = combination[i] + combination[i-coin]
		print("\nCombination status for {} is {}\n".format(coin, combination))
	print("\nMinimum number of coin require for sum {} using given denomation {} is {}\n".format(sums,denom,combination[sums]))


arr = [1,2,5]
coin_change_problem(arr,12)