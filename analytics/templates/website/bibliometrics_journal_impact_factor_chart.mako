## coding: utf-8
<div id="impact_factor_chart" style="width:100%; height:400px;">
  <span id="loading_impact_factor_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_selfcitation").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_impact_factor_chart')}?journal=${selected_code}&collection=${selected_collection_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {
            $('#impact_factor_chart').highcharts(data['options']);
            $("#loading_impact_factor_chart").hide();
        });
    });
</script>
