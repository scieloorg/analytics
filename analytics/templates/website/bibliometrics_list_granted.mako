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
    <h3>${_(u'Citações concedidas por periódico')}</h3>
    <table class="table">
      <tr>
        <th>${_(u'título')}</th>
        <th>${_(u'total')}</th>
      </tr>
      <%total=0%>
      % for item in blist:
      <%total+=item['count']%>
        <tr>
          <td>${item['source']}</td>
          <td>${item['count']}</td>
        </tr>
      % endfor
        <tr>
          <th>${_(u'total')}</th>
          <th>${total}</th>
        </tr>        
      % if len(blist) == 0:
        <tr>
          <td colspan="2">${_(u'sem resultados')}</td>
        </tr>    
      % endif
    </table>  
  % endif
</%block>

<%block name="extra_js">
% if not selected_journal_code:
  <script>
    $('#journal_selector_modal').modal();
  </script>
% endif
</%block>
