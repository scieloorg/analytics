## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="document_type" style="width:100%; height:400px;">
        <span id="loading_document_type">
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
          ${_(u'Este gráfico apresenta o total de documentos por tipo de documento. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os tipos de documento são os tipos utilizandos no SciELO Citation Index e documentados no SciELO Publishing Schema.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_document_type").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_document_type')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#document_type').highcharts(data['options']);
            $("#loading_document_type").hide();
        });
    });
</script>
