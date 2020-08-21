#Weather IPA

Projeto construido com objetivo de criar um serviço via rest-api que consulte o tempo

O projeto consiste na integração [AWS Lambda], [API Gateway] e wttr.in

[Demo](https://243qccqx07.execute-api.sa-east-1.amazonaws.com/weather/weather)

## O usuario podera utilizar a ferramentas Postman ou api gateway para realizar o teste abaixo
Podemos utilizar o postman para visualizar a previsão do tempo

No Postman podemos criar um method GET utilizando a url  https://243qccqx07.execute-api.sa-east-1.amazonaws.com/weather/weather, 

no authorization deixar como no auth, body selecione raw e utilizar a linha abaixo para saber o tempo:
```
	{
		"name": "Nome da cidade"
	}
```
```
	return
	{
		"statusCode": 200,
		"body": {
			"FeelsLikeC": "17",
			"Temperature": "17",
			"Humidity": "88"
		}
	}
```

### Codigo fonte
$ git clone https://github.com/ederwfranca/desafio_cloud_sre.git

##Na pasta web-API temos o codigo em Nodejs e um em Python

```
	- Nodejs é o mesmo codigo que utilizar nos testes via postman
	- Python pode ser realizado teste na propria maquina
```

## Intalação da infraestrutura tem um readme dentro da pasta Terraform. 
