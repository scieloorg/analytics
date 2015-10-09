## coding: utf-8
<ul id="lifetime" style="width: 60%; list-style-type: none; padding: 0px; margin: 0px;"></ul>
<span id="loading_lifetime">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
</span>
<script language="javascript">
    $("#loading_lifetime").show();
    $(document).ready(function() {
        var url =  "/ajx/accesses/lifetime?code=${selected_code}&collection=${selected_collection_code}&range_start=${range_start}&range_end=${range_end}&callback=?";
        $.getJSON(url,  function(data) {
            for (item in data) {
                $('#lifetime').append('<li id="lifetime_'+item+'" style="height: 250px; margin-bottom: 100px; padding: 0px; margin: 0px;"></li>');
                $('#lifetime_'+item).highcharts(data[item]);
                $("#loading_lifetime").hide();
            };
        });
    });
</script>