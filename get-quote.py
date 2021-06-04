import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write("Now the file has more content!") #add quotes programmatically
  f = open("quotes.txt", "r")
  quotes = f.readlines()
  f.close()
  #last=13   #last = len(quotes) - 1
  #rnd1= random.randint(0,last)
  #rnd2= random.randint(0,last)
  quotesE = [i.strip('\n') if type(i)== str else str(i) for i in quotes]
   #remove \n from each item in list






  print(quotesE[0], end = ' ')
  #print(quotes[rnd2])
  print(quotesE[1])

  print(quotesE[0])
  #print(quotes[rnd2])
  print(quotesE[1])

  #print(type(quotes))

  #print("hello", end=" ")
  #print("world")
if __name__== "__main__":
  primary()
