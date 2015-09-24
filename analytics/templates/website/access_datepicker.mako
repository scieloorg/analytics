## coding: utf-8
<div class="row container-fluid" style="padding-left: 30px;">
  <form class="form-inline">
    <div class="form-group">
      <label class="sr-only" for="exampleInputAmount">${_(u'Período')}</label>
      <div class="input-group">
        <div class="input-group-addon"><span class="glyphicon glyphicon-calendar" aria-hidden="true"></span></div>
        <input type="text" id="daterange" style="width: 180px; height: 30px;"/>
        <div class="input-group-addon"><a href="?range_start=${y3}&amp;range_end=${today}">${_(u'3 anos')}</a></div>
        <div class="input-group-addon"><a href="?range_start=${y2}&amp;range_end=${today}">${_(u'2 anos')}</a></div>
        <div class="input-group-addon"><a href="?range_start=${y1}&amp;range_end=${today}">${_(u'1 anos')}</a></div>
        <div class="input-group-addon"><a href="?range_start=0&amp;range_end=${today}">${_(u'tudo')}</a></div>
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