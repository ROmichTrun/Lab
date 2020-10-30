import re
readfile = open("telbook.txt", "r")
writefile = open("newtelbook.txt", "w")
for line in readfile:
    result = re.findall(r"\b9\d{9}\b", line)
    if not result:
        result.clear()
        result = re.findall(r"\b[7,8]\d{10}\b", line)
        if result:
            writefile.write(result[0]+"\n")
    else:
        writefile.write(result[0]+"\n")
    result.clear()
readfile.close()
writefile.close()