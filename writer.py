list = ['1','2','4','asdfasdf','dfsdaf']

with open('/home/textdocument.txt', 'w') as f:
    for item in list:
        f.write("%s.jpg\n" % item)