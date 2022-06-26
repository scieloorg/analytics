## coding: utf-8
<div class="row container-fluid">
  <form class="form-inline">
    <div class="form-group">
      <div class="input-group">
        <label class="sr-only" for="seleted-year">Ano</label>
        <div class="input-group-addon">
          <span class="glyphicon glyphicon-calendar" aria-hidden="true"></span>
        </div>
        <input class="input-group-addon" id="selected-year" type="number" name="selected-year" min="1941" max="2023" value="2021"/>
        <div class="input-group-addon">
          <a href="#" onclick="updateData();" data-toggle="tooltip" data-placement="bottom" title="${_(u'Citações realizadas no ano selecionado')}">${_(u'aplicar')}</a>
        </div>
        <div class="input-group-addon">
          <span class="glyphicon glyphicon-question-sign" data-toggle="popover" data-container="body" data-placement="bottom" title="${_(u'Seletor de ano de citações')}" data-content="${_(u'Utilize o campo para selecionar o ano das citações e clique em aplicar para atualizar os links.')}"></span>
        </div>
      </div>
    </div>
  </form>
</div>

<script language="javascript">
function updateData() {
  csvLinks = ['link_citations_granted_count', 'link_citations_received_count', 'link_citations_received_cited_forms', 'link_citations_received_citing_pids', 'link_citations_received_standardized'];

  for (var i = 0; i < csvLinks.length; i++){
    changeLinkData(document.getElementById(csvLinks[i]));
  }
}

function changeLinkData(element){
  selected_year = document.getElementById("selected-year").value;
  element.text = element.text.slice(0, -8) + selected_year + '.csv';
  element.href = element.href.slice(0, -8) + selected_year + '.csv';
}
</script>
