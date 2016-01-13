## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="article_licenses" style="width:100%; height:400px;">
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
        ${_(u'Este gráfico apresenta a distribuição de documentos por licença de uso. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. A disponibilidade de indicadores de licença de uso dependem da adoção da coleção ou periódico selecionado de licenças de uso creative commons.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_licenses").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_licenses')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            $('#article_licenses').highcharts(data['options']);
            $("#loading_licenses").hide();
        });
    });
</script>
