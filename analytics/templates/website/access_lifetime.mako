<h3>Vida útil de artigos</h3>
<p>Vida útil de artigos de acordo com acessos realizados aos artigos e o ano de publicação.</p>
<div id="lifetime" style="width:60%; height:400px;"></div>
<script>
    $(function () { 
        $('#lifetime').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Fruit Consumption'
            },
            xAxis: {
                categories: ['Apples', 'Bananas', 'Oranges']
            },
            yAxis: {
                title: {
                    text: 'Fruit eaten'
                }
            },
            series: [{
                name: 'Jane',
                data: [1, 0, 4]
            }, {
                name: 'John',
                data: [5, 7, 3]
            }]
        });
    });
</script>