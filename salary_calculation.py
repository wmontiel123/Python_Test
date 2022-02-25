from xml.etree.ElementInclude import include
salary = []
#Functions
def calculate_salary(salary_range,working_hours):
    salary_to_pay = 0
    #calculate the day wage
    salary_to_pay = round(working_hours/60,0)*salary_range
    return salary_to_pay
def calculate_schedule(inicio,fin,day_code):
    rango_1 = 0
    rango_2 = 0
    rango_3 = 0
    salary_total_day = 0
    #verify the hourly wage range
    if (inicio <= 540 and fin <= 541) or (541 <= inicio <= 1080 and fin <= 1081) or  (1081 <= inicio and fin >= 1081):
        if (inicio <= 540 ):
            rango_1 = fin -inicio
        if (541 <= inicio <= 1080):
            rango_2 = fin -inicio
        if (1081 <= inicio):
            rango_3 = fin -inicio
    else:
        #especial cases
        if inicio <= 540 and fin >= 541 and fin < 1081:
            rango_1 = 540 - inicio
            rango_2 = fin - 541
        if inicio <= 540 and fin >= 1081:
            rango_1 = 540 - inicio
            rango_2 = 1080 - 541
            rango_3 = fin - 1081
        if 541 >= inicio <= 1080 and fin >= 1081:
            rango_2 = 1081 - inicio
            rango_3 = fin - 1081
    #calculate for the day    
    if day_code in ['MO','TU','WE','TH','FR']:
       salary_total_day = calculate_salary(25,rango_1) + calculate_salary(15,rango_2) + calculate_salary(20,rango_3)
    else:
        salary_total_day = calculate_salary(30,rango_1) + calculate_salary(20,rango_2) + calculate_salary(25,rango_3)
    
    return salary_total_day
def proceso_principal():
    with open("Employees.txt") as fname:
    # Spliting the txt file into name and working hours
        for lineas in fname:
            nombre,horario = lineas[:-1].split('=')
            horarios = horario.split(',')
            salary.append({
                'nombre':nombre,
                'horarios':horarios
                })

        for nombre in salary:
            day_hour = nombre.get('horarios')
            name = nombre.get('nombre')
            salario_a_pagar = 0
            for horas in day_hour:
                day = horas[:2]
                inicio,fin = horas[2:].split("-")
                hora_inicio,minuto_inicio = inicio.split(":")
                inicio = int(hora_inicio)*60+int(minuto_inicio)
                hora_fin,minuto_fin = fin.split(":")
                fin = int(hora_fin)*60+int(minuto_fin)  
                if fin == 0:
                    fin = 1440
                salario_a_pagar = salario_a_pagar + calculate_schedule(inicio,fin,day)
            print(name,salario_a_pagar)
    
#Principal process
if __name__ == "__main__":
    proceso_principal()







