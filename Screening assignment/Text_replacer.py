def  Text_replacer(Filename, Original, Replacemnt):
# Read in the file
        with open(Filename, 'r') as file :
            filedata = file.read()

# Replace the target string
        filedata = filedata.replace(Original, Replacemnt)

# Write the file out again
        with open(Filename, 'w') as file:
            file.write(filedata)

Text_replacer('example.txt','placement','screening')
