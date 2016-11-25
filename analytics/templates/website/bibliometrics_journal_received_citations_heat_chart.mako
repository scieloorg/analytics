## coding: utf-8
<div id="bibliometrics_journal_publication_and_citing_years_heat_chart" style="width:100%; height:400px;">
  <span id="bibliometrics_journal_publication_and_citing_years_heat_chart">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_bibliometrics_journal_publication_and_citing_years_heat_chart").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_publication_and_citing_years_heat')}?journal=${selected_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {

            data['options']['title'] = {'text': 'Citações recebidas pelo periódico (15 anos)'};
            data['options']['subtitle'] = {'text': '${selected_journal}'}
            data['options']['tooltip'] = {
                'formatter': function () {
                    return 'Documentos da Rede SciELO publicados em <b>' + this.series.xAxis.categories[this.point.x] + '</b> citaram <b>' +
                    this.point.value + '</b> vezes os documentos do periódico <b>${selected_journal}</b> publicados em <b>' + this.series.yAxis.categories[this.point.y];
                }
            }

            Highcharts.chart('bibliometrics_journal_publication_and_citing_years_heat_chart', data['options']);
            $("#loading_bibliometrics_journal_publication_and_citing_years_heat_chart").hide();
        });
    });
</script>
