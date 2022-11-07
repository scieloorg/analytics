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
    <h2>${_('Indicadores JCR')}</h2>
    <h5>${_(u'Dados extraídos em: ')} ${jct_extraction_date.strftime('%Y-%m-%d')}</h5>
    % if len(jcr) == 0:
      <div class="row">
        <div class="col-md-12">
          <h4>
            <small>${_(u'Não há indicadores JCR para este periódico')}</small>
          </h4>      
        </div>
      </div>    
    % else:
          <h3>${_(u'Fator de impacto')}</h3>
            <%include file="bibliometrics_journal_jcr_impact_factor.mako"/>
          <h3>${_(u'Fator de impacto (Média de percentil)')}</h3>
            <%include file="bibliometrics_journal_jcr_average_impact_factor_percentile.mako"/>
          <h3>${_(u'Citações Recebidas')}</h3>
            <%include file="bibliometrics_journal_jcr_received_citations.mako"/>
          <h3>${_(u'Eigen Factor')}</h3>
            <%include file="bibliometrics_journal_jcr_eigen_factor.mako"/>
          <h3>${_(u'Dados de todos os anos')}</h3>
        % for year, data in sorted(jcr.items(), reverse=True):
          <h4>base year: ${ year }</h4>
          <div class="row">
            <div class="col-md-1">
                <h5>
                ${ data['total_cites'] }
                <br/>
                <small>${_(u'Total de citações')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['journal_impact_factor'] }
                <br/>
                <small>${_(u'FI 2 anos')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['impact_factor_without_journal_self_cites'] }
                <br/>
                <small>${_(u'FI 2 anos sem auto citações')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['five_year_impact_factor'] }
                <br/>
                <small>${_(u'FI 5 anos')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['immediacy_index'] }
                <br/>
                <small>${_(u'Indice de imediatez')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['citing_half_life'] }
                <br/>
                <small>${_(u'Vida média de citações')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['normalized_eigenfactor'] }
                <br/>
                <small>${_(u'Eigen Factor normalizado')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['average_journal_impact_factor_percentile'] }
                <br/>
                <small>${_(u'Percentíl de média de fator de FI de periódico')}</small>
                </h5>      
            </div>
            <div class="col-md-1">
                <h5>
                ${ data['percentage_articles_in_citable_items'] }
                <br/>
                <small>${_(u'Porcentagem de artigos em itens citáveis')}</small>
                </h5>      
            </div>
          </div>
        % endfor
    % endif
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