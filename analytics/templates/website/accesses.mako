<%inherit file="base.mako"/>

<%block name="central_container">
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
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
          <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
    </div>
</%block>

<%block name="extra_js">
  <script language="javascript">
      $('#carousel-example-generic').carousel({
        interval: false
      });
  </script>
</%block>
