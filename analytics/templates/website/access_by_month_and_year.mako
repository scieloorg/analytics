<h3>Total de accessos por Mês ano e Ano</h3>
<p>Total de acesso aos artigos no contexto selecionado por mês e ano de acesso</p>
<div id="bymonthandyear" style="width:60%; height:400px;"></div>
<script language="javascript">
$(document).ready(function() {

    var options = {
        chart: {
            renderTo: 'container',
            type: 'spline'
        },
        series: [{}]
    };

    $.getJSON('data.json', function(data) {
        options.series[0].data = data;
        var chart = new Highcharts.Chart(options);
    });

});
</script>
