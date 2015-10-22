## coding: utf-8
<div id="size_citations">
    <h1 id="size_citations_value">
        <span id="loading_size_citations">
            <img src="/static/images/loading.gif" width="40px" />
            <h5>${_(u'loading')}</h5>
        </span>
        <br/>
        <small>${_(u'referências')}</small>
    </h1>
</div>
<script language="javascript">
    $("#loading_size_citations").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_size')}?code=${selected_code}&collection=${selected_collection_code}&field=citations&callback=?";

        $.getJSON(url,  function(data) {
            $('#size_citations_value').prepend($.number(data['total']).replace(/,/gi, '.'));
            $("#loading_size_citations").hide();
        });
    });
</script>
