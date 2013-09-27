from sys import argv
import string
script, first = argv

def main():
    f = open(first)
    filetext = f.read()

    how_many_times = [0] * 26
    lowered_text = string.lower(filetext)
    for char in lowered_text:
        if ord(char) >= 97 and ord(char) <= 122:
            how_many_times[ord(char)-97] += 1
    for i in how_many_times:
        print i

    f.close()
main()