# anagram_checker.py

def are_anagrams(str1, str2):
    # Clean up the strings: remove spaces, convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
if __name__ == "__main__":
    # Input strings for testing
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    # Output result
    if are_anagrams(str1, str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
