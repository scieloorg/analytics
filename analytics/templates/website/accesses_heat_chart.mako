## coding: utf-8
<div id="accesses_heat_chart" style="width:100%; height:400px;">
  <span id="accesses_heat_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_accesses_heat_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('accesses_heat')}?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&py_range=${'-'.join(py_range)}&callback=?";

        $.getJSON(url,  function(data) {

            data['options']['title'] = {'text': "${_(u'Acessos aos documentos')}"};
            data['options']['subtitle'] = {'text': '${selected_journal or selected_collection["name"]}'};
            data['options']['tooltip'] = {
                'formatter': function () {
                    return '${_(u"Documentos publicados em")} <b>' + this.series.xAxis.categories[this.point.x] + '</b> ${_(u"tiveram")} <b>' + this.point.value + '</b> ${_(u"acessos em")} <b>' + this.series.yAxis.categories[this.point.y];
                }
            }

            Highcharts.chart('accesses_heat_chart', data['options']);
            $("#loading_accesses_heat_chart").hide();
        });
    });
</script>
