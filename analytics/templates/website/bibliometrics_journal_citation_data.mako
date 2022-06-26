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

    <p>${_(u'O módulo Analytics do SciELO fornece para cada periódico um conjunto de tabelas no formato CSV com o número de citações recebidas de periódicos da Rede SciELO e número de citações concedidas a outros periódicos sem restrição. São consideradas somente citações de periódicos a cada periódico.')}</p>
    
    <p>${_(u'Essas tabelas são resultado de um processo computacional que transforma para códigos ISSN os títulos (em conjunto com outros dados) grafados nas referências citadas nos artigos da Rede SciELO. Esse processo é uma evolução daquele previamente existente e permitiu atualizar as contagens de citações para todos os periódicos.')}</p>

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
  <p>Já o arquivo de citações recebidas é único, isto é, é o mesmo para todas as coleções e periódicos selecionados. Trata-se de um arquivo composto pelas seguintes colunas: "Título", "Coleção", "ISSNs", "1941", "1942", ..., "2020", "2021", "2022", "2023" e "Citações recebidas". Cada linha representa um periódico da Rede SciELO. As colunas de "1941" a "2022" representam os anos em que as citações foram recebidas. A última coluna representa o total de citações recebidas pelo periódico no período entre 1941 e 2023. A seguir é apresentado um exemplo fictício de tabela de citações recebidas.</p>

  <table class="table table-striped table-bordered">
    <caption>Citações recebidas</caption>
    <thead>
      <tr>
        <th>Título</th>
        <th>Coleção</th>
        <th>ISSNs</th>
        <th>2020</th>
        <th>2021</th>
        <th>Citações recebidas</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>ACTA BIOQUÍMICA CLÍNICA LATINOAMERICANA</td>
        <td>arg</td>
        <td>0325-2957#1851-6114</td>
        <td>75</td>
        <td>85</td>
        <td>160</td>
      </tr>
      <tr>
        <td>ACTA GEOLÓGICA LILLOANA</td>
        <td>arg</td>
        <td>0567-7513#1852-6217</td>
        <td>10</td>
        <td>25</td>
        <td>35</td>
      </tr>
      <tr>
        <td>ACTA ODONTOLÓGICA LATINOAMERICANA</td>
        <td>arg</td>
        <td>0326-4815#1852-4834</td>
        <td>13</td>
        <td>14</td>
        <td>27</td>
      </tr>
    </tbody>
  </table>

  <h3>3. Formas citadas</h3>
  <p>Para verificar como os periódicos têm sido citados nos registros de citação, o arquivo de formas citadas pode ser consultado. Nele a forma com que cada periódico é citado é apresentada por ordem de frequência. Assim, para cada periódico, as primeiras linhas indicam as formas mais comuns que os autores tem grafado os títulos do periódico. No arquivo disponibilizado há as seguintes colunas: "Título padronizado", "Título citado" e "Frequência". A primeira coluna representa o título padronizado pelos algoritmos de correção do método SciELO. A última representa o número de vezes que esse título foi citado nessa grafia. A seguir é apresentado um exemplo fictício para a Revista de Administração de Empresas (ISSN 0034-7590).</p>

  <table class="table table-striped table-bordered">
    <caption>Formas citadas</caption>
    <thead>
      <tr>
        <th>Título padronizado</th>
        <th>Título citado</th>
        <th>Frequência</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>Revista de Administração de Empresas</td>
        <td>3822</td>
      </tr>
      <tr>
        <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>RAE-Revista de Administração de Empresas</td>
        <td>612</td>
      </tr>
      <tr>
        <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>RAE - Revista de Administração de Empresas</td>
        <td>260</td>
      </tr>
      <tr>
        <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>RAE-revista de administração de empresas</td>
        <td>118</td>
      </tr>
      <tr>
        <td>RAE</td>
        <td>RAE</td>
        <td>95</td>
      </tr>
      <tr>
        <td>REV ADM EMPRES</td>
        <td>Rev Adm Empres</td>
        <td>72</td>
      </tr>
      <tr>
        <td>RAE REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>RAE: Revista de Administração de Empresas</td>
        <td>38</td>
      </tr>
      <tr>
        <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>Revista de Administração de Emprêsas</td>
        <td>37</td>
      </tr>
      <tr>
        <td>REVISTA DE ADMINISTRACAO DE EMPRESAS</td>
        <td>Revista de administração de empresas</td>
        <td>35</td>
      </tr>
    </tbody>
  </table>

  <h3>4. Lista de PIDs</h3>
  <p>Também é possível verificar que documentos da Rede SciELO citaram os periódicos. Para isso, pode-se acessar o arquivo de lista de PIDs que contém todos os códigos identificadores que citaram o periódico analisado. Nesse arquivo há duas colunas, a saber: "PID e acrônimo de coleção" e "Ano do documento citante". A primeira coluna é formada por um identificador de documento e um acrônimo de coleção que, em conjunto, representam um documento único na Rede SciELO. Um exemplo fictício é apresentado a seguir para a Revista Brasileira de Gestão Urbana (ISSN 2175-3369).</p>

  <table class="table table-striped table-bordered">
    <caption>Documentos citantes</caption>
    <thead>
      <tr>
        <th>PID e acrônimo de coleção</th>
        <th>Ano do documento citante</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>S2175-3369201300020000500002-scl</td>
        <td>2013</td>
      </tr>
      <tr>
        <td>S1414-753X201400040001000013-scl</td>
        <td>2014</td>
      </tr>
      <tr>
        <td>S1645-3794201400010000500019-prt</td>
        <td>2014</td>
      </tr>
      <tr>
        <td>S2236-9996201400020048700038-scl</td>
        <td>2014</td>
      </tr>
      <tr>
        <td>S2314-0208201400010000300004-arg</td>
        <td>2014</td>
      </tr>
      <tr>
        <td>S1984-2201201500040015900011-scl</td>
        <td>2015</td>
      </tr>
      <tr>
        <td>S0718-3402201500020000300018-chl</td>
        <td>2015</td>
      </tr>
    </tbody>
  </table>

  <h3>5. Lista de registros corrigidos</h3>
  <p>O arquivo mais detalhado que está disponibilizado nesse página é o que apresenta os métodos de correção utilizados para associar cada registro de citação a um periódico. Nesse arquivo há as seguintes colunas: "Coleção", "ISSN-L citado", "PID do documento citante", "Ano do documento citante", "PID da referência citada", "Ano da citação", "Título citado" e "Código do método de correção". Por meio dele é possível identificar que documento ("Coleção" e "PID do documento citante") citou o periódico analisado ("ISSN-L citado" ou "Título citado") e quando essa citação foi realizada ("Ano da citação"). A tabela seguinte apresenta um exemplo fictício para registros de citação da Revista Acta Cirúrgica Brasileira (ISSN 0102-8650).<p>

  <table class="table table-striped table-bordered">
    <caption>Métodos de correção</caption>
    <thead>
      <tr>
        <th>Coleção</th>
        <th>ISSN-L citado</th>
        <th>PID do documento citante</th>
        <th>Ano do documento citante</th>
        <th>PID da referência citada</th>
        <th>Ano da citação</th>
        <th>Titulo citado</th>
        <th>Código do método de correção</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>arg</td>
        <td>0102-8650</td>
        <td>S0025-76802008000200005</td>
        <td>2008</td>
        <td>S0025-7680200800020000500008</td>
        <td>2006</td>
        <td>Acta Cir Bras</td>
        <td>0</td>
      </tr>
      <tr>
        <td>arg</td>
        <td>0102-8650</td>
        <td>S1851-300X2008000100005</td>
        <td>2008</td>
        <td>S1851-300X200800010000500001</td>
        <td>2006</td>
        <td>Acta Cir Bras</td>
        <td>0</td>
      </tr>
      <tr>
        <td>arg</td>
        <td>0102-8650</td>
        <td>S1852-48342012000300006</td>
        <td>2012</td>
        <td>S1852-4834201200030000600021</td>
        <td>2006</td>
        <td>Acta Cirurgica Brasileira.</td>
        <td>1</td>
      </tr>
      <tr>
        <td>scl</td>
        <td>0102-8650</td>
        <td>S0102-695X2010000200011</td>
        <td>2010</td>
        <td>S0102-695X201000020001100007</td>
        <td>2000</td>
        <td>Acta Cirurgica Bras</td>
        <td>3</td>
      </tr>
      <tr>
        <td>scl</td>
        <td>0102-8650</td>
        <td>S0100-879X2004000700003</td>
        <td>2004</td>
        <td>S0100-879X200400070000300018</td>
        <td>2001</td>
        <td>Acta Cirúrgica Brasileira</td>
        <td>4</td>
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
</%block>
