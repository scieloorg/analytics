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
        var options = {
            'title': {
                'text': '${_(u'Total de acessos por ano e mês')}',
            },
            'yAxis': {
                'title': {
                    'text': '${_(u'Acessos')}'
                }
            }
        };
        
        var url =  "/ajx/accesses/bymonthandyear?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories']
            };
            $('#bymonthandyear').highcharts(options);
            $("#loading_bymonthandyear").hide();
        });
    });
</script>
