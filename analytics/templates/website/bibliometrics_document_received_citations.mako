## coding: utf-8
<div id="document_received_citations">
    <h1 id="document_received_citations_value">
        <span id="loading_document_received_citations">
            <img src="/static/images/loading.gif" width="40px" />
            <h5>${_(u'loading')}</h5>
        </span>  
        <br/>
        <small>${_(u'citações recebidas')}</small>
    </h1>      
</div>
<script language="javascript">
    $("#loading_document_received_citations").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_document_received_citations')}?code=${selected_code}&callback=?";

        $.getJSON(url,  function(data) {
            $('#document_received_citations_value').prepend($.number(data['total']).replace(',', '.'));
            $("#loading_document_received_citations").hide();
        });
    });
</script>
