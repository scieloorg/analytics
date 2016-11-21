## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <center>
    <div class="chart">
      <%include file="access_by_month_and_year.mako"/>
    </div>
  </center>
</%block>

<%block name="extra_js">
</%block>
