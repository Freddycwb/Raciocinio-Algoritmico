height = float(input("Digite uma altura: "))
radius = float(input("Digite um raio: "))

number_of_cans = int((2 * 3.1415 * radius * height + 2 * 3.1415 * radius ** 2) / 5 * 3)

print("sera necessario R$", float(number_of_cans * 50)," para comprar as latas para pintar esse cilindro, e vão ser compradas ", number_of_cans," latas")