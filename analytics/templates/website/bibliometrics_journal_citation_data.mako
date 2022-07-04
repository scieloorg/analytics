## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
% if not selected_journal_code:
    <div class="col-md-8">
      <div class="panel panel-warning">
        <div class="panel-heading">
          <h3 class="panel-title">${_(u'Atenção')}</h3>
        </div>
        <div class="panel-body">
          ${_(u'É necessário selecionar um periódico para visualizar os relatórios de citações disponíveis.')}
        </div>
      </div>
    </div>

  % else:
  <div class="col-md-8">
    <h1>${_(u'Dados de citações')}</h1>

    <p>${_(u'Antes de usar Dados de citações selecione um periódico.')}</p>

    <p>${_(u'O módulo Analytics do SciELO fornece para cada periódico um conjunto de tabelas no formato CSV com o número de citações recebidas de periódicos da Rede SciELO e número de citações concedidas a outros periódicos sem restrição. São consideradas somente citações de periódicos a cada periódico.')}</p>
    
    <p>${_(u'Essas tabelas, disponibilizadas a partir de julho de 2022, são resultado de um processo computacional atualizado que transforma para códigos ISSN os títulos (em conjunto com outros dados) grafados nas referências citadas nos artigos da Rede SciELO. Esse processo é uma evolução daquele previamente existente e permitiu atualizar as contagens de citações para todos os periódicos.')}</p>

    <p>${_(u'É fornecida também documentação sobre o processo computacional.')}</p>

    <p>${_(u'Ao todo são disponibilizadas cinco tabelas (arquivos em formato tabular) para cada periódico e ano:')}</p>

    <ol>
      <li><b>Citações concedidas</b>: número de citações concedidas pelo periódico</li>
      <li><b>Citações recebidas</b>: número de citações recebidas pelo periódico</li>
      <li><b>Formas citadas</b>: título citado do periódico e número de vezes que foi identificado</li>
      <li><b>Lista de códigos de documentos citantes</b>: códigos identificadores dos documentos que citaram o periódico</li>
      <li><b>Lista de registros padronizados</b>: registros padronizados que citaram o periódico</li>
    </ol>

    <p>${_(u'Veja no final desta página os detalhes relacionados a cada tabela disponibilizada.')}</p>

    <p>
      ${_(u'Os dados resumidos de citações recebidas e concedidas de todos os periódicos podem ser obtidos em:')} <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/citatons_received.csv">citations_received.csv</a> e <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/citatons_granted.csv">citations_granted.csv</a>.
    </p>

    <p>${_(u'Os dados detalhados de todos os anos para o periódico selecionado podem ser obtidos em:')} <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/zips/${selected_journal_code}.zip">${selected_journal_code}.zip</a></p>

    <p>${_(u'Para obter os dados detalhados do periódico selecionado para um ano específico, indique esse ano no menu seguinte e acesse os endereços disponibilizados nas listas 1-5.')}</p>

    <%include file="bibliometrics_datepicker.mako"/>

    <h3>1. Citações concedidas</h3>
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a id="link_citations_granted_count" href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/${selected_journal_code}/${selected_journal_code}_citations_granted_count_${selected_year}.csv">${selected_journal_code}_citations_granted_count_${selected_year}.csv</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
      <li><b>${_(u'Última atualização')}:</b> 24/06/2022</li>
      <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Vírgula')}</li>
    </ul>

    <h3>2. Citações recebidas</h3>
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a id="link_citations_received_count" href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/${selected_journal_code}/${selected_journal_code}_citations_received_count_${selected_year}.csv">${selected_journal_code}_citations_received_count_${selected_year}.csv</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
      <li><b>${_(u'Última atualização')}:</b> 24/06/2022</li>
      <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Vírgula')}</li>
    </ul>

    <h3>3. Formas citadas</h3>
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a id="link_citations_received_cited_forms" href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/${selected_journal_code}/${selected_journal_code}_citations_received_cited_forms_${selected_year}.csv">${selected_journal_code}_citations_received_cited_forms_${selected_year}.csv</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
      <li><b>${_(u'Última atualização')}:</b> 24/06/2022</li>
      <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Vírgula')}</li>
    </ul>

    <h3>4. Lista de códigos de documentos citantes</h3>
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a id="link_citations_received_citing_pids" href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/${selected_journal_code}/${selected_journal_code}_citations_received_citing_pids_${selected_year}.csv">${selected_journal_code}_citations_received_citing_pids_${selected_year}.csv</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
      <li><b>${_(u'Última atualização')}:</b> 24/06/2022</li>
      <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Vírgula')}</li>
    </ul>

    <h3>5. Lista de registros padronizados</h3>
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a id="link_citations_received_standardized" href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/${selected_journal_code}/${selected_journal_code}_citations_received_standardized_${selected_year}.csv">${selected_journal_code}_citations_received_standardized_${selected_year}.csv</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
      <li><b>${_(u'Última atualização')}:</b> 24/06/2022</li>
      <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Vírgula')}</li>
    </ul>

    <h2>Descrição dos métodos utilizados para gerar os dados das tabelas disponibilizadas</h2>
    <p>As tabelas disponibilizadas nesta página utilizam como fonte de dados as referências citadas nos artigos publicados nos periódicos da Rede SciELO. Na prática isso significa que todas as referências são processadas e tratadas para permitir a correta associação entre um título citado e seu respectivo código ISSN-L. Esse tratamento implica em eliminar acentos e transformar para caixa-alta os títulos citados. Também são eliminados caracteres especiais como aspas, parenteses, entre outros. As sessões seguintes descrevem os detalhes relacionados a cada uma das cinco tabelas.</p>

    <h3>1. Citações concedidas</h3>

    <p>O arquivo de citações concedidas possui as seguintes colunas: "ISSN", "Título" e "Citações concedidas". Cada linha nesse arquivo registra um periódico citado e a última coluna representa o número de citações que lhe foram concedidas (isto é, quantas vezes o periódico selecionado no menu superior citou o periódico que consta na linha do arquivo). Nas situações em que a coluna que representa o código ISSN estiver vazia, significa que não foi possível identificar esse código para o título citado. A seguir é apresentado um exemplo fictício para o arquivo de citações concedidas pelo periódico "Revista de Microbiologia" (ISSN 0001-3714).</p>

    <table class="table table-striped table-bordered">
      <caption>Citações concedidas</caption>
      <thead>
        <tr>
          <th>ISSN</th>
          <th>Título</th>
          <th>Citações concedidas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>0001-3714</td><td>REVISTA DE MICROBIOLOGIA</td><td>37</td>
        </tr>
        <tr>
          <td>0370-4106</td><td>REVISTA CHILENA DE PEDIATRIA</td><td>1</td>
        </tr>
        <tr>
          <td>0036-4665</td><td>REVISTA DO INSTITUTO DE MEDICINA TROPICAL DE SAO PAULO</td><td>3</td>
        </tr>
      </tbody>
    </table>

    <h3>2. Citações recebidas</h3>
    <p>O arquivo de citações recebidas possui as seguintes colunas: "ISSN", "Título" e "Citações recebidas". Cada linha nesse arquivo registra um periódico citante e a última coluna representa o número de citações que o periódico concedeu (isto é, quantas vezes o periódico selecionado no menu superior foi citado pelo periódico que consta na linha do arquivo). A seguir é apresentado um exemplo fictício para o arquivo de citações recebidas pelo periódico "Revista de Microbiologia" (ISSN 0001-3714).</p>

    <table class="table table-striped table-bordered">
      <caption>Citações recebidas</caption>
      <thead>
        <tr>
          <th>ISSN</th>
          <th>Título</th>
          <th>Citações recebidas</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>0325-2957</td>
          <td>ACTA BIOQUÍMICA CLÍNICA LATINOAMERICANA</td>
          <td>85</td>
        </tr>
        <tr>
          <td>0567-7513</td>
          <td>ACTA GEOLÓGICA LILLOANA</td>
          <td>25</td>
        </tr>
        <tr>
          <td>0326-4815</td>
          <td>ACTA ODONTOLÓGICA LATINOAMERICANA</td>
          <td>14</td>
        </tr>
      </tbody>
    </table>

    <h3>3. Formas citadas</h3>
    <p>Para verificar como os periódicos têm sido citados nos registros de citação, o arquivo de formas citadas pode ser consultado. Nele a forma com que cada periódico é citado é apresentada por ordem de frequência. Assim, para cada periódico, as primeiras linhas indicam as formas mais comuns que os autores tem grafado os títulos do periódico (para o ano analisado). No arquivo disponibilizado há as seguintes colunas: "Título padronizado", "Título citado" e "Frequência". A primeira coluna representa o título padronizado pelos algoritmos de correção do método SciELO. A última representa o número de vezes que esse título foi citado nessa grafia. A seguir é apresentado um exemplo fictício para a Revista de Administração de Empresas (ISSN 0034-7590).</p>

    <table class="table table-striped table-bordered">
      <caption>Formas citadas</caption>
      <thead>
        <tr>
          <th>Título citado</th>
          <th>Título padronizado</th>
          <th>Frequência</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Revista de Administração de Empresas</td>
          <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>181</td>
        </tr>
        <tr>
          <td>RAE-Revista de Administração de Empresas</td>
          <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>39</td>
        </tr>
        <tr>
          <td>RAE - Revista de Administração de Empresas</td>
          <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>12</td>
        </tr>
        <tr>
          <td>RAE-revista de administração de empresas</td>
          <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>9</td>
        </tr>
        <tr>
          <td>RAE</td>
          <td>RAE</td>
          <td>7</td>
        </tr>
        <tr>
          <td>Rev Adm Empres</td>
          <td>REV ADM EMPRES</td>
          <td>2</td>
        </tr>
        <tr>
          <td>RAE: Revista de Administração de Empresas</td>
          <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>2</td>
        </tr>
        <tr>
          <td>Revista de Administração de Emprêsas</td>
          <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>1</td>
        </tr>
        <tr>
          <td>Revista de administração de empresas</td>
          <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
          <td>1</td>
        </tr>
      </tbody>
    </table>

    <h3>4. Documentos citantes</h3>
    <p>Também é possível verificar que documentos da Rede SciELO citaram os periódicos. Para isso, pode-se acessar o arquivo de lista de PIDs que contém todos os códigos identificadores que citaram o periódico analisado. Nesse arquivo há duas colunas, a saber: "PID e acrônimo de coleção" e "Ano do documento citante". A primeira coluna é formada por um identificador de documento e um acrônimo de coleção que, em conjunto, representam um documento único na Rede SciELO. Um exemplo fictício é apresentado a seguir para a Revista Brasileira de Gestão Urbana (ISSN 2175-3369).</p>

    <table class="table table-striped table-bordered">
      <caption>Documentos citantes</caption>
      <thead>
        <tr>
          <th>Código de documento citante</th>
          <th>Coleção de documento citante</th>
          <th>Ano do documento citado</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>S0001-37652020000501113</td>
          <td>scl</td>
          <td>2017</td>
        </tr>
        <tr>
          <td>S0011-52582020000100200</td>
          <td>scl</td>
          <td>1971</td>
        </tr>
        <tr>
          <td>S0031-10492020000100214</td>
          <td>scl</td>
          <td>1969</td>
        </tr>
        <tr>
          <td>S0034-71672020001800306</td>
          <td>scl</td>
          <td>2014</td>
        </tr>
        <tr>
          <td>S0034-75902020000100003</td>
          <td>scl</td>
          <td>2020</td>
        </tr>
        <tr>
          <td>S0034-75902020000100003</td>
          <td>scl</td>
          <td>2020</td>
        </tr>
        <tr>
          <td>S0034-75902020000100003</td>
          <td>scl</td>
          <td>2020</td>
        </tr>
        <tr>
          <td>S0034-75902020000100047</td>
          <td>scl</td>
          <td>2016</td>
        </tr>
        <tr>
          <td>S0034-75902020000100059</td>
          <td>scl</td>
          <td>2015</td>
        </tr>
      </tbody>
    </table>

    <h3>5. Registros padronizados</h3>
    <p>O arquivo mais detalhado que está disponibilizado nesse página é o que apresenta os registros de citação padronizados. Nesse arquivo há as seguintes colunas: "Código da coleção citante", "ISSN", "Código do documento citante", "Código da referência citada", "Ano da referência citação", "Título citado", "Volume citado" e "Código do método de correção". Por meio dele é possível identificar que documento ("Códigos de coleção e documento citantes) citou o periódico analisado ("ISSN" ou "Título citado"). A tabela seguinte apresenta um exemplo fictício para registros de citação da Revista de Administração de Empresas (ISSN 0034-7590).<p>

    <table class="table table-striped table-bordered">
      <caption>Registros padronizados</caption>
      <thead>
        <tr>
          <th>Código da coleção citante</th>
          <th>ISSN</th>
          <th>Código do documento citante</th>
          <th>Código da referência citada</th>
          <th>Ano da referência citação</th>
          <th>Titulo citado</th>
          <th>Volume citado</th>
          <th>Código do método de correção</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>scl</td>
          <td>0001-3765</td>
          <td>S0001-37652020000501113</td>
          <td>S0001-3765202000050111300004</td>
          <td>2017</td>
          <td>RAE-Revista Adm Empres</td>
          <td>57</td>
          <td>11</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0011-5258</td>
          <td>S0011-52582020000100200</td>
          <td>S0011-5258202000010020000019</td>
          <td>1971</td>
          <td>Revista de Administração de Empresas</td>
          <td>11</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0031-1049</td>
          <td>S0031-10492020000100214</td>
          <td>S0031-1049202000010021400022</td>
          <td>1969</td>
          <td>Revista de Administração de Empresas</td>
          <td>9</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7167</td>
          <td>S0034-71672020001800306</td>
          <td>S0034-7167202000180030600045</td>
          <td>2014</td>
          <td>Rev Adm Empres</td>
          <td>54</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7590</td>
          <td>S0034-75902020000100003</td>
          <td>S0034-7590202000010000300006</td>
          <td>2020</td>
          <td>Revista de Administração de Empresas</td>
          <td>60</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7590</td>
          <td>S0034-75902020000100003</td>
          <td>S0034-7590202000010000300010</td>
          <td>2020</td>
          <td>RAE-Revista de Administração de Empresas</td>
          <td>60</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7590</td>
          <td>S0034-75902020000100003</td>
          <td>S0034-7590202000010000300019</td>
          <td>2020</td>
          <td>RAE-Revista de Administração de Empresas</td>
          <td>60</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7590</td>
          <td>S0034-75902020000100047</td>
          <td>S0034-7590202000010004700007</td>
          <td>2016</td>
          <td>RAE-Revista de Administração de Empresas</td>
          <td>56</td>
          <td>0</td>
        </tr>
        <tr>
          <td>scl</td>
          <td>0034-7590</td>
          <td>S0034-75902020000100059</td>
          <td>S0034-7590202000010005900002</td>
          <td>2015</td>
          <td>RAE-Revista de Administração de Empresas</td>
          <td>55</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>

    <p>Também é possível observar qual foi o método utilizado para associar o título do periódico citado ao ISSN-L (vide o valor numérico que consta na última coluna da tabela apresentada anteriormente). Na situação mais simples, o título do periódico citado é associado ao seu respectivo código ISSN-L de forma exata, isto é, todos os caracteres grafados no registro da citação correspondem a um dos títulos oficiais, sem homônimos. Na situação mais complexa, o título é associado por meio de métodos e bases de correção que consideram o ano e volume indicados no registro da citação. A tabela seguinte apresenta uma descrição do significado de cada código de correção.</p>

    <table class="table table-striped table-bordered">
      <caption>Significado de códigos de correção</caption>
      <thead>
        <tr>
          <th>Código</th>
          <th>Estado</th>
          <th>Descrição</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>0</td><td>Sucesso</td><td>Ocorreu associação exata do título por meio de base de correção "Título para ISSN-L"</td></tr>
        <tr><td>1</td><td>Sucesso</td><td>Ocorreu associação exata do título com mais de um ISSN-L e foi possível decidir qual é o correto por meio de base de dados "TÍtulo-Ano-Volume para ISSN-L"</td></tr>
        <tr><td>2</td><td>Sucesso</td><td>Ocorreu associação exata do título com mais de um ISSN-L e foi possível decidir qual é o correto por meio de base de dados "TÍtulo-Ano-Volume para ISSN-L" e volume inferido</td></tr>
        <tr><td>3</td><td>Sucesso</td><td>Ocorreu associação exata do título com mais de um ISSN-L e foi possível decidir qual é o correto por meio de base artificial de dados "TÍtulo-Ano-Volume para ISSN-L"</td></tr>
        <tr><td>4</td><td>Sucesso</td><td>Ocorreu associação exata do título com mais de um ISSN-L e foi possível decidir qual é o correto por meio de base artificial de dados "TÍtulo-Ano-Volume para ISSN-L" e volume inferido</td></tr>
        <tr><td>11</td><td>Sucesso</td><td>Ocorreu associação aproximada do título com um ou mais códigos ISSN-L e foi possível decidir qual é o correto por meio de base de dados "TÍtulo-Ano-Volume para ISSN-L"</td></tr>
        <tr><td>12</td><td>Sucesso</td><td>Ocorreu associação aproximada do título com um ou mais códigos ISSN-L e foi possível decidir qual é o correto por meio de base de dados "TÍtulo-Ano-Volume para ISSN-L" e volume inferido</td></tr>
        <tr><td>13</td><td>Sucesso</td><td>Ocorreu associação aproximada do título com um ou mais códigos ISSN-L e foi possível decidir qual é o correto por meio de base artificial de dados "TÍtulo-Ano-Volume para ISSN-L"</td></tr>
        <tr><td>14</td><td>Sucesso</td><td>Ocorreu associação aproximada do título com um ou mais códigos ISSN-L e foi possível decidir qual é o correto por meio de base artificial de dados "TÍtulo-Ano-Volume para ISSN-L" e volume inferido</td></tr>
        <tr><td>519</td><td>Erro</td><td>Ocorreu associação exata do título, mas não foi possível decidir qual é o ISSN-L correto usando a base de dados "Título-Ano-Volume"</td></tr>
        <tr><td>529</td><td>Erro</td><td>Ocorreu associação exata do título, mas não foi possível decidir qual é o ISSN-L correto usando a base de dados "Título-Ano-Volume" e volume inferido</td></tr>
        <tr><td>539</td><td>Erro</td><td>Ocorreu associação exata do título, mas não foi possível decidir qual é o ISSN-L correto usando a base artificial de dados "Título-Ano-Volume"</td></tr>
        <tr><td>549</td><td>Erro</td><td>Ocorreu associação exata do título, mas não foi possível decidir qual é o ISSN-L correto usando a base artificial de dados "Título-Ano-Volume" e volume inferido</td></tr>
        <tr><td>619</td><td>Erro</td><td>Ocorreu associação aproximada do título, mas não foi possível decidir qual é o ISSN-L correto usando a base de dados "Título-Ano-Volume"</td></tr>
        <tr><td>629</td><td>Erro</td><td>Ocorreu associação aproximada do título, mas não foi possível decidir qual é o ISSN-L correto usando a base de dados "Título-Ano-Volume" e volume inferido</td></tr>
        <tr><td>639</td><td>Erro</td><td>Ocorreu associação aproximada do título, mas não foi possível decidir qual é o ISSN-L correto usando a base artificial de dados "Título-Ano-Volume"</td></tr>
        <tr><td>649</td><td>Erro</td><td>Ocorreu associação aproximada do título, mas não foi possível decidir qual é o ISSN-L correto usando a base artificial de dados "Título-Ano-Volume" e volume inferido</td></tr>
        <tr><td>500</td><td>Erro</td><td>Ocorreu associação exata do título com mais de um código ISSN-L, mas nenhuma base foi capaz de decidir qual é o correto</td></tr>
        <tr><td>600</td><td>Erro</td><td>Ocorreu associação aproximada do título com um ou mais códigos ISSN-L, mas nenhuma base foi capaz de validar qual é o correto</td></tr>
        <tr><td>70</td><td>Erro</td><td>Título não foi encontrado nas bases de dados</td></tr>
        <tr><td>80</td><td>Erro</td><td>Ocorreu associação exata do título com mais de um ISSN-L, mas não foi possível decidir qual é o correto, pois o ano informado é inválido</td></tr>
        <tr><td>81</td><td>Erro</td><td>Ocorreu associação aproximada do título com mais de um ISSN-L, mas não foi possível decidir qual é o correto, pois o ano informado é inválido</td></tr>
        <tr><td>82</td><td>Erro</td><td>O título não foi informado</td></tr>
        <tr><td>90</td><td>Ignorado</td><td>Não foi realizada tentativa de associar o título a um ISSN-L, pois existe código DOI</td></tr>
        <tr><td>91</td><td>Ignorado</td><td>Não foi realizada tentativa de associação de título aproximada devido à indicação do usuário</td></tr>
      </tbody>
    </table>
  </div>
  % endif
</%block>
