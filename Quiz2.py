# The program runs until the user types exit

def ask_word():
    while True:
        put_word= input("Enter a word (or type 'exit' to stop): ")
        if put_word.lower() == "exit":
            print("Exiting the program.")
            break
        print(f"You entered: {put_word}")

ask_word()

