## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <h3>${_(u'Acessos aos periódicos por idioma de documento')}</h3>
  <table class="table">
    <tr>
      <th>${_(u'Periódico')}</th>
      <th>${_(u'Idioma de documento')}</th>
      <th class="text-right">${_(u'Requisições Únicas')}</th>
      <th class="text-right">${_(u'Requisições Totais')}</th>
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
        <td>${item['article_language_iso']}</td>
        <td class="text-right" data-value="${item['unique_item_requests']}">${'{:,.0f}'.format(item['unique_item_requests']).replace(',', '.')}</td>
        <td class="text-right" data-value="${item['total_item_requests']}">${'{:,.0f}'.format(item['total_item_requests']).replace(',', '.')}</td>
      </tr>
    % endfor
  </table>
</%block>

<%block name="extra_js">
<script>
  // Formata números com separador de milhar
  function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  }

  // Aplica formatação aos dados numéricos
  $(document).ready(function() {
    $('td[data-value]').each(function() {
      var value = parseInt($(this).data('value'));
      $(this).text(formatNumber(value));
    });
  });
</script>
</%block>