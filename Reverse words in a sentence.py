def reverse_words_function(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.

    Args:
        Sentence (str): Input Sentence.

    Returns:
        str: Sentence with words reversed.
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(sentence,str):
        raise TypeError("input must be a string")
    words_list = []
    word = ""
    for char in sentence:
        if char != " ":
            word = word + char
        else:
            words_list.append(word)
            word = ""
    words_list.append(word)
    # print(words_list)
    
    rev_sentence = ""
    for i in range(len(words_list)-1,-1,-1):
        rev_sentence = rev_sentence + words_list[i]
        if i != 0:
            rev_sentence = rev_sentence + " "
    return rev_sentence
if __name__ == "__main__":
    my_sentence = "This is python class"
    try:
        print(reverse_words_function(my_sentence))
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)