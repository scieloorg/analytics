<div id="article_languages" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Distribuição de idiomas dos documentos',
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
        
        var url =  "${request.route_url('publication_article_languages')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': 'Idiomas de publicação',
                    'align': 'high'
                }
            };
            $('#article_languages').highcharts(options);
        });
    });
</script>
