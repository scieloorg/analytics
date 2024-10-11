## coding: utf-8
<div id="usage_gr_j1_chart" style="width:100%; height:400px;">
  <span id="loading_usage_gr_j1_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'Carregando')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_usage_gr_j1_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('usage_report_chart')}?api_version=v2&granularity=totals&report_code=gr_j1&code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            data.options.series[0].mapData = Highcharts.maps['custom/world'];
            $('#usage_gr_j1_chart').highcharts('Map', data['options']);
            $("#loading_usage_gr_j1_chart").hide();
        });
    });
</script>
