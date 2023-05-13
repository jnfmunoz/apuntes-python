class Persona:
    def __init__(self, _rut, _name, _last_name, _birth_date):
        self.rut = _rut
        self.name = _name
        self.last_name = _last_name
        self.birth_date = _birth_date

class Estudiante(Persona):
    def __init__(self, _rut, _name, _last_name, _birth_day, _type_student):
        Persona.__init__(self, _rut, _name, _last_name, _birth_day)
        self.type_student = _type_student

class Universitario(Estudiante):
    def __init__(self, _rut, _name, _last_name, _birth_day, _type_student, _career , _semester):
        Estudiante.__init__(self, _rut, _name, _last_name, _birth_day, _type_student)
        self.career = _career
        self.semester = _semester

juan = Persona("20045286-0", "Juan", "Munoz", "06/09/98")
juan_estudiante = Estudiante("20045286-0", "Juan", "Munoz", "06/09/98", "universitario")
juan_universitario = Universitario("20045286-0", "Juan", "Munoz", "06/09/98", "universitario", "ingeniería en informática", "8")

#print(juan.rut ,juan.name, juan.last_name, juan.birth_date)
#print(juan_estudiante.rut ,juan_estudiante.name, juan_estudiante.last_name, juan_estudiante.birth_date, juan_estudiante.type_student)
print(f'rut alumno {juan_universitario.rut} , nombre alumno: {juan_universitario.name}, apellido alumno: {juan_universitario.last_name}, fecha de nacimiento {juan_universitario.birth_date}, tipo de estudiante: {juan_universitario.type_student}, carrera universitaria: {juan_universitario.career}, semestre: {juan_universitario.semester}')