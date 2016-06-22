## coding: utf-8
<div id="article_languages" style="width:100%; height:400px;">
    <span id="loading_article_languages">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_article_languages").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_languages')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#article_languages').highcharts(data['options']);
            $("#loading_article_languages").hide();
        });
    });
</script>
