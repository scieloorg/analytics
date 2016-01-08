## coding: utf-8
<div id="bymonthandyear" style="width:60%; height:400px;">
    <span id="loading_bymonthandyear">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_bymonthandyear").show();
    $(document).ready(function() {
        var url =  "/ajx/accesses/bymonthandyear?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            $('#bymonthandyear').highcharts('StockChart', data['options']);
            $("#loading_bymonthandyear").hide();
        });
    });
</script>
