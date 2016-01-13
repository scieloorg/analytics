## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="citabledocuments" style="width:100%; height:400px;">
      <span id="loading_citabledocuments">
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
          ${_(u'Este gráfico apresenta a distribuição de documentos citáveis e não citáveis relacionados ao periódico selecionado. Entendesse por documentos citáveis, todos os documentos elegíveis para contagem de fator de impacto, esses documentos devem ser do tipo "Research Article" ou "Review Article". Os demais tipos de documentos são considerados não citáveis.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_citabledocuments").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_citable_documents')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#citabledocuments').highcharts('StockChart', data['options']);
            $("#loading_citabledocuments").hide();
        });
    });
</script>
