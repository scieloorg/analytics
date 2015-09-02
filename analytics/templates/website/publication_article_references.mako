<div id="article_references" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Distribuição de número de referências bibliográficas dos documentos',
            },
            'yAxis': {
                'title': {
                    'text': 'Número de documentos'
                }
            },
            'legend': {
                'enabled': false
            }
        };
        
        var url =  "/ajx/publication/article_references?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories']
            };
            $('#article_references').highcharts(options);
        });
    });
</script>
