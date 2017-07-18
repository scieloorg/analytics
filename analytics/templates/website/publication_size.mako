## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
    <h3>${_('Composição da coleção')}</h3>
    <div class="row container-fluid">
        <div class="col-md-3">
          <%include file="publication_size_journals.mako"/>
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">${_(u'Sobre os números')}</h3>
            </div>
            <div class="panel-body">
              ${_(u'Os números acima correspondem aos periódicos com pelo menos 1 fascículo e artigo publicados. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado na barra superior do site.')}
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <%include file="publication_size_issues.mako"/>
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">${_(u'Sobre os números')}</h3>
            </div>
            <div class="panel-body">
              ${_(u'Os números acima correspondem aos fascículos com pelo menos 1 artigo publicado. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado na barra superior do site.')}
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <%include file="publication_size_documents.mako"/>
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">${_(u'Sobre os números')}</h3>
            </div>
            <div class="panel-body">
              ${_(u'Os números a cima correspondem ao número de documentos publicados. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado na barra superior do site.')}
            </div>
          </div>
        </div>
        <div class="col-md-3">
          <%include file="publication_size_citations.mako"/>
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">${_(u'Sobre os números')}</h3>
            </div>
            <div class="panel-body">
              ${_(u'Os números acima correspondem ao número das referências bibliográficas citadas nos documentos publicados. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado na barra superior do site.')}
            </div>
          </div>
        </div>
    </div>
</%block>

<%block name="extra_js">
</%block>