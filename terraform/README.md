# Usando block dynamic

No dock desafio teste para criação Main com Variaveis utilizei uma estrutura de 3 blocos de ingress onde 
o mesmo será substituídos por um dynamic block

#Configuração utilizada no Main.tf
Utilizando boas praticas foi utilizado um formato padrão onde não ha a necessidade de repetir varias vezes a mesma função

#terraform		
```	dynamic "ingress" {
	  for_each = var.default_ingress
	  content {
		description = ingress.value["description"]
		from_port   = ingress.key
		to_port     = ingress.key
		protocol    = "tcp"
		cidr_blocks = ingress.value["cidr_blocks"]
	  }
	}
```

#Configuração utilizada no variable.tf
Utilizando a variável **default_ingress** será usada no loop onde a variável definida é do tipo mapa e será inteirada diretamenta ao loop for_each dentro do main.tf.

```
  22 = { description = "SSH", cidr_blocks = [ "127.0.0.1/32" ] }
  80 = { description = "HTTP", cidr_blocks = [ "127.0.0.1/32" ] }
  443 = { description = "HTTPS", cidr_blocks = [ "127.0.0.1/32" ] }

```


## Intalação do Terraform deve primeiro ser instalado em sua máquina local ou onde você planeja executá-lo. 

Para instalar o Terraform, encontre o pacote apropriado para o seu sistema e faça o download.
Link para download : https://www.terraform.io/downloads.html

Após o download, descompacte o pacote em um diretório onde o Terraform será instalado. 
(Exemplo: ~/terraform ou c:\terraform) e criar uma "ENVIRONMENT VARIABLES".


## Utilizar no windows shell ou prompt e terminal linux

```
1- Inicialize o provedor, certifique-se de estar no diretório antes de executar o comando abaixo:
	Terraform init

2- Execute o comando abaixo para preparar a estrutura:
	terraform plan

3- Agora você está pronto para criar a infraestrutura definida no arquivo de configuração main.tf do seu módulo raiz:
	terraform apply ( Aparecera um mensagem para confirmar a instalação digitar yes ou No . 

4 - Para verificar a implantação, recuperar o endereço IP da sua instância:
	terraform show | grep 'ip_address'

5 - Para remover a estrutura criada utilizar o comando baixo:
	terraform destroy -auto-approve

```

