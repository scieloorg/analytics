## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
  <%include file="access_datepicker.mako"/>
  <div id="carousel-accesses" class="carousel slide" data-ride="carousel">
    <!-- Wrapper for slides -->
    <div class="carousel-inner" role="listbox">
      <div class="item active">
        <center>
          <%include file="access_by_month_and_year.mako"/>
        </center>
      </div>
      <div class="item">
        <center>
          <%include file="access_lifetime.mako"/>
        </center>
      </div>
      <div class="item">
        <center>
          <%include file="access_by_document_type.mako"/>
        </center>
      </div>
    </div>
    <!-- Controls -->
    <a class="left carousel-control" href="#carousel-accesses" role="button" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
      <span class="sr-only">${_(u'anterior')}</span>
    </a>
    <a class="right carousel-control" href="#carousel-accesses" role="button" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
      <span class="sr-only">${_(u'próximo')}</span>
    </a>
  </div>
</%block>

<%block name="extra_js">
  <script language="javascript">
    $('#carousel-accesses').carousel({
      interval: false
    });
  </script>
</%block>
