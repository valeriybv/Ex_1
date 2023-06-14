#Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2
#Напишите код, который проверяет какая из этих строк длиннее.
def compare_strings (str1, str2):
    if len(str1) < len(str2):
        print("Строка 1 короче строки 2")
        print (str1)
    elif len(str1) > len(str2):
        print("Строка 1 длиннее строки 2")
    else:
        print("Строки одинаковы по длине")

if __name__ == "__main__":
    print ("dfdsfds")
    phrase1 = input("Введите строку 1:\n")
    phrase2 = input("Введите строку 2:\n")
    compare_strings(phrase1, phrase2)