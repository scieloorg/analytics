<div id="subject_areas" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Distribuição de área temática dos documentos',
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
        
        var url =  "/ajx/publication/article_subject_areas?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories']
            };
            $('#subject_areas').highcharts(options);
        });
    });
</script>
