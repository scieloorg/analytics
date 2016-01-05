<div class="modal fade" id="journal_selector_modal" tabindex="-1" role="dialog" aria-labelledby="journal_selector_modal" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">${_(u'fechar')}</span></button>
        <h4 class="modal-title" id="myModalLabel">${_(u'selecionar periódico')}</h4>
      </div>
      <form role="form" method="GET">
        <div class="modal-body">
            ${_(u'selecionar um periódico')}:
            <select name="journal">
              % for issn, title in sorted(journals.items(), key=lambda x: x[1]):
                <option value="${issn}" ${'selected' if issn == selected_journal_code else ''}>${title}</option>
              % endfor
            </select>
            <input type="hidden" name="collection" value="${selected_collection_code}"/>
        </div>
        <div class="modal-footer">
          <button type="submit" class="btn btn-primary">${_(u'selecionar')}</button>
        </div>
      </form>
    </div>
  </div>
</div>