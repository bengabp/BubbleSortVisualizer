""" The bubble sort algorithm is a famous sorting algorithm.
It repeatedly compares the current element and the next
element and swaps both if the current one is greater than
the next one. Using this approach it is able to sort the given
array in ascending order"""


def bubble_sort(A):
	iterations = 0
	for i in range(len(A)):
		for j in range(len(A) - 1):
			iterations += 1
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]

	print("Took", iterations, "Iterations")
	return A


A = [12, 4, 3, 5, 6, 5]
print(bubble_sort(A))
