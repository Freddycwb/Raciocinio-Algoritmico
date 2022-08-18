price = float(input("Digite um preço: "))
five_percent = price * 0.05

print("valor parcelado em 3x com 5% de juros: ", (price + five_percent) / 3, " | valor parcelado em 2x sem juros: ", price / 2, " | valor a vista com 5% de desconto: ", price - five_percent)