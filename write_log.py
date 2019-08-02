def wlog(line):
    f = open("log.txt","a+")
    #f=open("guru99.txt","a+")
    f.write(line + '\n')
    f.close()
