## coding: utf-8
<div id="size_issue">
    <h1 id="size_issue_value">
        <span id="loading_size_issue">
            <img src="/static/images/loading.gif" width="40px" />
            <h5>${_(u'loading')}</h5>
        </span>
        <br/>
        <small>${_(u'fascículos')}</small>
    </h1>
</div>
<script language="javascript">
    $("#loading_size_issue").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_size')}?code=${selected_code}&collection=${selected_collection_code}&field=issue&callback=?";

        $.getJSON(url,  function(data) {
            $('#size_issue_value').prepend($.number(data['total']).replace(',', '.'));
            $("#loading_size_issue").hide();
        });
    });
</script>
