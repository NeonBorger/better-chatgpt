from subprocess import call
while True: 
  text=input("Enter text: ")
  call(["espeak",text])
