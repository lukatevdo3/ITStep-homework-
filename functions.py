import os, json, sys

# დავალება 12

# 1

def create_file(path, file_name):

    file = None

    if len(path.split('/')) == 2:
        file = f"{path}/{file_name}.json"
    
    os.makedirs(path, exist_ok=True)

    try:
        with open(file, mode = 'x', encoding = 'utf-8') as f:
            ...
    except FileExistsError:
        print(f"File called {file} already exists... \n")
        print("Keep going! \n")
    except TypeError:
        print("Such file couldn't be made...")
        print("Exiting...")
        sys.exit()

    return file


# 2 

def read_file(path):
    with open(path, mode = 'r', encoding = 'utf-8') as f:
        return json.loads(f.read())
    
# 3 / 4

def write_file(path, data):
    with open(path, mode = 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data, indent = 2))

# def update_file(path, dict):
    
#     data = read_file(path)

#     for x in dict:
#         if x['id'] != (y['id'] for y in data):
#             data.append(x)
#             write_file(path, data)
#         else:
#             break
    
#     return data

        





