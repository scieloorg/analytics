## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="article_licenses_publication_year" style="width100%; height:400px;">
        <span id="loading_licenses_publication_year">
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
        ${_(u'Este gráfico apresenta a distribuição de documentos por licença de uso e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. A disponibilidade de indicadores de licença de uso dependem da adoção da coleção ou periódico selecionado de licenças de uso creative commons.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_licenses_publication_year").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_licenses_publication_year')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            $('#article_licenses_publication_year').highcharts('StockChart', data['options']);
            $("#loading_licenses_publication_year").hide();
        });
    });
</script>
