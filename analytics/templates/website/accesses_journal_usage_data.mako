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
          ${_(u'É necessário selecionar um periódico para visualizar os relatórios de acesso disponíveis.')}
        </div>
      </div>
    </div>

  % else:
    <div class="col-md-8">
      <h1>${_(u'Dados de acessos')}</h1>

      <p>${_(u'O módulo Analytics do SciELO fornece para cada periódico um conjunto de tabelas em formato TSV ou JSON com métricas de acesso.')}</p>

      <p>${_(u'Essas tabelas são resultado de um processo computacional baseado no método COUNTER Release 5 e são disponibilizadas por meio da SciELO SUSHI API.')}</p>

      <p>${_(u'Para mais informações acerca desse método, acesse')} <a href="https://github.com/scieloorg/scielo-sushi-api/blob/master/docs/guide.md" target="_blank"> ${_(u'a documentação oficial da SciELO SUSHI API')}</a>.</p>

      <p>${_(u'Ao todo são disponibilizadas seis tabelas (arquivos em formato tabular).')}</p>
        
      <p>${_(u'Escolha um período e acesse os endereços indicados na coluna "Links" da tabela seguinte para obter os relatórios de acesso.')}</p>

      <%include file="access_datepicker.mako"/>

      <table class="table table-striped table-bordered" style="margin-top:20px;">
        <thead>
          <tr>
            <th>Nome</th>
            <th>Descrição</th>
            <th>Links</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Title Report J1</td>
            <td>Acessos mensais</td>
            <td>
              <a target="_blank" href="http://usage.apis.scielo.org/reports/tr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=tsv&api=v2&collection=${selected_collection_code}">Tabular</a> | <a target="_blank" href="http://usage.apis.scielo.org/reports/tr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=json&api=v2&collection=${selected_collection_code}">JSON</a>
            </td>
          </tr>
          <tr>
            <td>Language Report J1</td>
            <td>Acessos mensais agregados por idioma de documento</td>
            <td>
              <a target="_blank" href="http://usage.apis.scielo.org/reports/lr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=tsv&api=v2&collection=${selected_collection_code}">Tabular</a> | <a target="_blank" href="http://usage.apis.scielo.org/reports/lr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=json&api=v2&collection=${selected_collection_code}">JSON</a>
              </td>
          </tr>
          <tr>
            <td>Language Report J4</td>
            <td>Acessos mensais agregados por ano de publicação e idioma de documento</td>
            <td>
              <a target="_blank" href="http://usage.apis.scielo.org/reports/lr_j4?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=tsv&api=v2&collection=${selected_collection_code}">Tabular</a> | <a target="_blank" href="http://usage.apis.scielo.org/reports/lr_j4?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=json&api=v2&collection=${selected_collection_code}">JSON</a>
            </td>
          </tr>
          <tr>
            <td>Geolocation Report J1</td>
            <td>Acessos mensais agregados por país de origem de acesso</td>
            <td>
              <a target="_blank" href="http://usage.apis.scielo.org/reports/gr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=tsv&api=v2&collection=${selected_collection_code}">Tabular</a> | <a target="_blank" href="http://usage.apis.scielo.org/reports/gr_j1?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=json&api=v2&collection=${selected_collection_code}">JSON</a>
            </td>
          </tr>
          <tr>
            <td>Geolocation Report J4</td>
            <td>Acessos mensais agregados por país de origem de acesso e ano de publicação de documento</td>
            <td>
              <a target="_blank" href="http://usage.apis.scielo.org/reports/gr_j4?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=tsv&api=v2&collection=${selected_collection_code}">Tabular</a> | <a target="_blank" href="http://usage.apis.scielo.org/reports/gr_j4?begin_date=${range_start}&end_date=${range_end}&issn=${selected_journal_code}&fmt=json&api=v2&collection=${selected_collection_code}">JSON</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  % endif
</%block>