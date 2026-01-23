ventasDiarias={"lunes":1500,"martes":2300,"miércoles":1800,"jueves":2000,"viernes":2700,"sábado":3000,"domingo":2800}
for clave, valor in ventasDiarias.items():
    print(f"El día {clave} se vendieron {valor} euros.")
media = sum(ventasDiarias.values()) / len(ventasDiarias)