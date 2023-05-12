class Alumno:
    #variable de clase
    semestre = 1
    asignaturas = ["Python", "Javascript", "Base de datos"]

    def __init__(self, _name):
        #variable instancia
        self.name = _name
        self.asignatura = ""
        self.notas = []
    #metodos
    def inscribir_asignaturas(self, _asignatura):
        self.asignatura = _asignatura

    def registrar_notas(self, _nota):
        self.notas.append(_nota) #[4, 5.5, ... n]
    
    def get_promedio(self):
        promedio = sum(self.notas)/len(self.notas)
        print(f'el promedio de notas de {self.name} es: {promedio} ')

alumno1 = Alumno("Marysabel")
alumno2 = Alumno("María José")
alumno3 = Alumno("María Fernanda")

print(f'alumno 1: {alumno1.name}, alumno 2: {alumno2.name}, alumno 3: {alumno3.name}')
print(f'semestre alumno 1: {alumno1.semestre }, semestre  alumno 2: {alumno2.semestre }, semestre  alumno 3: {alumno3.semestre}')

alumno2.semestre = 2
print(f'semestre alumno 1: {alumno1.semestre }, semestre  alumno 2: {alumno2.semestre }, semestre  alumno 3: {alumno3.semestre}')

Alumno.semestre = 3
print(f'semestre alumno 1: {alumno1.semestre }, semestre  alumno 2: {alumno2.semestre }, semestre  alumno 3: {alumno3.semestre}')

alumno1.inscribir_asignaturas("Python")

alumno1.registrar_notas(7,7,6.5)
print(alumno1.nota1)
print(alumno1.nota2)
print(alumno1.nota3)