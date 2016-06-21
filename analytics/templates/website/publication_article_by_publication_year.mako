## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
  <div class="chart">
    <%include file="publication_article_licenses_publication_year.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_subject_areas_publication_year.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_languages_publication_year.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_affiliations_publication_year.mako"/>
  </div>
  % if not 'bibliometrics' in under_development:
    <div class="chart">
      <%include file="publication_article_citable_documents.mako"/>
    </div>
  % endif
</%block>

<%block name="extra_js">
</%block>