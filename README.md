# Sonda exploradora

### Descrição

Esse projeto implementa o desafio da sonda exploradora. Nesse desafio uma sonda exploradora pode navegar em uma área quandrangular (5x5) através de uma interface web. A posição da sonda é representada por três valores de coordenadas: o eixo x, o eixo y e a direção em que a sonda está orientada. A direção é representada por sua letra inicial, sendo as direções válidas:

- `E` - Esquerda
- `D` - Direita
- `C` - Cima
- `B` - Baixo

A sonda aceita três comandos:

- `GE` - girar 90 graus à esquerda
- `GD` - girar 90 graus à direta
- `M` - movimentar. Para cada comando `M` a sonda se move uma posição na direção à qual sua face está apontada.

A sonda inicia na posição (x = 0, y = 0), o que se traduz como o ponto mais inferior da esquerda e com sua face orientada à direita.
Se pudéssemos visualizar a posição inicial, seria:

| (0,4) |  (1,4) | (2,4) |  (3,4) | (4,4) |
|:-----:|  ----  |  ---- |  ----  |  ---- |
| (0,3) |  (1,3) | (2,3) |  (3,3) | (4,3) |
| (0,2) |  (1,2) | (2,2) |  (3,2) | (4,2) |
| (0,1) |  (1,1) | (2,1) |  (3,1) | (4,1) |
| * >   |  (1,0) | (2,0) |  (3,0) | (4,0) |

`* Indica a posição inicial da sonda`

`> Indica a direção inicial da sonda`

<br/>

### Configurando o projeto localmente

Para configurar localmente esse projeto é necessário possuir os seguintes requisitos instalados e devidamente configurados:

- [Python 3.6 or superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

Para iniciar a instalação, execute via terminal os seguintes comandos:

<br/>

**1.** No diretório desejado, inicie o git:
```shell script
$ git init
```
<br/>

**2.** Clone o projeto:
```shell script
$ git clone https://github.com/gustavolaires/exploration_probe.git
```
<br/>

**3.** Acesse a pasta criada com o projeto:
```shell script
$ cd exploration_probe
```
<br/>

**4.** Crie o ambiente virtual de desenvolvimento:
```shell script
$ python -m venv venv
```
<br/>

**5.** Entre no ambiente virtual de desenvolvimento:
```shell script
$ venv/scripts/activate
```
`Em alguns sistemas pode ser necessário utilizar venv/scripts/activate.ps1 ou .\venv\Scripts\activate`

<br/>

**6.** Instale as dependências do projeto:
```shell script
$ pip install -r requirements-dev.txt
```
<br/>

**7.** Crie o arquivo de nome **.env** no diretório atual e adicione os seguintes campos ao arquivo:
```shell script
SECRET_KEY=<defina_uma_chave_secreta_particular_nesse_campo>
DEBUG=True
```
<br/>

**8.** Execute as migrações do banco de dados:
```shell script
$ python manage.py migrate
```
<br/>

**9.** Execute o servidor:
```shell script
$ python manage.py runserver
```
<br/>

<br/>

### Endpoints disponíveis na interface web

Com a aplicação executando, é possível acessar a interface nos seguintes endpoints:

<br/>

**1.** Obtenha as coordenadas atuais da sonda com uma requisição de método **GET** para:
> localhost:8000/sonda/coordinate/

Será retornado um JSON com coordenadas atuais da sonda, como por exemplo:
```
{
    "x": 0,
    "y": 0,
    "face": "D"
}
```
<br/>

**2.** Envie comandos para a sonda através do envio de um JSON em uma requisição de método **PATCH** para:
> localhost:8000/sonda/move/

Exemplo de JSON enviando na requisição:
```
{
    "movimentos": ["GE", "M", "M", "M", "GD", "M", "M", "GD", "M"]
}
```

Se os comandos enviados resultarem em um caminho válido, será retornado um JSON com coordenadas atuais da sonda, como por exemplo:
```
{
    "x": 2,
    "y": 2,
    "face": "B"
}
```

Se os comandos enviados resultarem em um caminho inválido, será retornado um JSON com a seguinte mensagem:
```
{
    "erro": "Um movimento inválido foi detectado, infelizmente a sonda ainda não consegue ir tão longe."
}
```
<br/>

**3.** Faça a sonda retornar as coordenadas iniciais (x=0, y=0, face="D") com uma requisição de método **PUT** para:
> localhost:8000/sonda/reset/

<br/>

### Aplicação hospedada no Heroku

Essa aplicação também está hospedada na plataforma Heroku, podendo ser acessada pelos seguintes endpoins:

> [exploration-probe.herokuapp.com/sonda/coordinate/](https://exploration-probe.herokuapp.com/sonda/coordinate/)

> [exploration-probe.herokuapp.com/sonda/move/](https://exploration-probe.herokuapp.com/sonda/move/)

> [exploration-probe.herokuapp.com/sonda/reset/](https://exploration-probe.herokuapp.com/sonda/reset/)

<br/>

### Testes

Foram ainda desenvolvidos testes unitários que podem ser localizados em:

> ./core/tests.py

<br/>

Para realizar os testes, basta executar o comando no terminal:

```shell script
$ python manage.py test
```
