# Sum without highest and lowest number
# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):
	if not arr:
		print('list is empty')
		return 0

	if len(arr) < 3:
		print('list item is less than 3')
		return 0
	
	for key, item in enumerate(arr):
		if item == max(arr):
			arr.pop(key)
			break

	for key, item in enumerate(arr):
		if item == min(arr):
			arr.pop(key)
			break

	total = 0;
	for item in arr:
		total += item

	return total

print(sum_array([6, 2, 1, 8, 10]));



		