#Name: Lakshmi Prabha
#Program : Write a python program using function to which will do the following:
# a. The function will create a text file with the current timestamp
# b. the file content should have the content of the timestamp

#Date : 2 Jan 2024
#Version: 1
#Python Version: 3.12.0


import datetime

def create_file_with_timestamp():
    try:
        # Get the current timestamp
        current_time = datetime.datetime.now()

        # Print the current timestamp
        print()
        print("Current Timestamp:", current_time)

        # Open the file in write mode using the 'with' statement
        with open("timenow.txt", 'w') as file:
            # Write the current timestamp as a string into the file
            file.write(str(current_time))

        print()
        print("File 'timenow.txt' created successfully.")

    except Exception as e:
        # Handle any exceptions that may occur during file creation
        print(f"An error occurred: {e}")

# Call the function to create the file with the current timestamp
create_file_with_timestamp()


