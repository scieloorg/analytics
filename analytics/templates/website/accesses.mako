## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <center>
    <div class="chart">
      % if selected_journal_code:
      <h3>${_(u'Gráfico da evolução de acessos aos documentos')}</h3>
      <div class="col-md-12">
        <%include file="usage_tr_j1.mako"/>
      </div>
      <h3>${_(u'Mapa de acessos por país de origem')}</h3>
      <div class="col-md-12">
        <%include file="usage_gr_j1.mako"/>
      </div>
      % else:
      <h3>${_(u'Gráfico da evolução de acessos aos documentos da coleção')}</h3>
      <div class="col-md-12">
        <%include file="usage_cr_j1.mako"/>
      </div>
      % endif
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>
