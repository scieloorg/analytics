## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
    <div class="row container-fluid">
        <div class="row">
            <h3>${_(u'Composição da coleção')}</h3>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_issues.mako"/>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_documents.mako"/>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_citations.mako"/>
        </div>
    </div>
    <div class="row container-fluid" style="margin-top: 100px;">
        <div class="row">
            <h3>${_(u'Charts')}</h3>
        </div>
        <div class="col-md-6">
            <%include file="access_by_month_and_year.mako"/>
        </div>
        <div class="col-md-6">
            <%include file="publication_article_affiliations_map.mako"/>
        </div>
    </div>
</%block>
