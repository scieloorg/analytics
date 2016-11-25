## coding: utf-8
<div id="selfcitation" style="width:100%; height:400px;">
  <span id="loading_selfcitation">
    <img src="/static/images/loading.gif" />
    <h5>${_(u'loading')}</h5>
  </span>
</div>
<script language="javascript">
    $("#loading_selfcitation").show();
    $(document).ready(function() {
        var url =  "${request.route_url('bibliometrics_journal_received_self_and_granted_citation_chart')}?journal=${selected_code}&collection=${selected_collection_code}&titles=${titles}&callback=?";

        $.getJSON(url,  function(data) {
            % if selected_journal:
                data['options']['subtitle'] = {'text': '${selected_journal}'};
            % endif
            $('#selfcitation').highcharts(data['options']);
            $("#loading_selfcitation").hide();
        });
    });
</script>
