import socket,sys, os

print('xxxxxxxxxxxxxxxx -Python- xxxxxxxxxxxxxxxxxx\n')
ip=socket.gethostbyname(socket.gethostname())
user=os.getlogin()
system_name=os.getlogin()
print(user)



with open('Your file here.txt','w') as f:  #File W,R,A is for read write and append#
      f.write("This file\n\n")
      f.write("contains three lines\n")
      f.write(ip)
      f.write("\n")
      f.write(user)
      f.write("\n")
      f.write(system_name)
