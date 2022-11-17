'''
Given a string str, your task is to write a program which takes a string str as its only input and returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.

Input Format:
The first and only line of input contains string str.

Output Format:
The output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.

Sample Input :
abcdef

Sample Output :
6

Explanation:
For string 'abcdef' palindromic subsequence are : "a" ,"b", "c" ,"d","e","f"
'''


def palindrome_subs_count(start_val, end_val):

	if(start_val > end_val):
		return 0

	elif(string_check_arr[start_val][end_val] != -1):
		return string_check_arr[start_val][end_val]

	elif(start_val == end_val):
		string_check_arr[start_val][end_val] = 1
		return string_check_arr[start_val][end_val]

	elif (str[start_val] == str[end_val]):
		string_check_arr[start_val][end_val] = (palindrome_subs_count(start_val + 1, end_val) + palindrome_subs_count(start_val, end_val - 1) + 1)
		return string_check_arr[start_val][end_val]
	else:
		string_check_arr[start_val][end_val] = (palindrome_subs_count(start_val + 1, end_val) +
					palindrome_subs_count(start_val, end_val - 1) - palindrome_subs_count(start_val + 1, end_val - 1))
		return string_check_arr[start_val][end_val]

str = input("")
string_check_arr = [[-1 for x_value in range(1000)] for y_value in range(1000)]
string_size = len(str)
print(palindrome_subs_count(0, string_size - 1))