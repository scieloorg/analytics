## coding: utf-8
<div id="journal_status" style="width:60%; height:400px;">
    <span id="loading_journal_status">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_journal_status").show();
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de periódicos por situação atual de publicação no SciELO')}',
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
        
        var url =  "${request.route_url('publication_journal_status')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'Situação da publicação')}',
                    'align': 'high'
                }
            };
            $('#journal_status').highcharts(options);
            $("#loading_journal_status").hide();
        });
    });
</script>
