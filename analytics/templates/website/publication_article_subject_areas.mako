## coding: utf-8
<div id="article_subject_areas" style="width:100%; height:400px;">
    <span id="loading_subject_areas">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
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
