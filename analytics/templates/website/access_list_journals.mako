## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>${_(u'Acessos documentos por periódicos')}</h3>
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
          <a href="http://${selected_collection}/scielo.php?script=sci_serial&amp;pid=${item['issn']}" target="_blank">
            <span class="glyphicon glyphicon-globe" />
          </a>
          <a href="${request.route_url('accesses_bymonthandyear')}?journal=${item['issn']}">
            ${item['title']}
          </a>
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
