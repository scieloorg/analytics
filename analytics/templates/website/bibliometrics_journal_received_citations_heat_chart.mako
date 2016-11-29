## coding: utf-8
<div id="bibliometrics_journal_cited_and_citing_years_heat_chart" style="width:100%; height:400px;">
  <span id="bibliometrics_journal_cited_and_citing_years_heat_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_bibliometrics_journal_cited_and_citing_years_heat_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_cited_and_citing_years_heat')}?journal=${selected_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {

            data['options']['title'] = {'text': 'Citações recebidas pelo periódico'};
            data['options']['subtitle'] = {'text': '${selected_journal}'};
            data['options']['tooltip'] = {
                'formatter': function () {
                    return '${_(u"Documentos da Rede SciELO publicados em")} <b>' + this.series.xAxis.categories[this.point.x] + '</b> ${_(u"citaram")} <b>' + this.point.value + '</b> ${_(u"vezes os documentos do periódico")} <b>${selected_journal}</b> ${_(u"publicados em")} <b>' + this.series.yAxis.categories[this.point.y] +'<br/>${_(u"Clique no ponto para ver a lista de artigos.")}';
                }
            }

            data['options']['plotOptions']['series'] = {
                'cursor': 'pointer',
                'point': {
                    'events': {
                        'click': function() {
                            window.open('${request.route_url("bibliometrics_journal_cited_and_citing_years_heat_web")}?citing_year=' + this.series.xAxis.categories[this.x] + '&amp;cited_year=' + this.series.yAxis.categories[this.y], target='_self');
                        }
                    }
                }
            };

            Highcharts.chart('bibliometrics_journal_cited_and_citing_years_heat_chart', data['options']);
            $("#loading_bibliometrics_journal_cited_and_citing_years_heat_chart").hide();
        });
    });
</script>
