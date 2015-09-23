## coding: utf-8
<div id="bydocumenttype" style="width:60%; height:400px;">
    <span id="loading_bydocumenttype">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_bydocumenttype").show();
    $(document).ready(function() {
        var options = {
            chart: {
                type: 'pie'
            },
            title: {
                text: '${_('Total de accessos por tipo de documento')}',
            }
        };
        
        var url =  "/ajx/accesses/bydocumenttype?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";
        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            $('#bydocumenttype').highcharts(options);
            $("#loading_bydocumenttype").hide();
        });
    });
</script>
