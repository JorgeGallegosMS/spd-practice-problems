# Given a list of n numbers, determine if it contains any duplicate numbers

nums1 = [1, 2, 3, 6, 99, 2]
nums2 = [5, 1, 2, 64, 17]

def find_duplicates(num_list):
	seen_nums = set()

	for num in num_list:
		if num in seen_nums:
			return True
		else:
			seen_nums.add(num)

	return None

# print(find_duplicates(nums1))
# print(find_duplicates(nums2))

#################################

# Find the longest substring of unique letters in a given string of n letters. 

word = "pneumonoultramicroscopicsilicovolcanoconiosis"

def longest_substring(str):
	words = []
	longest_index = 0
	for i in range(len(str)):
		new_word = []
		for j in range(i, len(str)):
			if str[j] not in new_word:
				new_word.append(str[j])
			else:
				break

		words.append(''.join(new_word))

	for index in range(len(words)):
		if len(words[longest_index]) > len(words[index]):
			continue
		else:
			longest_index = index

	return words[longest_index]

print(longest_substring(word))