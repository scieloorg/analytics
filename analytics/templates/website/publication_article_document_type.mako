## coding: utf-8
<div id="document_type" style="width:100%; height:400px;">
    <span id="loading_document_type">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_document_type").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_article_document_type')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#document_type').highcharts(data['options']);
            $("#loading_document_type").hide();
        });
    });
</script>
