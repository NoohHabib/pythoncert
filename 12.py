def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

string = input("enter a string:").strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)