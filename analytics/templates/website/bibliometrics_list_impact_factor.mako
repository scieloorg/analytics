## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  % if not selected_journal_code:
    <div class="panel panel-warning">
      <div class="panel-heading">
        <h3 class="panel-title">${_(u'Atenção')}</h3>
      </div>
      <div class="panel-body">
        ${_(u'É necessário selecionar um periódico para dados bibliométricos.')}
      </div>
    </div>
  % else:
    <div class="row container-fluid">
      <form class="form-inline" method="GET">
          <label>Formas do título</label>
          <input type="text" name="titles" class="col-md-8" id="tokenfield" value="${titles}"/>
          <button type="submit" class="btn btn-default">${_(u'aplicar')}</button>
      </form>
    </div>
    <h3>${_(u'Fator de Impacto em 1, 2, 3, 4 e 5 anos')}</h3>
      <table class="table table-bordered table-impact-factor">
      % for base_year, data in sorted(blist.items(), reverse=True):
        <% 
          base_year = int(base_year) 
          citing_count12 = int(data['citing_count1']+data['citing_count2'])
          citing_count123 = int(data['citing_count1']+data['citing_count2']+data['citing_count3'])
          citing_count1234 = int(data['citing_count1']+data['citing_count2']+data['citing_count3']+data['citing_count4'])
          citing_count12345 = int(data['citing_count1']+data['citing_count2']+data['citing_count3']+data['citing_count4']+data['citing_count5'])
          citable_docs12 = int(data['citable_docs1']+data['citable_docs2'])
          citable_docs123 = int(data['citable_docs1']+data['citable_docs2']+data['citable_docs3'])
          citable_docs1234 = int(data['citable_docs1']+data['citable_docs2']+data['citable_docs3']+data['citable_docs4'])
          citable_docs12345 = int(data['citable_docs1']+data['citable_docs2']+data['citable_docs3']+data['citable_docs4']+data['citable_docs5'])
        %>
        <tr>
          <th class="table-impact-factor-header" colspan="6">${_(u'citações em')} ${base_year} ${_(u'para publicações de')}</th>
          <th class="table-impact-factor-header" colspan="6">${_(u'documentos publicados em')}</th>
          <th class="table-impact-factor-header" colspan="5">${_(u'fator de impacto')}</th>
        </tr>
        <tr>
          <th class="success">${base_year-1}</th>
          <th class="success">${base_year-2}</th>
          <th>${base_year-3}</th>
          <th>${base_year-4}</th>
          <th>${base_year-5}</th>
          <th>${_(u'total')}</th>
          <th class="success">${base_year-1}</th>
          <th class="success">${base_year-2}</th>
          <th>${base_year-3}</th>
          <th>${base_year-4}</th>
          <th>${base_year-5}</th>
          <th>${_(u'total')}</th>
          <th>${_(u'1 ano')}</th>
          <th class="success">${_(u'2 ano')}</th>
          <th>${_(u'3 ano')}</th>
          <th>${_(u'4 ano')}</th>
          <th>${_(u'5 ano')}</th>
        </tr>
        <tr>
          <td class="success">${int(data['citing_count1'])}</td>
          <td class="success">${int(data['citing_count2'])}</td>
          <td>${int(data['citing_count3'])}</td>
          <td>${int(data['citing_count4'])}</td>
          <td>${int(data['citing_count5'])}</td>
          <td>${citing_count12345}</td>
          <td class="success">${int(data['citable_docs1'])}</td>
          <td class="success">${int(data['citable_docs2'])}</td>
          <td>${int(data['citable_docs3'])}</td>
          <td>${int(data['citable_docs4'])}</td>
          <td>${int(data['citable_docs5'])}</td>
          <td>${citable_docs12345}</td>
          <td>${data['fi1']}</td>
          <td class="success">${data['fi2']}</td>
          <td>${data['fi3']}</td>
          <td>${data['fi4']}</td>
          <td>${data['fi5']}</td>
        </tr>
      % endfor
      </table>
  % endif
</%block>

<%block name="extra_js">
  <script>
    $('#tokenfield').tokenfield({
      'limit': 5
    })
  </script>
</%block>
