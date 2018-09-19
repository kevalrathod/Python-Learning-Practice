# Given a string as your input, delete any reoccurring 
# character, and return the new string.



def delete_characters(string):
    char_seen = set()
    output_string = ''
    for char in string:
        if char not in char_seen:
            char_seen.add(char)
            output_string += char
    print(output_string)
string='abbccdfet'
delete_characters(string)
