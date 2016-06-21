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
      <div class="row container-fluid">
        <form class="form-inline" method="GET">
            <label>Formas do título</label>
            <input type="text" name="titles" class="col-md-8" id="tokenfield" value="${titles}"/>
            <button type="submit" class="btn btn-default">${_(u'aplicar')}</button>
        </form>
      </div>
      % if not 'bibliometrics' in under_development:
        <div class="chart">
          <%include file="publication_article_citable_documents.mako"/>
        </div>
        <div class="chart">
          <%include file="bibliometrics_journal_impact_factor_chart.mako"/>
        </div>
      % endif
      <div class="chart">
        <%include file="bibliometrics_journal_received_self_and_granted_citation_chart.mako"/>
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