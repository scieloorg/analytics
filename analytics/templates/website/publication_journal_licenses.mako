## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="journal_licenses" style="width:100%; height:400px;">
        <span id="loading_licenses">
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
        ${_(u'Este gráfico apresenta o número de periódicos por licença de uso adotada. Os valores totais de periódicos deste gráfico não podem ser considerados como totais da coleção uma vez que um documento pode fazer parte de mais de uma área de atuação. Este gráfico é recomendado para extração de indicadores de Coleção.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_licenses").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_journal_licenses')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#journal_licenses').highcharts(data['options']);
            $("#loading_licenses").hide();
        });
    });
</script>
