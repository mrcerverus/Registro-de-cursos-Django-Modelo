from app.models import Profesor, Curso, Estudiante, Direccion

def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    return curso

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido,creado_por=creado_por)
    profesor.save()
    return profesor

def crear_estudiante(rut, nombre, apellido, fecha_nac,creado_por):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac,creado_por=creado_por)
    estudiante.save()
    return estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    direccion = Direccion(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante_id=estudiante_id)
    direccion.save()
    return direccion

def obtiene_estudiante(rut):
    try:
        return Estudiante.objects.get(rut=rut)
    except Estudiante.DoesNotExist:
        return print('Estudiante no existe')

def obtiene_profesor(rut):
    try:
        return Profesor.objects.get(rut=rut)
    except Profesor.DoesNotExist:
        return print('Profesor no existe')

def obtiene_curso(codigo):
    try:
        return Curso.objects.get(codigo=codigo)
    except Curso.DoesNotExist:
        return print('Curso no existe')

def agrega_profesor_a_curso(curso_codigo, profesor_rut):
    curso = obtiene_curso(curso_codigo)
    profesor = obtiene_profesor(profesor_rut)
    curso.profesor_id.add(profesor)

def agrega_cursos_a_estudiante(rut_estudiante, cod_curso):
    estudiante = obtiene_estudiante(rut_estudiante)
    curso = obtiene_curso(cod_curso)
    curso.estudiante_id.add(estudiante)

def imprime_estudiante_cursos(rut_estudiante):
    es = obtiene_estudiante(rut_estudiante)
    print(f"Rut: {es.rut}, Nombre: {es.nombre} {es.apellido}, Fecha Nac: {es.fecha_nac}")
    ps = es.cursos.all()
    for p in ps:
        print(f"    Curso: {p.nombre}, Código: {p.codigo}, Versión: {p.version}")