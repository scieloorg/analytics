## coding: utf-8
<%inherit file="central_container_for_article_filters.mako"/>

<%block name="central_container">
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_licenses_publication_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por licença de uso e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. A disponibilidade de indicadores de licença de uso dependem da adoção da coleção ou periódico selecionado de licenças de uso creative commons.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_subject_areas_publication_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por área de atuação e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode fazer parte de mais de uma área de atuação. Este gráfico é recomendado para extração de indicadores de Coleção.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_document_type_publication_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por tipo de publicação e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_languages_publication_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por idioma de publicação e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode ser publicado em mais de um idioma.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="chart">
    <div class="row container-fluid">
      <div class="col-md-8">
        <%include file="publication_article_affiliations_publication_year.mako"/>
      </div>
      <div class="col-md-4">
        <div class="panel panel-info">
          <div class="panel-heading">
            <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
          </div>
          <div class="panel-body">
            ${_(u'Este gráfico apresenta a distribuição de documentos por país de afiliação dos autores e ano de publicação. Os números são relacionados a coleção ou ao periódico quando um periódico é selecionado. Os valores totais de documentos deste gráfico não podem ser considerados como totais de publicações da coleção uma vez que um documento pode ser publicado por mais de um país de afiliação.')}
          </div>
        </div>
      </div>
    </div>
  </div>
  % if not 'bibliometrics' in under_development:
    <div class="chart">
      <div class="row container-fluid">
        <div class="col-md-8">
          <%include file="publication_article_citable_documents.mako"/>
        </div>
        <div class="col-md-4">
          <div class="panel panel-info">
            <div class="panel-heading">
              <h3 class="panel-title">${_(u'Sobre o gráfico')}</h3>
            </div>
            <div class="panel-body">
                ${_(u'Este gráfico apresenta a distribuição de documentos citáveis e não citáveis relacionados ao periódico selecionado. De acordo com as regras de contagem do SciELO, documentos citáveis devem ser do tipo "Research Article", "Review Article", "Case Report", "Brief Report", "Rapid Communication" e "Article Commentary". Os demais tipos de documentos são considerados não citáveis.')}
            </div>
          </div>
        </div>
      </div>
    </div>
  % endif
</%block>

<%block name="extra_js">
</%block>