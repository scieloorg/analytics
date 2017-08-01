## coding: utf-8
<div id="bymonthandyear" style="width:100%; height:400px;">
    <span id="loading_bymonthandyear">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_bymonthandyear").show();
    $(document).ready(function() {
        var url =  "${request.route_url('accesses_bymonthandyear')}?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&py_range=${'-'.join(py_range)}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#bymonthandyear').highcharts('StockChart', data['options']);
            $("#loading_bymonthandyear").hide();
        });
    });
</script>
