def calcular_imc(peso: float, altura: float):
    if altura <= 0 or peso <= 0:
        return "Peso e altura devem ser maiores que zero."
    return peso / (altura ** 2)


def classificar_imc(imc: float, genero: str):
    if genero == "homem":
        if imc < 20.7:
            return "Abaixo do peso"
        elif 20.7 <= imc < 26.4:
            return "Peso normal"
        elif 26.4 <= imc < 27.8:
            return "Marginalmente acima do peso"
        elif 27.8 <= imc < 31.1:
            return "Acima do peso"
        else:
            return "Obeso"
    elif genero == "mulher":
        if imc < 19.1:
            return "Abaixo do peso"
        elif 19.1 <= imc < 25.8:
            return "Peso normal"
        elif 25.8 <= imc < 27.3:
            return "Marginalmente acima do peso"
        elif 27.3 <= imc < 32.3:
            return "Acima do peso"
        else:
            return "Obeso"
    else:
        return "Gênero não selecionado."