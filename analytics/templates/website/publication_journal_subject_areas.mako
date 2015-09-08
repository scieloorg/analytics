## coding: utf-8
<div id="subject_areas" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de área temática dos periódicos')}',
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
        
        var url =  "${request.route_url('publication_journal_subject_areas')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'Areas temáticas')}',
                    'align': 'high'
                }
            };
            $('#subject_areas').highcharts(options);
        });
    });
</script>
