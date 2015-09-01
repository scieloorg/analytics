<h3>Total de accessos por ano e mês de acesso</h3>
<div id="bymonthandyear" style="width:60%; height:400px;"></div>
<p>Total de acesso aos artigos no contexto selecionado por ano e mês de acesso</p>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            title: {
                text: 'Total de accessos por ano e mês de aceasso',
            }
        };
        
        var url =  "http://localhost:6543/ajx/bymonthandyear?code=${selected_code}&collection=${selected_collection}&callback=?";

        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            options['xAxis'] = {
                'categories': data['categories']
            };
            $('#bymonthandyear').highcharts(options);
        });
    });
</script>
