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
    <h3>${_(u'Formas de citação encontrada para o periódico selecionado')}</h3>
    <table class="table">
      <tr>
        <th>${_(u'título')}</th>
        <th>${_(u'total')}</th>
        <th>${_(u'ações')}</th>
      </tr>
      <%total=0%>
      % for item in blist:
        <%total+=item['count']%>
        <tr>
          <td>${item['source']}</td>
          <td>${item['count']}</td>
          <td>
            <a href="https://github.com/scieloorg/analytics/issues/new?labels=bug&amp;title=Título de periódico invalido em ${selected_journal} (${selected_journal_code}): ${item['source']}" target="_blank">
              <button type="button" class="btn btn-primary btn-xs"><span class="glyphicon glyphicon-envelope"></span> ${_(u'reportar erro')}</button>
            </a>
          </td>
        </tr>
      % endfor
        <tr>
          <th>${_(u'total')}</th>
          <th>${total}</th>
          <th></th>
        </tr>        
      % if len(blist) == 0:
        <tr>
          <td colspan="3">${_(u'sem resultados')}</td>
        </tr>    
      % endif
    </table>  
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
