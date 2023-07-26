class StudentModel:
    #model kısmında öğrenci ekleme işlemleri yapılır.
    #mvc design pattern de model kısmında daha çok ekleme-silme vb.veritabanı işlemleri yapılmaktadır.
    #bu fonksiyında bir öğrenci listesi oluşturulup ekleme-get vb. işlemler onun üzerinden yapılıp daha sonra
    #view de gösterilicek ve controller da ise bir araya getirilecek.
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, roll_number):
        self.students[roll_number] = {'name': name, 'age': age, 'roll_number': roll_number}

    def get_student(self, roll_number):
        return self.students.get(roll_number)

    def get_all_students(self):
        return list(self.students.values())


class StudentView:
    #eklenen öğrncilerin bilgilerini göstermeye yarar.
    #bu pattern de view kısmında daha çok görselleştirme tabanlı işlemleriş yaparız.
    def show_student_details(self, student):
        if student:
            print("Student Details:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Roll Number: {student['roll_number']}")
        else:
            print("Student not found.")

    def show_all_students(self, students):
        print("All Students:")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Roll Number: {student['roll_number']}")


class StudentController:
    #controller kısmında ise model ve view de elde edilen bilgiler bir araya getirilir ve kullanılır.
    # pattern kullanılırken aslında tüm gereken işlemler view ve mmodelin bir araya gelmiş hali olan
    #controller kısmında bir araya gelmektedir.
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

    def add_student(self, name, age, roll_number):
        self.model.add_student(name, age, roll_number)

    def get_student(self, roll_number):
        student = self.model.get_student(roll_number)
        self.view.show_student_details(student)

    def get_all_students(self):
        students = self.model.get_all_students()
        self.view.show_all_students(students)


def main():
    #main kısmında controller nesnesi ile istenen veriler eklenir ve sonra gerekli fonksşyon çağırılıp print edilir.
    controller = StudentController()

    controller.add_student("John Doe", 20, "12345")
    controller.add_student("Jane Smith", 22, "54321")

    controller.get_student("12345")
    controller.get_student("54321")

    controller.get_all_students()


if __name__ == "__main__":
    main()

