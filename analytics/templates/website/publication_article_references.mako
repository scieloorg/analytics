## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="article_references" style="width: 100%; height:400px;">
        <span id="loading_article_references">
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
        ${_(u'Este gráfico apresenta a distribuição de documentos por número de referências bibliográficas. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_article_references").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_references')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            $('#article_references').highcharts(data['options']);
            $("#loading_article_references").hide();
        });
    });
</script>
