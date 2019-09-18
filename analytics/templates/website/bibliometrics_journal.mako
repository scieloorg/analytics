## coding: utf-8
<%inherit file="central_container_for_bibliometric_filters.mako"/>

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
      % if not 'bibliometrics' in under_development:
        <div class="row container-fluid">
          <form class="form-inline" method="GET">
              <label>Formas do título</label>
              <input type="text" name="titles" class="col-md-8" id="tokenfield" value="${titles}"/>
              <button type="submit" class="btn btn-default">${_(u'aplicar')}</button>
          </form>
        </div>
        <h3>${_(u'Impacto SciELO')}</h3>
        <div class="chart">
          <div class="row container-fluid">
            <div class="col-md-8">
              <%include file="bibliometrics_journal_impact_factor_chart.mako"/>
            </div>
            <div class="col-md-4">
              <div class="panel panel-info">
                <div class="panel-heading">
                  <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
                </div>
                <div class="panel-body">
                    ${_(u'Este gráfico apresenta a o fator de impacto do periódico selecionado considerando os períodos de imediatez, além de períodos de 1 a 5 anos. A linha de 2 anos equivale ao fator de impacto de periódicos da Thomson Reuters')}
                </div>
              </div>
            </div>
          </div>
        </div>
      % endif
      <h3>${_(u'Documentos citáveis e não citáveis')}</h3>
      <div class="chart">
        <div class="row container-fluid">
          <div class="col-md-8">
            <%include file="publication_article_citable_documents.mako"/>
          </div>
          <div class="col-md-4">
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Este gráfico apresenta a distribuição de documentos citáveis e não citáveis relacionados ao periódico selecionado. De acordo com as regras de contagem do SciELO, documentos citáveis devem ser do tipo "Research Article", "Review Article", "Case Report", "Brief Report", "Rapid Communication" e "Article Commentary". Os demais tipos de documentos são considerados não citáveis.')}
              </div>
            </div>
          </div>
        </div>
      </div>
      <h3>${_(u'Google H5M5')}</h3>
      <div class="chart">
        <div class="row container-fluid">
          <div class="col-md-8">
            <%include file="bibliometrics_journal_h5m5.mako"/>
          </div>
          <div class="col-md-4">
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Este gráfico apresenta os indices H5 e M5 do Google Scholar. Os indicadores são fornecidos anualmente pelo Google Scholar. A ausência de indicadores para um periódico ou para um período de um periódico pode ocorrer caso esses dados não tenham sido fornecidos pelo Google Scholar. Ao clicar na série, você será direcionado para o site do Google Scholar.')}
              </div>
            </div>
          </div>
        </div>
      </div>
      <h3>${_(u'Citações concedidas, recebidas e auto citação')}</h3>
      <div class="chart">
        <div class="row container-fluid">
          <div class="col-md-8">
            <%include file="bibliometrics_journal_received_self_and_granted_citation_chart.mako"/>
          </div>
          <div class="col-md-4">
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Este gráfico apresenta o número de citações concedidas, recebidas e auto citações do periódico selecionado, os dados estão distribuidos por ano de publicação.')}
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
