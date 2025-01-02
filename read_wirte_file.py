# f = open("G:\\New learning\\python\\newone.txt","w") for write something
#f = open("G:\\New learning\\python\\newone.txt","a") #for over write the file text with new text
# f.write("\nI love PHP")
# f.close()

# f = open("G:\\New learning\\python\\newone.txt","r")
# f_out = open("G:\\New learning\\python\\newone_qc.txt","w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write("Wordcount "+str(len(tokens))+line)

# f.close()
# f_out.close()

with open("G:\\New learning\\python\\newone.txt","r") as f:
    print(f.read())

print(f.closed)