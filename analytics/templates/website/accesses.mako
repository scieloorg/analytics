## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <center>
    <div class="chart">
      % if selected_document_code:
          <h3>${_(u'Evolução de acessos ao documento')}</h3>
          <div class="col-md-12">
            <%include file="usage_ir_a1.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_ir_a1_yearly_total.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_ir_a1_yearly_unique.mako"/>
          </div>

      % elif selected_journal_code:
          <h3>${_(u'Evolução de acessos aos documentos do periódico')}</h3>
          <div class="col-md-12">
            <%include file="usage_tr_j1.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_tr_j1_yearly_total.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_tr_j1_yearly_unique.mako"/>
          </div>
          <div class="col-md-12" style="margin-top: 50px;">
            <%include file="usage_gr_j1.mako"/>
          </div>

      % else:
          <h3>${_(u'Evolução de acessos aos documentos da coleção')}</h3>
          <div class="col-md-12">
            <%include file="usage_cr_j1.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_cr_j1_yearly_total.mako"/>
          </div>
          <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_cr_j1_yearly_unique.mako"/>
          </div>

      % endif
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>
