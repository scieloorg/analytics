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
  % endif
  <h3>${_(u'Top 100 Citações concedidas')}</h3>
  <table class="table">
    <tr>
      <th>${_(u'título')}</th>
      <th>${_(u'total')}</th>
    </tr>
    % for item in blist:
      <tr>
        <td>${item['source']}</td>
        <td>${item['count']}</td>
      </tr>
    % endfor
    % if len(blist) == 0:
      <tr>
        <td colspan="2">${_(u'sem resultados')}</td>
      </tr>    
    % endif
  </table>
</%block>

<%block name="extra_js">

</%block>
