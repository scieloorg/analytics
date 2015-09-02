<div id="bydocumenttype" style="width:60%; height:400px;"></div>
<script language="javascript">
    $(document).ready(function() {
        var options = {
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Total de accessos por tipo de documento',
            }
        };
        
        var url =  "/ajx/accesses/bydocumenttype?code=${selected_code}&collection=${selected_collection_code}&callback=?";
        $.getJSON(url,  function(data) {
            options['series'] = data['series'];
            $('#bydocumenttype').highcharts(options);
        });
    });
</script>
