## coding: utf-8
<div id="licenses" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de licença de uso dos periódicos')}',
            },
            'yAxis': {
                'title': {
                    'text': '${_(u'Número de periódicos')}'
                }
            },
            'legend': {
                'enabled': false
            }
        };
        
        var url =  "${request.route_url('publication_journal_licenses')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'Licenças de uso')}',
                    'align': 'high'
                }
            };
            $('#licenses').highcharts(options);
        });
    });
</script>
