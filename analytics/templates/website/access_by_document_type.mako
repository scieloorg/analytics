<h3>Total de accessos por tipo de documento</h3>
<div id="bydocumenttype" style="width:60%; height:400px;"></div>
<p>Total de acesso aos artigos por tipo de documento</p>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Total de accessos por ano, mês e tipo de documento',
            }
        };
        
        var url =  "http://localhost:6543/ajx/bydocumenttype?code=${selected_code}&collection=${selected_collection}&callback=?";
        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            $('#bydocumenttype').highcharts(options);
        });
    });
</script>
