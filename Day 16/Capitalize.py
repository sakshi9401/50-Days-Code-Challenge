def solve(s):
    caps = ""
    for i in s.split(" "):
        caps+=i.capitalize()
        caps+=" "
    return caps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
