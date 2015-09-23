## coding: utf-8
<div id="article_affiliations" style="width:60%; height:400px;">
    <span id="loading_article_affiliations">
        <img src="/static/images/loading.gif" />
        <h5>${_(u'loading')}</h5>
    </span>
</div>
<script language="javascript">
    $("#loading_article_affiliations").show();
    $(document).ready(function() {
        var options = {
            'chart': {
                'type': 'column'
            },
            'title': {
                'text': '${_(u'Distribuição de países de afiliação dos documentos')}',
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
        
        var url =  "${request.route_url('publication_article_affiliations')}?code=${selected_code}&collection=${selected_collection_code}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories'],
                'title': {
                    'text': '${_(u'País de afiliação')}',
                    'align': 'high'
                }
            };
            $('#article_affiliations').highcharts(options);
            $("#loading_article_affiliations").hide();
        });
    });
</script>
