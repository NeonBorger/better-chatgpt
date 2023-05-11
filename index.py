import subprocess

print("Welcome to Better ChatGPT!")
print("Please enter the mode that will be used for this session.")
print("1. Normal")
print("2. Normal, Does not speak")
print("3. Manual Speech")
print("4. Normal, Real voice.")

mode = input("Enter the mode number: ")

if mode == "1":
    subprocess.call(["python", "scripts/main.py"])
elif mode == "2":
    subprocess.call(["python", "scripts/no-speak.py"])
elif mode == "3":
    print("Manual Speech Options:")
    print("1. GTTS Manual Speech")
    print("2. Normal Manual Speech")
    option = input("Enter the option number: ")
    if option == "1":
        subprocess.call(["python", "scripts/gtts/gtts-manual-speech.py"])
    elif option == "2":
        subprocess.call(["python", "scripts/manual-speech.py"])
    else:
        print("Invalid option selected. Please try again.")
elif mode == "4":
    subprocess.call(["python", "scripts/gtts/gtts.py"])
else:
    print("Invalid mode selected. Please try again.")
