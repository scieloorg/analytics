## coding: utf-8
<div id="bymonthandyear" style="width:60%; height:400px;"></div>
<script language="javascript">
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
        });
    });
</script>
