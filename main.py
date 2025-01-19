path = "books/frankenstein.txt"
chars = []

def word_count(file_contents):
    words = file_contents.split()
    return len(words) 

def count_char(file_contents):
    my_dict = {}
    chars = "abcdefghijklmnopqrstuvwxyz"
    lowered = file_contents.lower()

    for x in lowered:
        if x not in my_dict:
            my_dict[x] = 0
        my_dict[x] = my_dict[x] + 1
        
    return my_dict

def sort_dict(dict):
    list_dict=[]
    for key in dict:
        if key.isalpha():
            temp_dict={}
            temp_dict["name"] = key
            temp_dict["num"] = dict[key]
            list_dict.append(temp_dict)
            
    return list_dict

def sort_on(dict):
    return dict["name"]


with open(path) as f:
    file_contents = f.read()
    count = word_count(file_contents)
    char_dict= count_char(file_contents)
    print("--- Begin report of {} ---".format(path))
    print("{} words found in the document".format(count))
    list_dict = sort_dict(char_dict)
    list_dict.sort( reverse=False, key=sort_on)

    for key in list_dict:
        print("The '{}' character was found {} times".format(key["name"], key["num"]))
        # print(key)
    print("--- End report ---")
