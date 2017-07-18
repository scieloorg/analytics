## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
  <h3>${_('Licenças de uso')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_licenses.mako"/>
      </div>  
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por licença de uso. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. A disponibilidade de indicadores de licença de uso dependem da adoção da coleção ou periódico selecionado de licenças de uso creative commons.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  % if content_scope in ['network', 'collection']:
  <h3>${_('Áreas temáticas')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_subject_areas.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta o total de documentos publicados por área de atuação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. As áreas de atuação são as grandes áreas do CNPQ, essas áreas são determinadas para cada um dos periódicos SciELO, podendo um periódico estar relacionado a mais de uma área de atuação. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode fazer parte de mais de uma área de atuação. Este gráfico é recomendado para extração de indicadores de Coleção.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  % endif
  <h3>${_('Tipos de documentos')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_document_type.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
              ${_(u'Este gráfico apresenta o total de documentos por tipo de documento. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os tipos de documento são os tipos utilizandos no SciELO Citation Index e documentados no SciELO Publishing Schema.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Idiomas dos documentos')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_languages.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta o total de documentos por idioma de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode ser publicado em mais de um idioma.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Anos de publicação')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
              ${_(u'Este gráfico apresenta o total de documentos publicados por ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Países de afiliação')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_affiliations.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
              ${_(u'Este gráfico apresenta o total de documentos por país de afiliação dos autores. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode ter mais um país de afiliação.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Mapa de países de afiliação')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_affiliations_map.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
              ${_(u'Este mapa apresenta o total de documentos por país de afiliação dos autores. Os valores totais de documentos deste mapa não podem ser considerados como totais de publicações da coleção uma vez que um documento pode ter mais um país de afiliação.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Número de autores')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_authors.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por número de autores. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <h3>${_('Número de referências bibliográficas')}</h3>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_references.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por número de referências bibliográficas. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
          </div>
        </div>
      </div>
    </div>
  </div>
</%block>

<%block name="extra_js">
</%block>