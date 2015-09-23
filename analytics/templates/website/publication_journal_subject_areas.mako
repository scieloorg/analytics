## coding: utf-8
<div id="journal_subject_areas" style="width:60%; height:400px;">
    <span id="loading_journal_subject_areas">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_journal_subject_areas").show();
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
            $('#journal_subject_areas').highcharts(options);
            $("#loading_journal_subject_areas").hide();
        });
    });
</script>
