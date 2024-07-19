# flask_celery_docker
<p>
  Este projeto tem como objetivo fornecer uma base simples para reuso em outros projetos, 
  bem como servir de treinamento e aprendizado sobre o funcionamento do Celery. 
  É um exemplo básico que utiliza Flask, Celery e Docker.
</p>

## Sobre o Projeto
<p>
Este projeto é uma aplicação básica que combina Flask, Celery e Docker para demonstrar como essas tecnologias podem ser integradas. 
Ele pode ser utilizado como ponto de partida para novos projetos ou como um meio de aprendizado sobre tarefas assíncronas com Celery.
</p>

## Tecnologias Utilizadas
* [Flask:](https://flask.palletsprojects.com/en/3.0.x/) Framework web minimalista em Python.
* [Celery:](https://docs.celeryq.dev/en/stable/getting-started/index.html) Sistema de fila de tarefas distribuídas.
* [RabbitMQ:](https://www.rabbitmq.com/) Broker de mensagens usado pelo Celery.
* [Redis:](https://redis.io/docs/latest/) Banco de dados em memória usado como backend de resultados pelo Celery.
* [Docker:](https://docs.docker.com/) Plataforma para desenvolvimento, envio e execução de aplicações em contêineres.

## Como Executar o Projeto

#### Pré-requisitos
* Docker instalado na máquina.


## Passo a Passo
1. Clone este repositório:
```
git clone https://github.com/AlexandreSCorreia/flask_celery_docker.git
cd flask_celery_docker
```
2. Construa e inicie os contêineres Docker:
```
docker-compose up --build
```
3. Acesse a aplicação:
    * Acesse o servidor Flask em http://localhost:5000/home


