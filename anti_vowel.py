def anti_vowel(text):
	resultado = ""
	vogais = "aeiouAEIOU"
	for caractere in text:
		if caractere not in vogais:
			resultado += caractere
	return resultado

print anti_vowel("Testando")