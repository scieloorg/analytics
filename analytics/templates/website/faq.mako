## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>

<%block name="central_container">
    <h3>${_(u'Perguntas Frequentes (Acessos)')}</h3>
    <blockquote>
        <h4>${_(u'Por que algumas coleções não possuem estatísticas de acesso?')}</h4>
        <p>${_(u'Para que os dados de acessos sejam computados é necessário que os logs de acessos sejam enviados para processamento. A ausência de estatísticas de acessos deve ser verificada com a coordenação de cada coleção SciELO.')}</p>
    </blockquote>
    <blockquote>
        <h4>${_(u'Por que algumas coleções possuem acessos computados para um período maior?')}</h4>
        <p>${_(u'O período disponível de cada uma das coleções depende dos logs de acessos registrados e disponibilizados. Este projeto se compromete a computar os dados de acessos a partir de 2012, desde que os logs sejam devidamente fornecidos pelas coleções.')}</p>
    </blockquote>
    <blockquote>
        <h4>${_(u'O que está sendo contabilizado?')}</h4>
        <p>${_(u'Estão sendo contabilizados os acessos ao texto completo, em quaisquer formatos, por meio das métricas Requisições Totais e Requisições Únicas, segundo o modelo COUNTER R5.')}</p>
    </blockquote>
    <blockquote>
        <h4>${_(u'Qual a periodicidade de atualização dos indicadores?')}</h4>
        <p>${_(u'Os indicadores de acesso são atualizados a cada cinco dias.')}</p>
    </blockquote>
    <h3>${_(u'Perguntas Frequentes (Publicação)')}</h3>
    <blockquote>
        <h4>${_(u'Porque algumas coleções possuem dados desatualizados?')}</h4>
        <p>${_(u'A atualização de dados depende de processos que envolvem cada uma das coleções certificadas do SciELO. A atualização destes indicadores está diretamente ligada à condução adequada desses processos por cada uma das coleções.')}</p>
    </blockquote>
    <blockquote>
        <h4>${_(u'O que esta sendo contabilizado?')}</h4>
        <p>${_(u'Estão sendo contabilizados indicadores de publicação das coleções com base nos metadados fornecidos durante todo o processo de publicação de um documento no SciELO. A qualidade desses indicadores está diretamente ligada à qualidade dos processos implementados por cada uma das coleções.')}</p>
    </blockquote>
    <blockquote>
        <h4>${_(u'Qual a periodicidade de atualização dos indicadores?')}</h4>
        <p>${_(u'Semanal')}</p>
    </blockquote>
</%block>