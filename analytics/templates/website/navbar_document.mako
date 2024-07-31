## coding: utf-8
<ul class="nav navbar-nav">
  <li class="${'active' if page == 'home' else ''}">
    <a href="${request.route_url('index_web')}"><span class="glyphicon glyphicon-home"></span> ${content_scope}</a>
  </li>
  <li class="${'active' if page == 'accesses' else ''}">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">${_(u'Acessos')} <span class="caret"></span></a>
    <ul class="dropdown-menu">
      <li><a href="${request.route_url('accesses_document_web')}">${_(u'Gráficos')}</a></li>
    </ul>
  </li>
  <li class="${'active' if page == 'bibliometrics' else ''}">
    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">${_(u'Bibliometria')} <span class="caret"></span></a>
    <ul class="dropdown-menu">
      <li><a href="${request.route_url('bibliometrics_document_list_received_citations')}">${_(u'Citações recebidas')}</a></li>
    </ul>
  </li>
  <%include file="navbar_common_links.mako"/>
</ul>
