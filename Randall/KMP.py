def KMPSearch(search, txt):
	patternFound = []
	M = len(search)
	j = 0  # index for search


	N = len(txt)
	i = 0  # index for txt

	suffix = [0]*M

	#Creates the comparison array
	SuffixArray(search, M, suffix)


	while (N - i) >= (M - j):
		if search[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print("Found pattern at " + str(i-j))
			patternFound.append(i-j)
			j = suffix[j-1]

		# mismatch after j matches
		elif i < N and search[j] != txt[i]:
			if j != 0:
				j = suffix[j-1]
			else:
				i += 1

	return patternFound


def SuffixArray(search, M, suffix):
	len = 0
	suffix[0] = 0
	i = 1

	while i < M:
		if search[i] == search[len]:
			len += 1
			suffix[i] = len
			i += 1
		else:
			if len != 0:
				len = suffix[len - 1]
			else:
				suffix[i] = 0
				i += 1


txt = "Hola com estas co o como"
search = "como"
a = KMPSearch(search, txt)
print(len(a))



