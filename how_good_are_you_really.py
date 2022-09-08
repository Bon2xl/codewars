# How good are you really?
#https://www.codewars.com/kata/5601409514fc93442500010b/train/python

# Append item to the right list
# Check the array count
# If more people are great than your point
# Return false
# Othewise true
def better_than_average(class_points, your_points):
	high_points = []
	lower_points = []
	i_am_better = False

	for point in class_points:
		if (point > your_points):
			high_points.append(point)
		else:
			lower_points.append(point)

	if len(high_points) <= len(lower_points):
		i_am_better = True
    
	return i_am_better


print(better_than_average([45, 69, 94, 25, 88, 98, 8, 34, 74, 55, 14, 37, 17, 8, 3, 40, 64, 59, 89, 4, 15, 16, 99, 34, 44, 80, 62, 27, 96, 75, 74, 56, 62, 25, 29, 16, 39, 69, 17, 76, 40, 69, 57, 51, 62, 52, 65, 88, 44, 63], 53))
print(better_than_average([3, 4], 5))