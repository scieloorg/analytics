## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  % if not selected_journal_code:
    <div class="panel panel-warning">
      <div class="panel-heading">
        <h3 class="panel-title">${_(u'Atenção')}</h3>
      </div>
      <div class="panel-body">
        ${_(u'É necessário selecionar um periódico para dados bibliométricos.')}
      </div>
    </div>
  % else:
      <div class="chart">
        <div class="row container-fluid">
          <div class="col-md-10">
            <%include file="bibliometrics_journal_received_citations_heat_chart.mako"/>
          </div>
          <div class="col-md-2">
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Este gráfico apresenta o número de citações recebidas por um determinado periódico. O corpus de citações corresponde a todas as coleções da Rede SciELO, coleções Temáticas e Independentes.')}
              </div>
            </div>
          </div>
        </div>
      </div>
      <h3>${_(u'Lista de citações para o eixo selecionado')}</h3>
      <div class="table">
        <div class="row container-fluid">          
          <div class="col-md-12">
            <table class="table table-bordered">
              <tr>
                <th colspan="3">${_(u'Citante')}</th>
                <th colspan="3">${_(u'Citado')}</th>
              </th>
              <tr>
                <th>${_(u'documento')}</th>
                <th>${_(u'periódico')}</th>
                <th>${_(u'ano de publicação')}</th>
                <th>${_(u'documento')}</th>
                <th>${_(u'periódico')}</th>
                <th>${_(u'ano de publicação')}</th>
              </th>
              % for item in citing_list:
                <tr>
                  <td><a href="http://${collections[item['citing_collection']]['domain']}/?script=sci_arttext&pid=${item['citing_pid']}" target="_blank">${item['citing_title']}</a></td>
                  <td>${item['citing_source']}</td>
                  <td>${item['citing_publication_year']}</td>
                  <td>${item['cited_title']}</td>
                  <td>${item['cited_source']}</td>
                  <td>${item['cited_publication_year']}</td>
                </tr>
              % endfor
              % if len(citing_list) == 0:
                <tr>
                  <td colspan="6">${_(u'Selecione um eixo x/y para obter a lista de citações para o período.')}</td>
              % endif              
            </table>
          </div>
        </div>
      </div>
  % endif
</%block>

<%block name="extra_js">
  <script>
    $('#tokenfield').tokenfield({
      'limit': 10,
      'delimiter': '||'
    });
    % if not selected_journal_code:
    $('#journal_selector_modal').modal();
    % endif
  </script>
</%block>