<div id="journal_status" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': 'Distribuição de periódicos por situação atual de publicação no SciELO',
            },
            'yAxis': {
                'title': {
                    'text': 'Número de periódicos'
                }
            },
            'legend': {
                'enabled': false
            }
        };
        
        var url =  "${request.route_url('publication_journal_status')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': 'Situação da publicação',
                    'align': 'high'
                }
            };
            $('#journal_status').highcharts(options);
        });
    });
</script>
