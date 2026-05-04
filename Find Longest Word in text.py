import string
def longest_word_finder(text: str) -> list:
    """
    Find Longest Word in a text variable.

    Args:(text):
    
    TypeError: Input must be a string.

    Returns: Return a list.
    """
    
    if not isinstance(text,str):
        raise TypeError("input must be a string")
    
    # string.punctuation
    text = text.lower()
    pattern = str.maketrans("","",string.punctuation)
    clean_text = text.translate(pattern)
    words_list = clean_text.split()
    
    word_count_dict = {}
    for word in words_list:
        if word not in word_count_dict:
            word_count_dict[word] = len(word)
    
    max_len = max(word_count_dict.values())
    
    longest_word = [key for key,value in word_count_dict.items() if value == 11]
    return longest_word

if __name__ == "__main__":
    text = """Building a modern requires patience. Is programming difficult? Many People find the process rewarding."""
             
    try:
        print(longest_word_finder(text))
    except TypeError as e:
        print("Error:",e)
    except Exception as e:
        print("Error:",e)