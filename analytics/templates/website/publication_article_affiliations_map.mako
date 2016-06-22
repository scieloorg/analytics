## coding: utf-8
<div id="article_affiliations_map" style="width:100%; height:400px;">
    <span id="loading_article_affiliations_map">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_article_affiliations_map").show();

    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_affiliations_map')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            data.options.series[0].mapData = Highcharts.maps['custom/world'];
            $('#article_affiliations_map').highcharts('Map', data['options']);
            $("#loading_article_affiliations_map").hide();
        });
    });
</script>
