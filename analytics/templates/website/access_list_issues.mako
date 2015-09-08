## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>${_(u'Top 100 fascículos por número de acessos')}</h3>
  <table class="table">
    <tr>
      <th>${_(u'periódico')}</th>
      <th>html</th>
      <th>pdf</th>
      <th>epdf</th>
      <th>${_(u'resumo')}</th>
      <th>${_(u'total')}</th>
    </tr>
    % for item in aclist:
      <tr>
        <td>
          <a href="http://${selected_collection}/scielo.php?script=sci_issuetoc&amp;pid=${item['issue'][1:]}" target="_blank">
            <span class="glyphicon glyphicon-globe" />
          </a>
          ${item['issue']}
        </td>
        <td>${item['html']}</td>
        <td>${item['pdf']}</td>
        <td>${item['epdf']}</td>
        <td>${item['abstract']}</td>
        <td>${item['total']}</td>
      </tr>
    % endfor
  </table>
</%block>

<%block name="extra_js">

</%block>
