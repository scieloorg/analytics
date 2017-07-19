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
    <h3>${_('Indicadores Altmetric')}</h3>
    % if not altmetric:
      <div class="row">
        <div class="col-md-12">
          <h4>
            <small>${_(u'Não há indicadores Altmetric para este periódico')}</small>
          </h4>      
        </div>
      </div>    
    % endif
    % for timeframe, data in altmetric:
      <h4>time frame: ${ timeframe }</h4>
      % if not data:
        <div class="row">
          <div class="col-md-12">
            <h4>
              <small>${_(u'Não há indicadores Altmetric para este periódico neste timeframe')}</small>
            </h4>      
          </div>
        </div>    
      % else:
        <div class="row">
          <div class="col-md-2">
              <h5>
              ${ data['posts'] }
              <br/>
              <small>${_(u'Posts')}</small>
              </h5>      
          </div>
          <div class="col-md-2">
              <h5>
              ${ data['scores_sum'] }
              <br/>
              <small>${_(u'Soma de pontuação')}</small>
              </h5>      
          </div>
          <div class="col-md-2">
              <h5>
              ${ data['scores_median'] }
              <br/>
              <small>${_(u'Mediana de pontuação')}</small>
              </h5>      
          </div>
          <div class="col-md-2">
              <h5>
              ${ data['scores_in_timeframe_sum'] }
              <br/>
              <small>${_(u'Soma de pontuação no timeframe')}</small>
              </h5>      
          </div>
          <div class="col-md-2">
              <h5>
              ${ data['scores_in_timeframe_median'] }
              <br/>
              <small>${_(u'Mediana de pontuação no timeframe')}</small>
              </h5>      
          </div>
        </div>
      % endif
    % endfor
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