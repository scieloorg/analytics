## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <div class="row container-fluid">
    <h3>${_(u'Citações Recebidas')} (${citedby['total']})</h3>
      <table class="table">
      <tr>
        <th>${_(u'ano de publicação')}</th>
        <th>${_(u'periódico')}</th>
        <th>${_(u'primeiro autor')}</th>
        <th>${_(u'título do documento')}</th>
      </tr>
      % for item in citedby['citedby']:
        <tr>
          <td>${item['code'][10:14]}</td>
          <td>${item['source']}</td>
          <td>
            ${item.get('first_author_lt', '')}
          </td>
          <td>
            <a href="${item['url']}" target="_blank">
              ${item['titles'][0]}
            </a> 
          </td>
        </tr>
      % endfor
      </table>
  </div>
</%block>