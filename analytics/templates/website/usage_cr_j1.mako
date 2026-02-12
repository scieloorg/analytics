## coding: utf-8
<div style="margin-bottom: 10px;">
  <small class="text-muted">
    ${_(u'Período')}: <strong>${range_start}</strong> ${_(u'a')} <strong>${range_end}</strong>
    <span style="margin-left: 15px;">
      <a href="${request.route_url('accesses_web')}?collection=${selected_collection_code}" class="btn btn-xs btn-default">
        <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span> ${_(u'Ver todos os períodos')}
      </a>
    </span>
  </small>
</div>
<div id="usage_cr_j1_chart" style="width:100%; height:400px;">
  <span id="loading_usage_cr_j1_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'Carregando')}</h5>
  </span>
</div>
<div id="usage_cr_j1_no_data_message" style="display:none; text-align:center; padding: 20px;">
  <p class="text-muted">
    <span class="glyphicon glyphicon-info-sign" aria-hidden="true"></span>
    ${_(u'Não há dados de acesso para o período selecionado')}.
  </p>
  <p>
    <a href="${request.route_url('accesses_web')}?collection=${selected_collection_code}&range_start=1998-01-01" class="btn btn-primary">
      <span class="glyphicon glyphicon-search" aria-hidden="true"></span> ${_(u'Ver dados históricos completos')}
    </a>
  </p>
</div>
<script language="javascript">
    $("#loading_usage_cr_j1_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('usage_report_chart')}?api_version=v2&report_code=cr_j1&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            // Check if there's any data in the series
            var hasData = false;
            if (data['options'] && data['options']['series']) {
                for (var i = 0; i < data['options']['series'].length; i++) {
                    if (data['options']['series'][i]['data'] && data['options']['series'][i]['data'].length > 0) {
                        hasData = true;
                        break;
                    }
                }
            }
            
            if (hasData) {
                $('#usage_cr_j1_chart').highcharts('StockChart', data['options']);
                $("#loading_usage_cr_j1_chart").hide();
            } else {
                // No data available - show helpful message
                $("#loading_usage_cr_j1_chart").hide();
                $('#usage_cr_j1_chart').hide();
                $('#usage_cr_j1_no_data_message').show();
            }
        });
    });
</script>
