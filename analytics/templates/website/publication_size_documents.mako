## coding: utf-8
<div id="size_documents">
    <h1 id="size_documents_value">
        <span id="loading_size_documents">
            <img src="/static/images/loading.gif" width="40px" />
            <h5>${_(u'Carregando')}</h5>
        </span>  
        <br/>
        <small>${_(u'Documentos')}</small>
    </h1>      
</div>
<script language="javascript">
    $("#loading_size_documents").show();
    $(document).ready(function() {
        var url =  "${request.route_url('publication_size')}?code=${selected_code}&collection=${selected_collection_code}&field=documents&callback=?";

        $.getJSON(url,  function(data) {
            $('#size_documents_value').prepend($.number(data['total']).replace(',', '.'));
            $("#loading_size_documents").hide();
        });
    });
</script>
