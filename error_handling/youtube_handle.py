#method 1  
file = open("youtube.txt" , "w")

try:
  file.write("raman kumar")
finally:
  file.close()


#method 2 
with open("youtube,txt" , "w") as file:
  file.write("raman")

