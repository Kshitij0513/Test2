def sroute(n, arr):
		arr.sort()
		d = 0
		if n%2:
			mid = arr[n//2]
		else:
			mid = 0.5*(arr[n//2 - 1] + arr[n//2])
			
		for a in arr:
			d += abs(a - mid)
			
		return int(d)

if __name__ == '__main__':
	test_cases = int(input())
	for _ in range(test_cases):
		arr = list(map(int, input().split()))
		print(sroute(arr[0], arr[1:]))
