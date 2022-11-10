def count_substring(string, sub_string):
    c = 0
    strlist = []
    for i in range(0,len(string)):
        s = string[i:]
        strlist.append(s)
    for i in strlist:
        j = i[0:len(sub_string)]
        if j == sub_string:
            c= c+1
    return c
     
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
