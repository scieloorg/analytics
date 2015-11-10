## coding: utf-8
<div class="row container-fluid">
  <div class="col-md-8">
    <div id="article_subject_areas" style="width:100%; height:400px;">
        <span id="loading_subject_areas">
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
        ${_(u'Este gráfico apresenta o total de documentos publicados por área de atuação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. As áreas de atuação são as grandes áreas do CNPQ, essas áreas são determinadas para cada um dos periódicos SciELO, podendo um periódico estar relacionado a mais de uma área de atuação. Os valores totais de documentos deste gráfico não podem ser considerados como totais da coleção uma vez que um documento pode fazer parte de mais de uma área de atuação. Este gráfico é recomendado para extração de indicadores de Coleção.')}
      </div>
    </div>
  </div>
</div>
<script language="javascript">
    $("#loading_subject_areas").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_subject_areas')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#article_subject_areas').highcharts(data['options']);
            $("#loading_subject_areas").hide();
        });
    });
</script>
