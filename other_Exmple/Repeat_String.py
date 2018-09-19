# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd")


def repeat_string(A, B):
    count = 1
    tmp = A
    max_count = (len(B) / len(A)) + 1
    while not(B in tmp):
        tmp = tmp + A
        if (count > max_count):
            count = -1
            break
        count = count + 1
    print(count)
A='abcd'
B='cdabcdab'
repeat_string(A,B)