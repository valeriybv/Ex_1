#Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2
#Напишите код, который проверяет какая из этих строк длиннее.
def compare_strings (str1, str2):
    if str1 < str2:
        print("1")
    elif str1 > str2:
        print("3")
    else:
        print("fdsfs")

if __name__ == "__main__":
    print ("dfdsfds")
    phrase1 = input("Введите строку 1:\n")
    phrase2 = input("Введите строку 2:\n")
    compare_strings(phrase1, phrase2)