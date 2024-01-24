# Write a program to find how many times substring “Emma” appears in the given string.

def count_substring_occurrences(input_string, substring):
    
# Count the occurrences of a substring in a given string.

    count = input_string.lower().count(substring.lower())
    return count

# Given string
str_x = "Emma is good developer. Emma is a writer"

# Substring to search
substring_to_search = "Emma"

# Count occurrences
occurrences = count_substring_occurrences(str_x, substring_to_search)

# Display the result
print(f"The substring '{substring_to_search}' appeared {occurrences} times.")
