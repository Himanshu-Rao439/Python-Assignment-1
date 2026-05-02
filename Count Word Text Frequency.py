import string
def freq_count():
    
    with open(r"D:\New folder\my_file.txt",mode = "r") as file:
        text = file.read()
    pattern = str.maketrans("","",string.punctuation)
    clean_text = text.translate(pattern)
    word_list = clean_text.lower().split()
    
    word_count_dict = {}
    for word in word_list:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] = word_count_dict[word] + 1
            for key,value in word_count_dict.items():
                 print(key,value)
if __name__ == "__main__":
    try:
        print(freq_count())
    except Exception as e:
        print(e)