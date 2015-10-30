## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container">
    <div class="row container-fluid">
        <div class="col-md-3">
            <%include file="publication_size_journals.mako"/>
            <div class="panel panel-info">
              <div class="panel-heading">
                <h3 class="panel-title">${_(u'Sobre os números')}</h3>
              </div>
              <div class="panel-body">
                  ${_(u'Os números acima correspondem aos periódicos com pelo menos 1 fascículo e artigo publicados. Os números são definidos de acordo com os filtros aplicados através da interface.')}
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
                  ${_(u'Os números acima correspondem aos fascículos com pelo menos 1 artigo publicado. Os números são definidos de acordo com os filtros aplicados através da interface.')}
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
                  ${_(u'Os números acima correspondem ao número de documentos publicados. Os números são definidos de acordo com os filtros aplicados através da interface.')}
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
                  ${_(u'Os números acima correspondem ao número referências bibliográficas dos documentos publicados. Os números são definidos de acordo com os filtros aplicados através da interface.')}
              </div>
            </div>
        </div>
    </div>
</%block>

<%block name="extra_js">
</%block>