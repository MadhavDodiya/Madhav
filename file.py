# mode -> w(write),r(read),a(append)


# f = open("pyfile.txt", "a")
# for i in range(1,11):
#     f.write(f"{i}\n")
# f.close()

# f = open("pyfile.txt", "r")
# print(f.read(40))
# print(f.readlines())
# print(f.readline())
# for i in f:
#     print(i)
# f.close()

f=open("file.txt", "a")
f.write("Now the file has more content!")

f.close()





