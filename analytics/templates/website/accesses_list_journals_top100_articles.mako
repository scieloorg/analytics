## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>${_(u'100 artigos mais acessados')}</h3>
  <table class="table">
    <tr>
      <th>${_(u'Periódico (ISSN)')}</th>
      <th>${_(u'Artigo (PID)')}</th>
      <th>${_(u'Ano de Publicação')}</th>
      <th>${_(u'Requisições Únicas')}</th>
      <th>${_(u'Requisições Totais')}</th>
      <th>${_(u'Investigações Únicas')}</th>
      <th>${_(u'Investigações Totais')}</th>
    </tr>
    % for item in usage:
      <tr>
        <td>
          <a href="http://${selected_collection['domain']}/scielo.php?script=sci_serial&amp;pid=${item['key_issn']}" target="_blank">
            <span class="glyphicon glyphicon-globe" />
          </a>
          <a href="${request.route_url('index_web')}?journal=${item['key_issn']}">
            ${item['key_issn']}
          </a>
        </td>
        <td>
          <a href="http://${selected_collection['domain']}/scielo.php?script=sci_article&amp;pid=${item['val']}" target="_blank">
            ${item['val']}
          </a>
        </td>
        <td>${item['yop']}</td>
        <td>${item['unique_item_requests_sum']}</td>
        <td>${item['total_item_requests_sum']}</td>
        <td>${item['unique_item_investigations_sum']}</td>
        <td>${item['total_item_investigations_sum']}</td>
      </tr>
    % endfor
  </table>
</%block>

<%block name="extra_js">

</%block>