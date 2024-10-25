def todolist():
 file=open("notewriter.txt","a+")
 list_name=str(input("ENTER THE TITLE OF YOUR NOTE""\n"))
 print("NAME OF NOTE IS SUCCESSFULLY ADDED IN FILE")
 file.write(list_name+"\n")
 print("WHAT DO YOU WANTS TO WRITE A PARAGRAPH OR LIST")
 choice=int(input("ENTER 1-PARAGRAPH OR 2-LIST:"))
 if(choice==1):
  print("PRESS ENTER TO FINISH WRITING")
  para=str(input("HERE YOU BEGIN................""\n"))
  file.write(para)
 if(choice==2):
  nameoflist=str(input("ENTER LIST NAME:"))
  file.write(nameoflist+"\n")
  print("LIST NAME IS SUCCESFULLY ADDES INTO FILE")
  inp=int(input("HOW MANY ITEMS DO YOU WANTS TO ADD IN YOUR LIST"))
  for i in range (inp):
   itemno=str(input("ENTER ITEM NUMBER:"))
   itemname=str(input("ENTR ITEM NAME AS PER YOUR WISH"))
   file.write(itemno+"-")
   file.write(itemname+"\n")

todolist()