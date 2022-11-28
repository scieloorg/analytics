## coding: utf-8
<div id="jcr_eigen_factor_chart" style="width:100%; height:400px;">
  <span id="loading_jcr_eigen_factor_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_jcr_eigen_factor_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_jcr_eigen_factor_chart')}?journal=${selected_code}&callback=?";
        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#jcr_eigen_factor_chart').highcharts(data['options']);
            $("#loading_jcr_eigen_factor_chart").hide();
        });
    });
</script>
