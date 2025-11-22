import os, csv, sys
from time import sleep
data = [
    {'id' : 1, 'name' : 'string', 'age' : 0, 'grade' : 'string', 'subject_name' : 'string', 'mark' : 3},
    {'id' : 2, 'name' : 'string', 'age' : 0, 'grade' : 'string', 'subject_name' : 'string', 'mark' : 4}
]


path = 'file2'
file_name = 'data.csv'

os.makedirs(path, exist_ok  = True)
csv_file = os.path.join(path, file_name)

with open(csv_file, mode = 'w', encoding = 'utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


# 1

def add_student(id,name,age,grade,subject_name,mark):

    student = {'id' : id, 'name' : name, 'age' : age, 'grade' : grade, 'subject_name' : subject_name, 'mark' : mark}

    for x in data:
        if id == x['id']:
            print("Such Student Already Exists!")
            sys.exit()
    else:
        with open(csv_file, mode = 'a', encoding = 'utf-8', newline='') as f:
            append = csv.DictWriter(f, fieldnames=data[0].keys())   
            append.writerow(student)

    with open(csv_file, mode = 'r', encoding = 'utf-8') as f:
        reader1 = list(csv.DictReader(f))

        reader1.sort(key=lambda x: x['id']) 

        
            
                

add_student(3, 'string', 0 , 'string', 'string', 0)


#2

def read_student(id):

    input_student = None

    with open(csv_file, mode = 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        try:
            if id == 'all':
                for x in reader:
                    print("="*85)
                    print(f"ID: {x['id']:<5}| Name: {x['name']:<8}| Age: {x['age']:<3}| Grade: {x['grade']:<8}| Subject: {x['subject_name']:<8}| Mark: {x['mark']}")
                    print("="*85)
            elif id.isdigit():
                for x in reader:
                    if x['id'] == id:
                        print("="*85)
                        print(f"ID: {x['id']:<5}| Name: {x['name']:<8}| Age: {x['age']:<3}| Grade: {x['grade']:<8}| Subject: {x['subject_name']:<8}| Mark: {x['mark']}")
                        print("="*85)
                else:
                    print("Such Student Doesn't Exist!")
            else:
                print("Such Option Doesn't Exist!")
        except TypeError:
            print("Wrong Type of Input!")
            sleep(1)
            print("Exiting...")
            
                
read_student(input("Enter an ID or All: "))


#3

def average_student(subject):

    arr = []
    count = 0

    with open(csv_file, mode = 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for x in reader:
            if x['subject_name'] == subject:
                arr.append(x['mark'])
        
    for y in arr:
        count += int(y)
    
    return count/len(arr)
    


            
print(average_student(input("Enter any subject: ")))

#4

def update_student(id, subject, mark):
    with open(csv_file, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

        for r in rows:
            if r['id'] == str(id) and r['subject_name'] == subject:
                r['mark'] = str(mark)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

update_student(3, 'string', 90)



    
    

