## coding: utf-8
<div id="article_references" style="width:100%; height:400px;">
    <span id="loading_article_references">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
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
