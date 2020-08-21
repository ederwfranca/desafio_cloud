import requests

def main():
	print('//////////////////////////////////////')
	print('////// Consulta Previsao do Tempo ////')
	print('//////////////////////////////////////')
	print()

	input_cidade = input('Digite o nome da cidade para saber a previsao do tempo: ')

	if not input_cidade:
		print('Cidade inválida!')
		exit()

	url = 'http://wttr.in/' + input_cidade + '?format=j1'
	request = requests.get(url)

	try:
		json = request.json()
		print('==> Previsão do tempo encontrada <==')
		print('Current Temperatura C: ' + json["current_condition"][0]["temp_C"]),
		print('Current Temperatura F: ' + json["current_condition"][0]["temp_F"]),
		print('Current Visibility: ' + json["current_condition"][0]["visibility"]),
		print('Current Humidity: ' + json["current_condition"][0]["humidity"]),
		print('Weather Temp C: ' + json["weather"][0]["hourly"][0]["tempC"]),
		print('Weather Temp F: ' + json["weather"][0]["hourly"][0]["tempF"]),
		print('Weather Visibility: ' + json["weather"][0]["hourly"][0]["visibility"]),
		print('Weather Humidity: ' + json["weather"][0]["hourly"][0]["humidity"]),
		print('Weather data: ' + json["weather"][0]["date"]),
		print('Area: ' + json["nearest_area"][0]["areaName"][0]["value"]),
		print('Pais: ' + json["nearest_area"][0]["country"][0]["value"])
	except ValueError:
		print('Cidade inválida.')


	print('---------------------------------')
	option = int(input('Deseja realizar uma nova consulta cidade ?\n1. Sim\n2. Sair\n'))
	if option == 1:
		main()
	else:
		print('Saindo da consulta Tempo...')

if __name__ == '__main__':
	main()
