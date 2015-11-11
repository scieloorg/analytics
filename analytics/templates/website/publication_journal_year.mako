## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="journal_year" style="width:100%; height:400px;">
        <span id="loading_journal_year">
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
          ${_(u'Este gráfico apresenta o número periódicos por ano de inclusão no SciELO. Este gráfico é recomendado para extração de indicadores de Coleção.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_journal_year").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_journal_year')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#journal_year').highcharts(data['options']);
            $("#loading_journal_year").hide();
        });
    });
</script>
