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
          <div class="col-md-12">
            <%include file="bibliometrics_journal_received_citations_heat_chart.mako"/>
          </div>
        </div>
      </div>
      <div class="chart">
        <div class="row container-fluid">          
          <div class="col-md-12">
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Este gráfico apresenta o número de citações recebidas por um determinado periódico. O corpus de citações corresponde a todas as coleções da Rede SciELO, coleções Temáticas e Independentes. Este gráfico utiliza os documentos publicados na Rede SciELO nos últimos 15 anos.')}
              </div>
            </div>
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