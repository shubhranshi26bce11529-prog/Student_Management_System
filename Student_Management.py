from modules.marks import calculate_result

print("===== Student Management System=====")
students=[]      # Store all students here

#Add a new student to the list
def add_student():
    student_id = input("Enter student ID:")
    name=input("enter the student name:")
    student={
        "id":student_id,
        "name":name
    }
    students.append(student)

    print("student added succesfully",name)

#Add marks to existing student
def add_marks():
     student_id = input("Enter student ID:")
     marks= input("Enter student marks:")
     for student in students:
          if student["id"] == student_id:
               student["marks"] =marks 
               print("marks added successfully")
               break
          else:
               print("student not found")


while True:
    print("\n===== MENU =====")
    print("1.Add Student")
    print("2. View Students")
    print("3. Delete student")
    print("4. Update student")
    print("5. Search student")
    print("6.Add marks")
    print("7.View result")
    print("8.Exit")
    
    choice=input("Enter your choice")
    if choice == "1":
        add_student()

    elif choice == "2":  # View all students
        print("\nAll Students:")
        for student in students:
             print("ID:",student["id"], "| Name:",student["name"],"| marks:",student.get("marks","not added")) 

    elif choice =="3":
        student_id=input("Enter student ID to delete:") # Remove the student from the list
        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("student deleted successfully")
                break 

    elif choice == "4":
        student_id = input("Enter student ID to update:") # Update the name of existing student
        for student in students :
             if student["id"]== student_id:
                  new_name = input("Enter new student name")
                  student["name"]=new_name
                  print("Student updated successfully")
                  break 
        else:
           print("student not found")

    elif choice == "5":
        student_id = input ("Enter student ID to search:") # find the student using student ID
        for student in students :
            if student["id"]== student_id:
                print("student found")
                print("id:",student["id"])
                print("name:",student["name"])
                break
        else:
             print("student not found")

    elif choice == "6":
           add_marks()

    elif choice=="7":
           student_id = input("Enter student ID:")  #Calculate and show the student result
           for student in students:
                if student["id"]==student_id:
                     if "marks" in student:
                          marks= float(student["marks"])
                          percentage =marks
                          print("student name:",student["name"])
                          print("marks:",marks)
                          print("percentage:",percentage,"%")

                          result = calculate_result(marks)
                          print("result:", result)
                          break
                else:
                          print("marks not added")
                          break
           else:
                print("student not found")

    elif choice =="8":
           print("Thank you for using student management system")
           break 
    else :
           print("invalid choice, please try again") 
           


