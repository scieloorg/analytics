## coding: utf-8
<div id="google_h5m5_chart" style="width:100%; height:400px;">
  <span id="loading_google_h5m5_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'Carregando')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_google_h5m5_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_google_h5m5_chart')}?journal=${selected_code}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            data.options.plotOptions.series = {
                'cursor': 'pointer',
                'point': {
                    'events': {
                        'click': function() {
                            window.open(this.ownURL);
                        }
                    }
                }
            };
            $('#google_h5m5_chart').highcharts(data['options']);
            $("#loading_google_h5m5_chart").hide();
        });
    });
</script>
