## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
<div class="col-md-8">
  <h1>${_(u'Dados de citação')}</h1>

  <p>${_(u'O SciELO fornece um conjunto de tabelas com dados de citação relacionados a cada periódico. Essas tabelas são resultado de um processo computacional que transforma para códigos ISSN os títulos (em conjunto com outras informações) grafados nas referências citadas nos artigos da Rede SciELO. Esse processo é uma evolução daquele previamente existente e permitiu atualizar as contagens de citações para todos os periódicos. Ao todo são disponibilizadas cinco tabelas (arquivos em formato tabular) que contêm as seguintes informações:')}</p>

  <ol>
    <li><b>Citações concedidas</b>: número de citações concedidas pelo periódico, por ano</li>
    <li><b>Citações recebidas</b>: número de citações recebidas pelo periódico, por ano</li>
    <li><b>Formas citadas</b>: título citado e número de vezes que foi identificado</li>
    <li><b>Lista de PIDs citantes</b>: códigos identificadores dos documentos citantes</li>
    <li><b>Lista de registros corrigidos</b>: métodos de transformação de títulos para códigos ISSN</li>
  </ol>

  <p>${_(u'Veja no final desta página os detalhes relacionados a cada tabela disponibilizada.')}</p>

  <h3>1. Citações concedidas</h3>
  <ul>
    <li><b>${_(u'Nome do arquivo')}:</b> <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/journal_citations_granted_count/${selected_collection_code}_${selected_journal_code}.csv">citations_granted_${selected_collection_code}_${selected_journal_code}.csv</a></li>
    <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
    <li><b>${_(u'Última atualização')}:</b> 20/05/2022</li>
    <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Barra vertical')}</li>
  </ul>

  <h3>2. Citações recebidas</h3>
  <ul>
    <li><b>${_(u'Nome do arquivo')}:</b> <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/journal_citations_received_count.csv">citations_received.csv</a></li>
    <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
    <li><b>${_(u'Última atualização')}:</b> 20/05/2022</li>
    <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Barra vertical')}</li>
  </ul>

  <h3>3. Formas citadas</h3>
  <ul>
    <li><b>${_(u'Nome do arquivo')}:</b> <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/journal_cited_forms/${selected_collection_code}_${selected_journal_code}.csv">cited_forms_${selected_collection_code}_${selected_journal_code}.csv</a></li>
    <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
    <li><b>${_(u'Última atualização')}:</b> 20/05/2022</li>
    <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Barra vertical')}</li>
  </ul>

  <h3>4. Lista de PIDs</h3>
  <ul>
    <li><b>${_(u'Nome do arquivo')}:</b> <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/journal_citations_received_citing_pids/${selected_collection_code}_${selected_journal_code}.csv">citing_pids_${selected_collection_code}_${selected_journal_code}.csv</a></li>
    <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
    <li><b>${_(u'Última atualização')}:</b> 20/05/2022</li>
    <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Barra vertical')}</li>
  </ul>

  <h3>5. Lista de registros corrigidos</h3>
  <ul>
    <li><b>${_(u'Nome do arquivo')}:</b> <a href="https://storage.googleapis.com/scielo-datalake-gold/bibliometrics/journal_citations_correction_methods/${selected_collection_code}_${selected_journal_code}.csv">correction_methods_${selected_collection_code}_${selected_journal_code}.csv</a></li>
    <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'Trimestral')}</li>
    <li><b>${_(u'Última atualização')}:</b> 20/05/2022</li>
    <li><b>${_(u'Separador de colunas')}:</b> ${_(u'Barra vertical')}</li>
  </ul>

  <h2>Descrição dos métodos utilizados para gerar os dados das tabelas disponibilizadas</h2>
  <p>As tabelas disponibilizadas nesta página utilizam como fonte de dados as referências citadas nos artigos publicados nos periódicos da Rede SciELO. Na prática isso significa que todas as referências são processadas e tratadas para permitir a correta associação entre um título citado e seu respectivo código ISSN-L. Esse tratamento implica em eliminar acentos e transformar para caixa-alta os títulos citados. Também são eliminados caracteres especiais como aspas, parenteses, entre outros. As sessões seguintes descrevem os detalhes relacionados a cada uma das cinco tabelas.</p>

  <h3>1. Citações concedidas</h3>

  <p>O arquivo de citações concedidas possui as seguintes colunas: "ISSN", "Title" e "Total citations granted". Cada linha nesse arquivo é um periódico citado e a última coluna representa o número de citações que ocorreram (isto é, quantas vezes o periódico selecionado no menu superior citou o periódico que consta na linha do arquivo). Nas situações em que a coluna que representa o código ISSN estiver vazia, significa que não foi possível identificar esse código para o título citado. A seguir é apresentado um exemplo fictício para o arquivo de citações concedidas pelo periódico "Revista de Microbiologia" (ISSN 0001-3714).</p>

  <table class="table table-striped table-bordered">
    <caption>Citações concedidas</caption>
    <thead>
      <tr>
        <th>ISSN</th>
        <th>Title</th>
        <th>Total citations granted</th>
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
  <p>Já o arquivo de citações recebidas é único, isto é, é o mesmo para todas as coleções e periódicos selecionados. Trata-se de um arquivo composto pelas seguintes colunas: "Title", "Collection", "ISSNs", "1941", "1942", ..., "2020", "2021", "2022", "2023" e "Total citations received". Cada linha representa um periódico da Rede SciELO. As colunas de "1941" a "2022" representam os anos em que as citações foram recebidas. A última coluna representa o total de citações recebidas pelo periódico no período entre 1941 e 2023. A seguir é apresentado um exemplo fictício.</p>

  <table class="table table-striped table-bordered">
    <caption>Citações recebidas</caption>
    <thead>
      <tr>
        <th>Title</th>
        <th>Collection</th>
        <th>ISSNs</th>
        <th>2020</th>
        <th>2021</th>
        <th>Total citations received</th>
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
  <p>Para verificar como os periódicos têm sido citados nos registros de citação, o arquivo de formas citadas pode ser consultado. Nele a forma com que cada periódico é citado é apresentada por ordem de frequência. Assim, para cada periódico, as primeiras linhas indicam as formas mais comuns que os autores tem grafado os títulos do periódico. No arquivo disponibilizado há as seguintes colunas: "Standardized title", "Title" e "Frequency". A primeira coluna representa o título padronizado pelos algoritmos de correção do método SciELO. A última representa o número de vezes que esse título foi citado nessa grafia. A seguir é apresentado um exemplo fictício para a Revista de Administração de Empresas (ISSN 0034-7590).</p>

  <table class="table table-striped table-bordered">
    <caption>Formas citadas</caption>
    <thead>
      <tr>
        <th>Title Standardized</th>
        <th>Title</th>
        <th>Frequency</th>
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
  <p>Também é possível verificar que documentos da Rede SciELO citaram os periódicos. Para isso, pode-se acessar o arquivo de lista de PIDs que contém todos os códigos identificadores que citaram o periódico analisado. Nesse arquivo há duas colunas, a saber: "Collection" e "PID". Este último é um campo que, em conjunto com o acrônimo da coleção, identifica um arquivo na Rede SciELO. Um exemplo fictício é apresentado a seguir para a Revista Brasileira de Gestão Urbana (ISSN 2175-3369).</p>

  <table class="table table-striped table-bordered">
    <caption>Documentos citantes</caption>
    <thead>
      <tr>
        <th>PID and acronym</th>
        <th>Citing document year</th>
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
  <p>O arquivo mais detalhado que está disponibilizado nesse página é o que apresenta os métodos de correção utilizados para associar cada registro de citação a um periódico. Nesse arquivo há as seguintes colunas: "Collection", "Cited ISSN-L", "Citing PID", "Citing year", "Reference PID", "Cited year", "Cited journal" e "Correction method". Por meio dele é possível identificar que documento ("Collection" e "PID") citou o periódico analisado ("Cited ISSN-L" ou "Cited journal") e quando essa citação foi realizada ("Citing year").<p>

  <p>Também é possível observar qual foi o método utilizado para associar o título do periódico citado ao ISSN-L. Na situação mais simples, o título do periódico citado é associado ao seu respectivo código ISSN-L de forma exata, isto é, todos os caracteres grafados no registro da citação correspondem a um dos títulos oficiais, sem homônimos. Na situação mais complexa, o título é associado por meio de métodos e bases de correção que consideram o ano e volume indicados no registro da citação. A tabela apresenta a seguir ilustra um exemplo fictício para registros de citação da Revista Acta Cirúrgica Brasileira (ISSN 0102-8650).</p>

  <table class="table table-striped table-bordered">
    <caption>Métodos de correção</caption>
    <thead>
      <tr>
        <th>Collection</th>
        <th>Cited ISSN-L</th>
        <th>Citing PID</th>
        <th>Citing year</th>
        <th>Reference PID</th>
        <th>Cited year</th>
        <th>Cited journal</th>
        <th>Correction method</th>
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
        <td>success: exact match occurred through title-issnl correction base</td>
      </tr>
      <tr>
        <td>arg</td>
        <td>0102-8650</td>
        <td>S1851-300X2008000100005</td>
        <td>2008</td>
        <td>S1851-300X200800010000500001</td>
        <td>2006</td>
        <td>Acta Cir Bras</td>
        <td>success: exact match occurred through title-issnl correction base</td>
      </tr>
      <tr>
        <td>arg</td>
        <td>0102-8650</td>
        <td>S1852-48342012000300006</td>
        <td>2012</td>
        <td>S1852-4834201200030000600021</td>
        <td>2006</td>
        <td>Acta Cirurgica Brasileira.</td>
        <td>success: exact match occurred with more than one ISSN and it was possible to decide which one is the correct through year-volume correction base</td>
      </tr>
      <tr>
        <td>scl</td>
        <td>0102-8650</td>
        <td>S0102-695X2010000200011</td>
        <td>2010</td>
        <td>S0102-695X201000020001100007</td>
        <td>2000</td>
        <td>Acta Cirurgica Bras</td>
        <td>success: fuzzy match occurred and was validated through year-volume correction base</td>
      </tr>
      <tr>
        <td>scl</td>
        <td>0102-8650</td>
        <td>S0100-879X2004000700003</td>
        <td>2004</td>
        <td>S0100-879X200400070000300018</td>
        <td>2001</td>
        <td>Acta Cirúrgica Brasileira</td>
        <td>success: exact match occured with more than one ISSN and it was possible to decide which one is the correct through year-volume-inferred correction base</td>
      </tr>
    </tbody>
  </table>
</div>
</%block>
