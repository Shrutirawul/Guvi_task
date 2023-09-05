# 1. a)Write a python program to create a text file with the current timestamp.
# b)The content of the file should have the content of the current timestamp.
import datetime

def current_timestamp_file():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%y-%m-%d_%H-%M-%S")
    file_name = f"timestamp_{timestamp}.txt"

    with open(file_name, "w") as file:
        file.write("Timestamp: " + str(current_time))

if __name__ == "__main__":
    current_timestamp_file()
    print("Timestamp file created")


# 2. Write a python function to read from a text file.The function will take the name of the file and display the contents of the file on console.
file = open("myfile.txt","w")
file.write("Chandrayaan 3 successfully landed on moon")
file.close()

file= open("myfile.txt","r")
print(file.read())



