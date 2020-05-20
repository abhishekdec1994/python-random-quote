import random
def main2():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  
  last = 13
  rnd = random.randint(0,last)
  lstrip = quotes[rnd].strip()
  print(quotes[0])
  f.close()
  f = open("quotes.txt", 'a')
  inp = "Please enter "
  print(inp)
  f.write(inp)
  f.close()
if __name__== "__main__":
  main2()
