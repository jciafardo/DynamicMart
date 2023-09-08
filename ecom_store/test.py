from collections import Counter

# initializing strings
test_str1 = 'bugatti'
test_str2 = "msn"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K
K = 2

# extracting frequencies
cnt1 = Counter(test_str1.lower())
cnt2 = Counter(test_str2.lower())

# getting maximum difference
res = True
if max((cnt1 - cnt2).values()) > K or max((cnt2 - cnt1).values()) > K:
	res = False

# printing result
print("Are strings similar ? : " + str(res))
