# Analytics

Interface web para consulta de indicadores de acessos e publicação das coleções da rede SciELO.

---

## Arquivos: Dockerfile* e docker-compose*.yml

### Dockerfile

* **Dockerfile**: define a imagem para **produção**.
* **Dockerfile-dev**: define a imagem para **desenvolvimento**, com ferramentas adicionais e configuração para debug.

### Docker Compose

* **docker-compose.yml**: inicia todos os containers necessários para **produção**.
* **docker-compose-dev.yml**: inicia todos os containers necessários para **desenvolvimento**, incluindo Memcached, VPN, etc.

---

## Execução dos testes

Para testes, é mais prático usar um ambiente virtual Python em vez de containers Docker.

1. Instale a dependência de sistema `libmemcached-dev` (no Ubuntu/Debian):

```bash
sudo apt install libmemcached-dev
```

2. Crie um ambiente virtual Python 3.6 (usando miniconda):

```bash
conda create -n scl-analytics python=3.6 -y
conda activate scl-analytics
```

3. Instale as dependências:

```bash
pip install deps/scielojcr-1.3.0-py2.py3-none-any.whl
pip install -r requirements.txt
```

4. Execute os testes de unidade:

```bash
python setup.py test
```

> ⚠️ **Observação**: fora do Docker, o Memcached deve estar rodando localmente (`127.0.0.1:11211`). Você pode iniciá-lo com:

```bash
docker run -d --name memcached-dev -p 11211:11211 memcached:latest
```

---

## Integrações

O Analytics integra cinco serviços principais:

* **Article Meta**: [GitHub](https://github.com/scieloorg/articles_meta)
* **Publication Stats**: [GitHub](https://github.com/scieloorg/publication_stats)
* **Access Stats**: [GitHub](https://github.com/scieloorg/access_stats)
* **Bibliometrics**: [GitHub](https://github.com/scieloorg/bibliometrics)
* **SUSHI API**: [GitHub](https://github.com/scieloorg/scielo-sushi-api)

### Conexões necessárias

| Serviço           | Host/Port                    | Observações       |
| ----------------- | ---------------------------- | ----------------- |
| Article Meta      | articlemeta.scielo.org:11621 | Thrift            |
| Publication Stats | publication.scielo.org:11620 | Thrift            |
| Access Stats      | ratchet.scielo.org:11660     | Thrift            |
| Bibliometrics     | usa conexão do Article Meta  | Thrift            |
| SUSHI API         | usage.apis.scielo.org        | HTTP (não Thrift) |

> ⚠️ **Importante**: verifique a conectividade antes de instalar. Exemplo com `telnet`:

```bash
telnet articlemeta.scielo.org 11621
```

Se conectar, o host tem acesso à porta do serviço.

---

## Executando a aplicação (desenvolvimento)

1. Crie o arquivo `development.ini` a partir do template:

```bash
cp development.ini-TEMPLATE development.ini
```

2. Certifique-se de que Memcached está acessível:

   * Fora do Docker: use `docker run -d --name memcached-dev -p 11211:11211 memcached:latest`
   * Dentro do Docker Compose: o serviço já estará configurado.

3. Construir o container:

```bash
docker-compose -f docker-compose-dev.yml build --no-cache
```

4. Iniciar o container:

```bash
docker-compose -f docker-compose-dev.yml up
```

5. Conectar-se à VPN SciELO (necessário para acessar alguns serviços).

6. Acessar a interface web:

```
http://0.0.0.0:6543
```

---

## Alterando a aplicação (desenvolvimento)

Sempre que fizer alterações:

1. Construir o container (`docker-compose build --no-cache`)
2. Iniciar o container (`docker-compose up`)
3. Conectar à VPN SciELO
4. Acessar a interface web (`http://0.0.0.0:6543`)

> ⚠️ Para desenvolvimento local fora do Docker, lembre-se de iniciar o Memcached local (`127.0.0.1:11211`) antes de rodar o `pserve`.

---

## Internacionalização

Para adicionar ou atualizar strings de tradução, siga os passos abaixo.

### 1. Marcar Strings para Tradução

Nos templates Mako (`.mako`), envolva as strings com `${_(u'texto para traduzir')}`. Em arquivos Python (`.py`), use `_('texto para traduzir')` após importar o tradutor.

### 2. Extrair Novas Strings

Execute o comando abaixo na raiz do projeto para extrair as strings marcadas para um arquivo de modelo (`.pot`):

```bash
python setup.py extract_messages
```

### 3. Atualizar os Arquivos de Tradução

Atualize os arquivos de tradução (`.po`) de cada idioma com as novas strings do arquivo de modelo:

```bash
python setup.py update_catalog
```

### 4. Traduzir as Strings

Edite os arquivos `.po` em `analytics/locale/<idioma>/LC_MESSAGES/analytics.po` e adicione as traduções para as strings com `msgstr ""`.

### 5. Compilar as Traduções

Compile os arquivos `.po` para o formato binário (`.mo`), que é usado pela aplicação:

```bash
python setup.py compile_catalog
```
