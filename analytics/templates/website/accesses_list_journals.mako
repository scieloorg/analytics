## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>${_(u'Acessos aos documentos por periódico')}</h3>
  <table class="table">
    <tr>
      <th>${_(u'Periódico')}</th>
      <th>${_(u'Requisições Únicas')}</th>
      <th>${_(u'Requisições Totais')}</th>
    </tr>
    % for item in usage:
      <tr>
        <td>
          <a href="http://${selected_collection['domain']}/scielo.php?script=sci_serial&amp;pid=${item['issn']}" target="_blank">
            <span class="glyphicon glyphicon-globe" />
          </a>
          <a href="${request.route_url('index_web')}?journal=${item['issn']}">
            ${item['title']}
          </a>
        </td>
        <td>${item['unique_item_requests']}</td>
        <td>${item['total_item_requests']}</td>
      </tr>
    % endfor
  </table>
</%block>

<%block name="extra_js">

</%block>