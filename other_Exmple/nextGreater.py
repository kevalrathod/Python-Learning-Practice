import math
def smallestGreater(arr, n) :
	for i in range(0, n):
		diff=math.inf
		closest = -1;
		for j in range(0, n) :
			if ( arr[i] < arr[j] and arr[j] - arr[i] < diff):
				diff = arr[j] - arr[i];
				closest = j;     
		if (closest == -1):
			print ("_ ", end = "");
		else:
			print ("{} ".format(arr[closest]),end = "");

ar = [6, 3, 9, 8, 10, 2, 1, 15, 7];
n = len(ar) ;
smallestGreater(ar, n);