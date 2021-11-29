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
- Para ter o relatório de coverage deve executar: ``python setup.py converage``


### Integrações

O analytics é um aplicação que faz a integração de 4 serviços:

* Article Meta: https://github.com/scieloorg/articles_meta
* Publication Stats: https://github.com/scieloorg/publication_stats
* Access Stats: https://github.com/scieloorg/access_stats
* Bibliometrics: https://github.com/scieloorg/bibliometrics

Para realizar o uso do analytics é necessário ter as seguintes conexões **Thrift**:

* Article Meta: articlemeta.scielo.org:11621
* Publication Stats: publication.scielo.org:11620
* Access Stats: ratchet.scielo.org:11660
* Access Stats: Utiliza a conexão do Article Meta

É **importante** testar previamente se o host que está utilizando para fazer a instalação da aplicação está com conectividade para esses endereços e portas, para isso utilize o utilitário **telnet**.

```shell
telnet hospedeiro porta
```

Caso a conexão seja estabelecida é que o host esta com acesso na porta do serviço do **thrift**, o que garante que o serviço esta acessível, tanto em uma instalação local utilizando o ```python setup.py``` quanto em uma instalação dockenizada.
