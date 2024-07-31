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
      <li><a href="${request.route_url('accesses_list_journals_web')}">${_(u'Periódico')}</a></li>
      <li><a href="${request.route_url('accesses_list_journals_language')}">${_(u'Periódico por idioma')}</a></li>
      <li><a href="${request.route_url('accesses_list_journals_top100_articles')}">${_(u'Top 100 artigos')}</a></li>
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
      <li><a href="${request.route_url('bibliometrics_list_general_indicators_web')}">${_(u'Indicadores Gerais')}</a></li>
    </ul>
  </li>
  <%include file="navbar_common_links.mako"/>
</ul>
