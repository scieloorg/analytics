## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="article_year" style="width:100%; height:400px;">
        <span id="loading_article_year">
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
          ${_(u'Este gráfico apresenta o total de documentos publicados por ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_article_year").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_year')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#article_year').highcharts('StockChart', data['options']);
            $("#loading_article_year").hide();
        });
    });
</script>
