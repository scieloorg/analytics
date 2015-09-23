## coding: utf-8
<div id="journal_licenses" style="width:60%; height:400px;">
    <span id="loading_licenses">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_licenses").show();
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
            $('#journal_licenses').highcharts(options);
            $("#loading_licenses").hide();
        });
    });
</script>
