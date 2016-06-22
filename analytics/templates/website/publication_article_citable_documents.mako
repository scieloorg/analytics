## coding: utf-8
<div id="citabledocuments" style="width:100%; height:400px;">
  <span id="loading_citabledocuments">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
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
