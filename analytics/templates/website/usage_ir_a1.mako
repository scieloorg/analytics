## coding: utf-8
<div id="usage_ir_a1_chart" style="width:100%; height:400px;">
  <span id="loading_usage_ir_a1_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'Carregando')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_usage_ir_a1_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('usage_report_chart')}?api_version=v2&report_code=ir_a1&pid=${selected_document_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_document_code:
                data['options']['subtitle'] = {'text': '${selected_document_code}'};
            % endif
            $('#usage_ir_a1_chart').highcharts('StockChart', data['options']);
            $("#loading_usage_ir_a1_chart").hide();
        });
    });
</script>
