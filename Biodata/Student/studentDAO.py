from Student.models import Student
class Students:
    def getParticular(self,updated_id_to_update):
        new_stud = Student.objects.get(id=updated_id_to_update)
        return new_stud

    def getAll(self):
        new_stud = Student.objects.all()
        return new_stud

    def createData(self,first_name,last_name,date_of_birth):
        new_stud = Student(f_name=first_name, l_name=last_name, dob=date_of_birth)
        new_stud.save()
        return new_stud
    
    def deleteData(self, first_name):
        new_stud = Student.objects.get(f_name = first_name)
        new_stud.delete()

    def updateData(self, stud_id, **updated_data):
        try:
            new_stud = Student.objects.get(id=stud_id)
            for key, value in updated_data.items():
                setattr(new_stud,key,value)
            new_stud.save()
            return new_stud
        except Student.DoesNotExist:
            return None
