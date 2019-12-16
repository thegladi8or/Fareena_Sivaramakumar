import re
try:
    with open('D:\RA\Git\Python\challenge2\MP_N_EXT_RAND_0001_sample.txt', 'r+') as readFile:
        fileData=readFile.readlines()
        content=[]        
        i=0
        for record in fileData:
            i+=1
            field=record.split()
            field[0]="\t"+field[0]
            if (i==1):
                field[11]=field[11]+"\n"
                content.append('\t'.join(field))
            elif (not re.search("-1",field[2]) and not re.search("-1", field[3]) and (re.search("A1/A2", field[5].upper()) or re.search("A2/A1", field[5].upper())) and (re.search("M1/M2",field[6].upper()) or re.search("M2/M1", field[6].upper()))):   
                field[11]="#"+"\n"
                content.append('\t'.join(field))
            else:
                field[11]=field[11]+"\n"
                content.append('\t'.join(field))
            fileData = readFile.readline()
    readFile.close()

    with open('D:\RA\Git\Python\challenge2\MP_N_EXT_RAND_0001_sample.txt', 'w+') as readFile:
        #update content to file
        for line in content:
            readFile.write(line)
    readFile.close()            
except Exception as err:
    print("Error: {0}".format(err))