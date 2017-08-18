## coding: utf-8
<%inherit file="central_container_for_journal_filters.mako"/>

<%block name="central_container">
    <h3>${_(u'Licenças de uso dos periódicos')}</h3>
    <div class="chart">
      <%include file="publication_journal_licenses.mako"/>
    </div>
    % if content_scope in ['network', 'collection']:
    <h3>${_(u'Áreas temáticas dos periódicos')}</h3>
    <div class="chart">
      <%include file="publication_journal_subject_areas.mako"/>
    </div>
    % endif
    <h3>${_(u'Ano de inclusão de periódicos')}</h3>
    <div class="chart">
      <%include file="publication_journal_year.mako"/>
    </div>
    <h3>${_(u'Situação de publicação dos periódicos')}</h3>
    <div class="chart">
      <%include file="publication_journal_status.mako"/>
    </div>
</%block>

<%block name="extra_js">
</%block>