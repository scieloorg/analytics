## coding: utf-8
<ul class="nav navbar-nav">
  <li class="${'active' if page == 'home' else ''}">
    <a href="${request.route_url('index_web')}"><span class="glyphicon glyphicon-home"></span> ${content_scope}</a>
  </li>
  <li class="${'active' if page == 'accesses' else ''}">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">${_(u'Acessos')} <span class="caret"></span></a>
    <ul class="dropdown-menu">
      <li><a href="${request.route_url('accesses_journal_usage_data_web')}">${_(u'Dados de acessos')}</a></li>
      <li><a href="${request.route_url('accesses_web')}">${_(u'Gráficos')}</a></li>
    </ul>
  </li>
  <li class="${'active' if page == 'publication' else ''}">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">${_(u'Publicação')} <span class="caret"></span></a>
    <ul class="dropdown-menu">
      <li><a href="${request.route_url('publication_size_web')}">${_(u'Composição da coleção')}</a></li>
      <li><a href="${request.route_url('publication_article_web')}">${_(u'Gráficos de documentos')}</a></li>
      <li><a href="${request.route_url('publication_article_web_by_publication_year')}">${_(u'Gráficos de documentos por ano de publicação')}</a></li>
    </ul>
  </li>
  <li class="${'active' if page == 'bibliometrics' else ''}">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">${_(u'Bibliometria')} <span class="caret"></span></a>
    <ul class="dropdown-menu">
      <li><a href="${request.route_url('bibliometrics_journal_citation_data_web')}">${_(u'Dados de citações')}</a></li>
      <li><a href="${request.route_url('bibliometrics_journal_web')}">${_(u'Gráficos')}</a></li>
      <li><a href="${request.route_url('bibliometrics_journal_altmetric')}">${_(u'Indicadores Altmetric')}</a></li>
      <li><a href="${request.route_url('bibliometrics_journal_jcr')}">${_(u'Indicadores JCR')}</a></li>
      <li><a href="${request.route_url('bibliometrics_journal_cited_and_citing_years_heat_web')}">${_(u'Gráfico de calor de citações recebidas')}</a></li>
      % if not 'bibliometrics' in under_development:
        <li><a href="${request.route_url('bibliometrics_list_impact_factor_web')}">${_(u'Impacto SciELO em 1, 2, 3, 4 e 5 anos')}</a></li>
        <li><a href="${request.route_url('bibliometrics_list_citing_half_life_web')}">${_(u'Vida media da citação')}</a></li>
      % endif
      <li><a href="${request.route_url('bibliometrics_list_granted_web')}">${_(u'Citações concedidas por periódicos')}</a></li>
      <li><a href="${request.route_url('bibliometrics_list_received_web')}">${_(u'Citações recebidas por periódicos')}</a></li>
      <li><a href="${request.route_url('bibliometrics_list_citing_forms_web')}">${_(u'Formas de citação do periódico')}</a></li>
      <li><a href="${request.route_url('bibliometrics_list_general_indicators_web')}">${_(u'Indicadores Gerais')}</a></li>
    </ul>
  </li>
  <%include file="navbar_common_links.mako"/>
</ul>
