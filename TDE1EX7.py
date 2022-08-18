hour = float(input("Digite uma hora de 0 a 24: "))
minute = float(input("Digite um minuto de 0 a 59: "))

print("desde o inicio do dia ate esse horario se passaram ", hour * 60 + minute, " minutos no total assim, como se passaram ", hour * 60 * 60 + minute * 60 ," segundos no total")