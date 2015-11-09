## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="selfcitation" style="width:100%; height:400px;">
      <span id="loading_selfcitation">
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
          ${_(u'Este gráfico apresenta o número de citações concedidas, recebidas e auto citações do periódico selecionado, os dados estão distribuidos por ano de publicação.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_selfcitation").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_received_self_and_granted_citation_chart')}?code=${selected_code}&collection=${selected_collection_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {
            $('#selfcitation').highcharts(data['options']);
            $("#loading_selfcitation").hide();
        });
    });
</script>
