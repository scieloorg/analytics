## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
<h1>${_(u'Tabulações')}</h1>
<p>
${_(u'O SciELO fornece algumas tabulações pré-formatadas com alguns dos metadados utilizados para produção dos indicadores presentes nesta ferramenta. Qualquer interessado pode fazer o download e produzir análises bibliométricas de acordo com suas necessidade.')}
</p>
<p>
${_(u'Para mais informações sobre as catacterísticas de cada tabulação, acessar')} <a href="http://docs.scielo.org/projects/scielo-processing/pt/latest/public_reports.html" target="_blank"><span class="glyphicon glyphicon-globe"></span></a>.
</p>
% for tab in  sorted(tabs, key=lambda x: x['collection']['name']):
  <h3>${tab['collection']['name']}</h3>
  %if tab['is_available']:
    <ul>
      <li><b>${_(u'Nome do arquivo')}:</b> <a href="${tab['tabsurl']}">${tab['tabsfilename']}</a></li>
      <li><b>${_(u'Periodicidade de atualização')}:</b> ${_(u'mensal')}</li>
      <li><b>${_(u'Tamanho do arquivo')}:</b> ${tab['contentlength']}Mb</li>
      <li><b>${_(u'Conjunto de caracteres')}:</b> utf-8</li>
      <li><b>${_(u'Última atualização')}:</b> ${tab['lastmodified']}</li>
    </ul>
  %else:
    <h5>${_(u'Arquivo não disponível para esta coleção')}</h5>
  %endif
% endfor

</%block>