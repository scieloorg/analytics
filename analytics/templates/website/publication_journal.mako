## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <center>
    <div class="chart">
      <%include file="publication_journal_licenses.mako"/>
    </div>
    <div class="chart">
      <%include file="publication_journal_subject_areas.mako"/>
    </div>
    <div class="chart">
      <%include file="publication_journal_year.mako"/>
    </div>
    <div class="chart">
      <%include file="publication_journal_status.mako"/>
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>