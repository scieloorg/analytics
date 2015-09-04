<%inherit file="base.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>Acessos documentos por periódicos</h3>
  <table class="table">
    <tr>
      <th>periódico</th>
      <th>html</th>
      <th>pdf</th>
      <th>epdf</th>
      <th>abstract</th>
      <th>total</th>
    </tr>
    % for item in aclist:
      <tr>
        <td><a href="?journal=${item['issn']}">${item['title']}</a></td>
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
