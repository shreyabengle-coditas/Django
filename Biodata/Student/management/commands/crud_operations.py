from django.core.management.base import BaseCommand
from Student.studentDAO import Students
class Command(BaseCommand):
    help = "Perform CRUD"

    def handle(self, *args, **kwargs):
        check=1
        while(check):
            print("What do you want to perform:\n 1)Create\n 2)Update\n 3)Delete\n 4)Display:")
            choice =int(input("Enter your choice:"))
            student_dao = Students()
            if(choice==1):
                first_name = input("Enter Student first name")
                last_name = input("Enter Student last name")
                date_of_birth= input("Enter date of birth")
                student_dao.createData(first_name,last_name,date_of_birth)

            elif(choice==2):
                #UPDATE
                updated_id_to_update = int(input("Enter ID"))
                entry=1
                while(entry):
                    print("What field you want to update: 1)First name\n 2)Last name\n 3)Date of birth")
                    field_to_update = int(input("Enter:"))
                    stud_data = student_dao.getParticular(updated_id_to_update)
                    first_name= stud_data.f_name
                    last_name= stud_data.l_name
                    dob=stud_data.dob
                
                    if(field_to_update==1):
                        updated_first_name = input("Enter updated first name")
                        student_dao.updateData(updated_id_to_update,f_name=updated_first_name,l_name=last_name,dob=dob)
                    elif(field_to_update==2):
                        updated_last_name = input("Enter updated last name")
                        student_dao.updateData(updated_id_to_update,f_name=first_name,l_name=updated_last_name,dob=dob)
                    elif(field_to_update==3):
                        updated_dob = input("Enter Date of birth")
                        student_dao.updateData(updated_id_to_update,f_name=first_name,l_name=last_name,dob=updated_dob)
                    else:
                        entry=0
                    print("Do you want to continue updating")
                    entry=int(input())

            elif(choice==3):
                delete_name=input("Enter name to delete:")
                student_dao.deleteData(delete_name)

            elif(choice==4):
            #Retrive
                all_student = student_dao.getAll()
                self.stdout.write("All employ")
                for student in all_student:
                    self.stdout.write(f"{student.f_name}  {student.l_name}  {student.dob}")
            else:
                print("Invalid Input")

            print("Do you want to Continue\n1)Continue\n0)Exit")
            check=int(input("Enter"))


        