#Name: Lakshmi Prabha
#Program : Write a python function to read from a text file. The function will take the name of the text file and display the content of the file into the console .
#Date : 2 Jan 2024
#Version: 1
#Python Version: 3.12.0


def read_file_and_display(file_name):
    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the entire content of the file
            file_content = file.read()
            
            # Display the content in the console
            print()
            print("Content of the file:")
            print(file_content)
    
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# Call the function to read the file
read_file_and_display('fileHandlingConcepts.txt')

print()
print("..............................................................")
print()


