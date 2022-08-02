# Ambiente de desenvolvimento.
## links 
- VS Code: https://code.visualstudio.com/download
- Python: https://www.python.org/downloads/
- Git: https://git-scm.com/downloads

## Powershell
OBS: N�o se esque�a de configurar o powershell com o comando abaixo (como administrador):
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

#Comandos
##Ambiente de desenvolvimento:
Abaixo est� uma lista dos comandos mais utilizados:
1. Cria��o do ambiente virtual
	python -m venv venv
2. Ativa��o do ambiente virutal
	.venv\Scripts\activate
3. Instalando django
	pip install django
4. Iniciando projeto
	django-admin startproject *projeto*
5. Executar servidor 
	python manage.py runserver

##Git
1. Inicializando o git
	git init
2. Config. o usarname
	git config --global user.name "Pedro Guilherme"
3. Config. o email
	git config --global user.email "exemplo@gmail.com"
4. Cofing branch
	got --global init.defaultBranch main
5. Gerando chave ssh
	ssh-keygen
6. Adicionar reposit�rio
	git remote add origin *link do reposit�rio*
7. Puxar reposit�rio
	git pull *reposit�rio*
8. Adicionar commits
	git add *
9. Enviar commits
	git push *reposit�rio*
	
