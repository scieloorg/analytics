## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
    <div class="row container-fluid">
        <div class="row">
            <h3>${_(u'Composição da coleção')}</h3>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_journals.mako"/>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_documents.mako"/>
        </div>
        <div class="col-md-4">
          <%include file="publication_size_citations.mako"/>
        </div>
    </div>
    <div class="row container-fluid" style="margin-top: 50px;">
        <div class="row">
            <h3>${_(u'Contagem de acessos')}</h3>
            <p class="text-info">${_(u'Os filtros para documentos não são aplicados aos gráficos de acessos.')}</p>
            <%include file="access_datepicker.mako"/>
        </div>
        <div class="col-md-12" style="margin-top: 30px;">
            <%include file="usage_cr_j1.mako"/>
        </div>
        <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_cr_j1_yearly_total.mako"/>
        </div>
        <div class="col-md-6" style="margin-top: 50px;">
            <%include file="usage_cr_j1_yearly_unique.mako"/>
        </div>
    </div>
    <div class="row container-fluid" style="margin-top: 50px;">
        <div class="row">
            <h3>${_(u'Distribuição de documentos por país de afiliação de autores')}</h3>
        </div>
        <div class="col-md-12" style="margin-top: 30px;">
            <%include file="publication_article_affiliations_map.mako"/>
        </div>
    </div>
</%block>
