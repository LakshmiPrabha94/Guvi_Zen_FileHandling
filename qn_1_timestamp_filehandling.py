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
        
        # Format the timestamp as a string
        timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create a filename based on the timestamp
        filename = f"file_{timestamp_str}.txt"
        
        # Open the file in write mode
        with open(filename, "w") as file:
            # Write the timestamp into the file
            file.write(f"Timestamp: {timestamp_str}")
        
        print()
        print(f"File '{filename}' created successfully with the timestamp!!!")
        print()
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to create the file
create_file_with_timestamp()


