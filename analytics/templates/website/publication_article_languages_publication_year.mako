## coding: utf-8
<div id="article_languages_publication_year" style="width: 100%; height:400px;">
    <span id="loading_languages_publication_year">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_languages_publication_year").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_languages_publication_year')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            $('#article_languages_publication_year').highcharts('StockChart', data['options']);
            $("#loading_languages_publication_year").hide();
        });
    });
</script>
