## coding: utf-8
<div id="usage_cr_j1_chart" style="width:100%; height:400px;">
  <span id="loading_usage_cr_j1_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_usage_cr_j1_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('usage_report_chart')}?api_version=v2&report_code=cr_j1&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            $('#usage_cr_j1_chart').highcharts('StockChart', data['options']);
            $("#loading_usage_cr_j1_chart").hide();
        });
    });
</script>
