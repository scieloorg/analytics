## coding: utf-8
<div id="article_authors" style="width:100%; height:400px;">
    <span id="loading_article_authors">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_article_authors").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_authors')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#article_authors').highcharts(data['options']);
            $("#loading_article_authors").hide();
        });
    });
</script>
