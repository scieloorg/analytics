## coding: utf-8
<div id="article_references" style="width: 60%; height:400px;">
    <span id="loading_article_references">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_article_references").show();
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de número de referências bibliográficas dos documentos')}',
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
        var url =  "${request.route_url('publication_article_references')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'Referências bibliográficas')}',
                    'align': 'high'
                }
            };
            $('#article_references').highcharts(options);
            $("#loading_article_references").hide();
        });
    });
</script>
