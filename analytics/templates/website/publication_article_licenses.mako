## coding: utf-8
<div id="article_licenses" style="width:60%; height:400px;">
    <span id="loading_licenses">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
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
