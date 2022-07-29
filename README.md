# Analytics

Interface web para consulta de indicadores de acessos e publicação das coleções da rede SciELO.


### Arquivos: Dockerfile* e docker-compose*.yml


Dockerfile:
- **Dockerfile**: contém as definições para construir a imagem pronta para instalar em **produção**
- **Dockerfile-dev**: contém as definições para construir a imagem pronta para instalar em **desenvolvimento**

Docker Compose:
- **docker-compose.yml**: contém as definições para iniciar todos os containers necessários para rodar em **produção**
- **docker-compose-dev.yml**: contém as definições para iniciar todos os containers necessários para rodar em **desenvolvimento**


### Como executar os tests



- Para rodar os tests de unidade, pode executar: ``python setup.py test``


### Integrações

O analytics é um aplicação que faz a integração de 5 serviços:

* Article Meta: https://github.com/scieloorg/articles_meta
* Publication Stats: https://github.com/scieloorg/publication_stats
* Access Stats: https://github.com/scieloorg/access_stats
* Bibliometrics: https://github.com/scieloorg/bibliometrics
* SUSHI API: https://github.com/scieloorg/scielo-sushi-api

Para realizar o uso do analytics é necessário ter as conexões **Thrift** dos quatro primeiros serviços listados a seguir e uma conexão com a SUSHI API (que não possui **Thrift**):

* Article Meta: articlemeta.scielo.org:11621
* Publication Stats: publication.scielo.org:11620
* Access Stats: ratchet.scielo.org:11660
* Bibliometric Stats: Utiliza a conexão do Article Meta
* SUSHI API: usage.apis.scielo.org

É **importante** testar previamente se o host que está utilizando para fazer a instalação da aplicação está com conectividade para esses endereços e portas, para isso utilize o utilitário **telnet**.

```shell
telnet hospedeiro porta
```

Caso a conexão seja estabelecida é que o host esta com acesso na porta do serviço do **thrift**, o que garante que o serviço esta acessível, tanto em uma instalação local utilizando o ```python setup.py``` quanto em uma instalação dockenizada.

### Executando a aplicação (desenvolvimento)

Na primeira execução fazer uma cópia do arquivo `development.ini-TEMPLATE`

```shell
cp development.ini-TEMPLATE development.ini

```

Construir do container
```shell

docker-compose -f docker-compose-dev.yml build --no-cache
```

Iniciar o container
```shell
docker-compose -f docker-compose-dev.yml up
```

Conectar-se a VPN SciELO

Acessar a interface web: http://0.0.0.0:8000

### Alterando a aplicação (desenvolvimento)

Cada vez que for editar/corrigir algo na aplicação, repetir os passos:

Construir o container (verificar se sua conexão com Internet está ok); Iniciar o container; Conectar-se a VPN SciELO e Acessar a interface web.
