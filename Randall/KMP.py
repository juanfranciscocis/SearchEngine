import time
def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time.time()*10**12
        result = func(*args, **kwargs)
        t2 = time.time()*10**12
        return result , t2-t1
    return wrap_func


with open('huge_txt_example.txt', 'r') as file:
    document = file.read()
#data to lowercase
document = document.lower()




wordSearchList = ['dui','aliquam','habitant','neque','nunc','commodo','libero','nulla','sapien','suscipit','viverra','mauris','nibh','nisi','nisl','nunc','odio','orci','ornare','pellentesque','pharetra','placerat','porta','porttitor','posuere','potenti','praesent','pretium','proin','pulvinar','purus','quam','quis','quisque','rhoncus','risus','rutrum','sagittis','sapien','scelerisque','sed','sem','semper','senectus','sit','sociis','sociosqu','sodales','sollicitudin','suscipit','suspendisse','taciti','tellus','tempor','tempus','tincidunt','torquent','tortor','tristique','turpis','ullamcorper','ultrices','ultricies','urna','ut','varius','vehicula','vel','velit','venenatis','vestibulum','vitae','vivamus','viverra','volutpat','vulputate']

@timer_func
def KMPSearch(search, txt):
	M = len(search)
	j = 0  # index for search
	index = []


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
			index.append(i - j)
			# print("Found pattern at " + str(i-j))
			j = suffix[j-1]

		# mismatch after j matches
		elif i < N and search[j] != txt[i]:
			if j != 0:
				j = suffix[j-1]
			else:
				i += 1
	print("Word found at: ",index)


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


runtimeSearch = []
for i in wordSearchList:
	search = KMPSearch(i,document)
	runtimeSearch.append(search[1])

print(runtimeSearch)







