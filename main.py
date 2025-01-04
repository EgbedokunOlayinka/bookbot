def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    sorted_list = []

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")

    for char in char_count:
      if char.isalpha():
        sorted_list.append({"char": char, "count": char_count[char]})
    
    sorted_list.sort(reverse=True, key=sort_func)
    
    for item in sorted_list:
      print(f"The '{item["char"]}' character was found {item["count"]} times")

    print("--- End report ---")

def get_word_count(str):
  return len(str.split())

def get_char_count(str):
  char_dict = {}

  for char in str:
    lower_char = char.lower()
    if lower_char in char_dict:
      char_dict[lower_char] += 1
    else:
      char_dict[lower_char] = 1

  return char_dict

def sort_func(item):
  return item["count"]

main();