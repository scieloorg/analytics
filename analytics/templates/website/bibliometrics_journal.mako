## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <center>
    <div class="chart">
      <%include file="publication_article_citable_documents.mako"/>
    </div>
    <div class="chart">
      <%include file="bibliometrics_journal_self_citation.mako"/>
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>