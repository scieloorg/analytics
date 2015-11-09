## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="impact_factor_chart" style="width:100%; height:400px;">
      <span id="loading_impact_factor_chart">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
      </span>
    </div>
  </div>
  <div class="col-md-4">
    <div class="panel panel-info">
      <div class="panel-heading">
        <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
      </div>
      <div class="panel-body">
          ${_(u'Este gráfico apresenta a o fator de impacto do periódico selecionado considerando os períodos de imediatez, além de períodos de 1 a 5 anos. A linha de 2 anos equivale ao fator de impacto de periódicos da Thomson Reuters')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_selfcitation").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_impact_factor_chart')}?code=${selected_code}&collection=${selected_collection_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {
            $('#impact_factor_chart').highcharts(data['options']);
            $("#loading_impact_factor_chart").hide();
        });
    });
</script>
