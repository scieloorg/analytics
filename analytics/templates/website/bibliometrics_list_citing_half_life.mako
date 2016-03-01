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
    <h3>${_(u'Vida media da citação')}</h3>
      <table class="table table-bordered table-citing-half-life">

      % for base_year, data in sorted(blist.items(), reverse=True):
        <% 
          base_year = int(base_year) 
        %>

        <tr>
          <th rowspan="2"></th>
          <th class="table-citing-half-life-header" colspan="10">${_(u'citações em')} ${base_year} ${_(u'para publicações de')}</th>
          <th class="table-citing-half-life-header">${_(u'Citação total')}</th>
          <th class="table-citing-half-life-header">${_(u'Vida media')}</th>
        </tr>
        <tr>
          % for reference_year in range(base_year, base_year - 10, -1):
            <% 
              reference_year = str(reference_year)
              data['data'].setdefault(reference_year, {'percentage': 0, 'citations': 0, 'accumulated_percentage': 0})
            %>
            <th class="${'success' if reference_year == data['half_life']['year'] else ''}">${reference_year}</th>
          % endfor
          <th class="citing-half-life-result" rowspan="4">${data['total']}</th>
          <th class="citing-half-life-result" rowspan="4">${'>10.0' if data['half_life']['value'] > 10 else '%.1f' % data['half_life']['value']}</th>
        </tr>
        <tr>
          <td class="table-citing-half-life-header">${_(u'citações')}</td>
          % for reference_year in range(base_year, base_year - 10, -1):
            <% 
              reference_year = str(reference_year)
            %>
            <td class="${'success' if reference_year == data['half_life']['year'] else ''}">${'-' if data['data'][reference_year]['citations'] == 0 else data['data'][reference_year]['citations']}</td>
          % endfor
        </tr>
        <tr>
          <td class="table-citing-half-life-header">${_(u'percentagem')}</td>
          % for reference_year in range(base_year, base_year - 10, -1):
            <% 
              reference_year = str(reference_year)
            %>
            <td class="${'success' if reference_year == data['half_life']['year'] else ''}">${'-' if data['data'][reference_year]['percentage'] == 0 else '%.1f %%' % data['data'][reference_year]['percentage']}</td>
          % endfor
        </tr>
        <tr>
          <td class="table-citing-half-life-header">${_(u'percentagem acumulado')}</td>
          % for reference_year in range(base_year, base_year - 10, -1):
            <% 
              reference_year = str(reference_year)
            %>
            <td class="${'success' if reference_year == data['half_life']['year'] else ''}">${'-' if data['data'][reference_year]['accumulated_percentage'] == 0 else '%.1f %%' % data['data'][reference_year]['accumulated_percentage']}</td>
          % endfor
        </tr>
      % endfor
      </table>
  % endif
</%block>

<%block name="extra_js">
  <script>
    $('#tokenfield').tokenfield({
      'limit': 10,
      'delimiter': '||'
    });
    % if not selected_journal_code:
    $('#journal_selector_modal').modal();
    % endif
  </script>
</%block>
