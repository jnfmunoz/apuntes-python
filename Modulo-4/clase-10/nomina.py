class Empleado:
    def __init__(self, _rut, _nombre, _apellido, _tipo_empleado) -> None:
        self.rut = _rut
        self.nombre = _nombre
        self.apellido = _apellido
        self.tipo_empleado = _tipo_empleado


class HorasWork:
    def agregar_horas(self, _horas):
        self.horas.append(_horas)


class Profesor(Empleado, HorasWork):
    def __init__(self, _rut, _nombre, _apellido, _tipo_empleado, _categoria) -> None:
        super().__init__(_rut, _nombre, _apellido, _tipo_empleado)
        self.categoria = _categoria
        self.horas = []


class Asistente(Empleado, HorasWork):
    def __init__(self, _rut, _nombre, _apellido, _tipo_empleado) -> None:
        super().__init__(_rut, _nombre, _apellido, _tipo_empleado)
        self.horas = []

class Evaluacion:
    def __init__(self, _fecha_inicio, _fecha_final, _nota, _numero_semana) -> None:
        self.fecha_inicio = _fecha_inicio
        self.fecha_final = _fecha_final
        self.nota = _nota
        self.numero_semana = _numero_semana
        self.es_aprobado = False
        if (_nota >= 3.5):
            self.es_aprobado = True

class Administrativo(Empleado):
    def __init__(self, _rut, _nombre, _apellido, _tipo_empleado, _titulo) -> None:
        super().__init__(_rut, _nombre, _apellido, _tipo_empleado)
        self.titulo = _titulo
        self.evaluaciones = []

    def agregar_evaluacion(self, _evaluacion):
        self.evaluaciones.append(_evaluacion)

class Obrero(Empleado):
    def __init__(self, _rut, _nombre, _apellido, _tipo_empleado, _es_graduado) -> None:
        super().__init__(_rut, _nombre, _apellido, _tipo_empleado)
        self.es_graduado = _es_graduado

class Horas:
    def __init__(self, _fecha_inicio, _fecha_final, _semana_numero, _horas) -> None:
        self.fecha_inicio = _fecha_inicio
        self.fecha_final = _fecha_final
        self.semana_numero = _semana_numero
        self.numero_horas = _horas

class Nomina:
    tipo_empleado = {
        "Docente": "D",
        "Asistente": "T",
        "Administrativo": "A",
        "Obrero": "O"
    }

    costo_hora_docente = {
        "Categoria I": 18000,
        "Categoria II": 25000
    }

    bono_titulo = {
        "Doctor": 20000,
        "Msc": 15000,
        "Titulado": 10000,
    }

    sueldo_base = {
        "Asistente": "400000",
        "Administrativo": "380000",
        "Obrero": "350000"
    }

    bono_categoria = {
        "Categoria I": 8000,
        "Categoria II": 12000
    }

    bono_hora_asistente = 500

    bono_titulo_obrero = 10000
    bono_evaluacion_administrativo = 5000

    retenciones_suedo = {
        "Docente": 0.02,
        "Administrativo": 0.02,
        "Obrero": 0.01
    }

    retencion_seguro_docente = 0.02

    def __init__(self) -> None:
        self.personal = []
        self.nomina_personal = []

    def agregar_personal(self, _empleado):
        self.personal.append(_empleado)

    def procesar_nomina(self, _semana_numero, _fecha_inicio, _fecha_final):
        for empleado in self.personal:
            
            sueldo = 0
            if (empleado.tipo_empleado == self.tipo_empleado["Docente"]):
                # Sueldos
                horas = filter(lambda hora: hora["semana"] == _semana_numero, empleado.horas)
                sueldo = self.costo_hora_docente[empleado.categoria] * horas[0].horas
                # Bono
                bono = self.bono_categoria["Docente"]
                # Retencion
                retencion = sueldo * self.retenciones_suedo["Docente"] + self.retencion_seguro_docente * sueldo
                self.nomina_personal.append((_semana_numero, _fecha_inicio, _fecha_final, sueldo, bono, retencion, empleado.rut))
            elif (empleado.tipo_empleado == self.tipo_empleado["Asistente"]):
                sueldo = self.sueldo_base["Asistente"]
                # Bono
                horas = filter(lambda hora: hora["semana"] == _semana_numero, empleado.horas)
                bono = self.bono_hora_asistente * horas[0].horas                
                # Retencion
                retencion = 0
                self.nomina_personal.append((_semana_numero, _fecha_inicio, _fecha_final, sueldo, bono, retencion, empleado.rut))
            elif (empleado.tipo_empleado == self.tipo_empleado["Administrativo"]):
                evaluacion = filter(lambda eval: eval["semana"] == _semana_numero, empleado.evaluaciones)
                bono = 0
                if evaluacion[0].es_aprobado == True:
                    bono = self.bono_evaluacion_administrativo
                sueldo = self.sueldo_base["Administrativo"] + bono
                # Bono
                bono = self.bono_titulo[empleado.titulo]
                # Retencion
                retencion = sueldo * self.retenciones_suedo["Administrativo"]
                self.nomina_personal.append((_semana_numero, _fecha_inicio, _fecha_final, sueldo, bono, retencion, empleado.rut))
            else:
                #Sueldo
                sueldo = self.sueldo_base["Obrero"]
                # Bono
                bono = 0
                if empleado.es_graduado == True:
                    bono = self.bono_titulo_obrero
                # Retencion
                retencion = sueldo * self.retenciones_suedo["Obrero"]
                self.nomina_personal.append((_semana_numero, _fecha_inicio, _fecha_final, sueldo, bono, retencion, empleado.rut))


