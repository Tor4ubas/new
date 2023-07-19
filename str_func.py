def capitalize_string(input_string):
    return input_string.upper()
# функцию принимает на вход строку и возвращает ее со всеми заглавными буквами
my_string = "Привет, мир!"
capitalized_string = capitalize_string(my_string)
print(capitalized_string)

def capitalize_words(string): # делает заглавными первые буквы каждого слова в строке,
# поступившей на вход функции

    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string