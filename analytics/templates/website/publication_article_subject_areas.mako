## coding: utf-8
<div id="article_subject_areas" style="width:60%; height:400px;">
    <span id="loading_subject_areas">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_subject_areas").show();
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de área temática dos documentos')}',
            },
            'yAxis': {
                'title': {
                    'text': '${_(u'Número de documentos')}'
                }
            },
            'legend': {
                'enabled': false
            }
        };
        
        var url =  "${request.route_url('publication_article_subject_areas')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'Areas temáticas')}',
                    'align': 'high'
                }
            };
            $('#article_subject_areas').highcharts(options);
            $("#loading_subject_areas").hide();
        });
    });
</script>
