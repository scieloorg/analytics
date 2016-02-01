## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <div class="chart">
    <%include file="publication_article_licenses.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_subject_areas.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_document_type.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_languages.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_year.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_affiliations.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_affiliations_map.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_authors.mako"/>
  </div>
  <div class="chart">
    <%include file="publication_article_references.mako"/>
  </div>
</%block>

<%block name="extra_js">
</%block>