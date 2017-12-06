## coding: utf-8
<li>
    <a href="http://visual.scielo.org/v1" target="_blank">${_(u'Visualização')}</a>
</li>
<li class="${'active' if page == 'reports' else ''}">
    <a href="${request.route_url('reports')}">${_(u'Relatórios')}</a>
</li>
<li class="${'active' if page == 'faq' else ''}">
    <a href="${request.route_url('faq_web')}">FAQ</a>
</li>