## coding: utf-8
<li class="${'active' if page == 'reports' else ''}">
    <a href="${request.route_url('reports')}">${_(u'Relatórios')}</a>
</li>
<li class="${'active' if page == 'faq' else ''}">
    <a href="${request.route_url('faq_web')}">FAQ</a>
</li>