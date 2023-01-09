#!/usr/bin/env python3

'''
StephanieCobble | Lab 67 - Challenge - Looping Vampires - Spooky Looping’ Vampires
1. Read in the content of the Dracula novel as a file object.
2. Loop over every line in Dracula, print each line out
3. Actually, fix that for loop... only print out the line if it has the word vampire in it
4. If you didn't already, make sure it prints the line no matter what case vampire is
5. Count that up! How many lines contain the word vampire?
6. Take the lines from Dracula that have vampire in it and write them to a second file named vampytimes.txt
'''
def main():

    counter = 0
    with open("dracula.txt","r") as book:
        with open("vampytimes.txt","w") as vamp:
            for line in book:
                if "vampire" in line.lower():
                    print(line)
                    counter += 1
                    vamp.write(line)
    print(counter)

if __name__ == "__main__":
    main()
