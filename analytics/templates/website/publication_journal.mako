## coding: utf-8
<%inherit file="central_container_for_journal_filters.mako"/>

<%block name="central_container">
    <div class="chart">
      <%include file="publication_journal_licenses.mako"/>
    </div>
    % if content_scope in ['network', 'collection']:
    <div class="chart">
      <%include file="publication_journal_subject_areas.mako"/>
    </div>
    % endif
    <div class="chart">
      <%include file="publication_journal_year.mako"/>
    </div>
    <div class="chart">
      <%include file="publication_journal_status.mako"/>
    </div>
</%block>

<%block name="extra_js">
</%block>