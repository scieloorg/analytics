## coding: utf-8
<div class="row container-fluid" style="padding-left: 30px;">
  <form class="form-inline">
    <div class="form-group">
      <label class="sr-only" for="exampleInputAmount">${_(u'Período')}</label>
      <div class="input-group">
        <div class="input-group-addon"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span></div>
        <input type="text" id="daterange" style="width: 180px; height: 30px;"/>
        <div class="input-group-addon"><a href="?range_start=${y3}&amp;range_end=${today}" data-toggle="tooltip" data-placement="bottom" title="${_(u'acessos nos últimos 36 meses')}">${_(u'3 anos')}</a></div>
        <div class="input-group-addon"><a href="?range_start=${y2}&amp;range_end=${today}" data-toggle="tooltip" data-placement="bottom" title="${_(u'acessos nos últimos 24 meses')}">${_(u'2 anos')}</a></div>
        <div class="input-group-addon"><a href="?range_start=${y1}&amp;range_end=${today}" data-toggle="tooltip" data-placement="bottom" title="${_(u'acessos nos últimos 12 meses')}">${_(u'1 ano')}</a></div>
        <div class="input-group-addon"><a href="?range_start=0&amp;range_end=${today}" data-toggle="tooltip" data-placement="bottom" title="${_(u'todos acessos disponíveis')}">${_(u'tudo')}</a></div>
        <div class="input-group-addon">
          <span class="glyphicon glyphicon-question-sign" data-toggle="popover" data-container="body" data-placement="bottom" title="${_(u'Seletor de período de acessos')}" data-content="${_(u'Utilize o campo com datas para selecionar um período customizado para recuperação dos dados de acesso. Você pode também selecionar o período de 1, 2 e 3 anos, através dos links rápidos ou todos os acessos disponíveis selecionando tudo.')}"></span>
        </div>
      </div>
    </div>
  </form>
</div>
<script language="javascript">
  $(function() {
    $('#daterange').daterangepicker(
      {
        'locale': {
          'format': 'YYYY-MM-DD'
        },
        'startDate': '${range_start}',
        'endDate': '${range_end}'
      },
      function(start, end, label) {
        window.open("?range_start="+start.format('YYYY-MM-DD')+"&range_end="+end.format('YYYY-MM-DD'), name="_self");
      }
    );
  });
</script>