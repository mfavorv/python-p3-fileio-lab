def write_file(file_name, file_content):
     with open(f"{file_name}.txt", mode="w") as write_file:
         write_file.write(f"{file_content}")
pass

def append_file(file_name, append_content):
     with open(f"{file_name}.txt", mode="a") as append_file:
         append_file.write(f"{append_content}")
pass

def read_file(file_name): 
    with open(f"{file_name}.txt", mode='r') as read_file:
        content = read_file.read()
    return content
pass
