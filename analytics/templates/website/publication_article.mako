## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
    <div id="carousel-production" class="carousel slide" data-ride="carousel">
          <!-- Wrapper for slides -->
          <div class="carousel-inner" role="listbox">
            <div class="item active">
                <center>
                    <%include file="publication_article_licenses.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_subject_areas.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_document_type.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_languages.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_year.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_affiliations.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_authors.mako"/>
                </center>
            </div>
            <div class="item">
                <center>
                    <%include file="publication_article_references.mako"/>
                </center>
            </div>
          </div>
          <!-- Controls -->
          <a class="left carousel-control" href="#carousel-production" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">${_(u'anterior')}</span>
          </a>
          <a class="right carousel-control" href="#carousel-production" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">${_(u'próximo')}</span>
          </a>
    </div>
</%block>

<%block name="extra_js">
  <script language="javascript">
      $('#carousel-production').carousel({
        interval: false
      });
  </script>
</%block>