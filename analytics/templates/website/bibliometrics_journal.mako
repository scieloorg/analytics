## coding: utf-8
<%inherit file="base.mako"/>

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
      <center>
        <div class="chart">
          <%include file="publication_article_citable_documents.mako"/>
        </div>
        <div class="chart">
          <%include file="bibliometrics_journal_self_citation.mako"/>
        </div>
      </center>  
  % endif
</%block>

<%block name="extra_js">
  <script>
    $('#tokenfield').tokenfield({
      'limit': 5
    })
  </script>
</%block>