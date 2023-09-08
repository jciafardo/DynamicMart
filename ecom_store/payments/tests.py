#  function is responsible for the logic of searching or a product

'''
def search_function(response):
    search = (response.session.get('search'))

    results = []

    for car in Products.objects.all():
        car_name = car.name.lower()
        percentage_of_letters = []  # variable controls what percent of letters searched matches the car being looped thorough
        letters_matched = []

        for letter in search:
            if letter.lower() in car_name:
                if letters_matched.count(letter.lower()) >= car_name.count(letter.lower()):
                    letters_matched.append(letter.lower())
                    percentage_of_letters.append(True)

                else:
                    percentage_of_letters.append(False)
            else:
                percentage_of_letters.append(False)

        if len(percentage_of_letters) > 0:
            percentage = percentage_of_letters.count(True) / len(percentage_of_letters)
        else:
            percentage = 0

        if percentage >= .5:
            results.append(car.name)
        print(search)
        print(car_name)
        print(percentage_of_letters)
        print(percentage)

    return render(response, 'search-results.html', {'results': results})




for search funciton I will:

take string typed by user 

compare each letter in users string to each 
letter in all the products (non case sensitive)

if at least 30% of the letters the user typed 
matches the letters of the products 
it will result in a search result for that product

from string import ascii_lowercase

# function to compute frequencies


def get_freq(test_str):

	# starting at 0 count
	freqs = {char: 0 for char in ascii_lowercase}

	# counting frequencies
	for char in test_str:
		freqs[char] += 1
	return freqs


# initializing strings
test_str1 = 'bugatti'
test_str2 = "tesla"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K
K = 2

# getting frequencies
freqs_1 = get_freq(test_str1)
freqs_2 = get_freq(test_str2)

# checking for frequencies
res = True
for char in ascii_lowercase:
	if abs(freqs_1[char] - freqs_2[char]) > K:
		res = False
		break

# printing result
print("Are strings similar ? : " + str(res))
'''

from fuzzywuzzy import fuzz
t = fuzz.ratio("ford focus rs", "ford")

print(t)