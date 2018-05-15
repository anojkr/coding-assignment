#For reference - https://www.youtube.com/watch?v=jaNZ83Q3QGc 
def coin_change_problem(denom, sums):
	combination = [0]*sums
	combination.insert(0,1) 

	for coin in denom:
		for i in range(1,sums+1):
			if i>=coin:
				combination[i] = combination[i] + combination[i-coin]
		#print("\nCombination status for {} is {}\n".format(coin, combination))
	print("\nTotal number of combination that make up for sum {} using given denomation {} is {}\n".format(sums,denom,combination[sums]))


#For Refrence - https://www.youtube.com/watch?v=GafjS0FfAC0
def minimum_coin_for_sum(denom, sums):
	table = [0]*(sums+1)
	table[0] = 0

	for coin in range(1,sums+1):
		r = []
		for d in denom:
			if d<=coin:
				r.append(table[coin-d])
		table[coin] = min(r)+1
	print("\nMinimum no. of coin required from denominations {} to get sum of {} is {}\n".format(denom, sums, table[sums]))


arr = [9,5,4,3,2,7,1]
coin_change_problem(arr,55)
minimum_coin_for_sum(arr, 55)