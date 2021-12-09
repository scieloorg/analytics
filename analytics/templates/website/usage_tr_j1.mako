## coding: utf-8
<div id="usage_tr_j1_chart" style="width:100%; height:400px;">
  <span id="loading_usage_tr_j1_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_usage_tr_j1_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('usage_title_report_chart')}?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&py_range=${'-'.join(py_range)}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#usage_tr_j1_chart').highcharts('StockChart', data['options']);
            $("#loading_usage_tr_j1_chart").hide();
        });
    });
</script>
