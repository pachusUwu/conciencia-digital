# ===========================================================================================
# Laboratorio de Programación (LPR 5° Año) — E.E.S.T. N° 1 "Eduardo Ader" - Vicente López
# ACTIVIDAD 10 BIS: Simulador de Normativa de Celulares en el Aula (Ley 15.678)
# DOCENTE: Mansilla Muñoz York Elías
# ESTUDIANTES: QUIROGA, Ian - LAUDATI, Santino - IGLESIAS, Dante
# Archivo: src/ley_celulares.py
# Objetivo: Simular el filtro de decisiones que aplica un docente o el sistema escolar
#           para saber si un estudiante puede usar el celular en el aula.
# ===========================================================================================


def leer_si_no(pregunta):
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("   [AVISO] Respuesta no valida. Escriba S (si) o N (no).")


print("==================================================")
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("==================================================")
print(" Estudiantes: Ian Quiroga, Santino Laudati y Dante Iglesias")
print("==================================================\n")

motivo = input("=> Motivo por el que quiere usar el celular: ").strip()

# Simulamos las variables de contexto del aula
autorizacion_docente = leer_si_no("=> El docente habilito la actividad digital? (S/N): ")
emergencia_familiar = leer_si_no("=> La emergencia fue validada por preceptoria? (S/N): ")

print(f"\nMotivo declarado               : {motivo if motivo else '(sin motivo)'}")
print(f"Estado de Autorización Docente : {autorizacion_docente}")
print(f"Estado de Emergencia Validada  : {emergencia_familiar}\n")

# Estructura de decision
if autorizacion_docente == True:
    print("[ACCESO PERMITIDO] El celular solo para estudiar y para aprender (Fines Pedagogicos).")
elif emergencia_familiar == True:
    print("[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente a través de preceptoría y/o dirección.")
else:
    print("[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado en la mochila.")

print("==================================================")
