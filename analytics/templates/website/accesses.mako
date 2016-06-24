## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <center>
    <div class="chart">
      <%include file="access_by_month_and_year.mako"/>
    </div>
    <div class="chart">
      <%include file="access_lifetime.mako"/>
    </div>
    <div class="chart">
      <%include file="access_by_document_type.mako"/>
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>
