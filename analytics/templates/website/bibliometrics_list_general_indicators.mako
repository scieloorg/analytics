## coding: utf-8
<%inherit file="central_container_without_filters.mako"/>
<%block name="central_container">

  <h3>${_(u'Indicadores Bibliométricos da Rede SciELO')}</h3>
  <h5><b>${_(u'Periodicidade de atualização:')}</b>${_(u' anual')}</h5>
    <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
      <!-- collapseOne -->
      <div class="panel panel-default">
        <div class="panel-heading" role="tab" id="headingOne">
          <h4 class="panel-title">
            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
            ${_(u'Indicadores de Publicação')}
            </a>
          </h4>
        </div>
        <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
          <div class="panel-body">
            <b>${_(u'Numeros da Rede SciELO por:')}</b>
            <ul>
              <li>${_(u'Ano de publicação: ')}<a href="https://static.scielo.org/indicators/${locale}/A01a_${locale}.xls">A01a_${locale}.xls</a></li>
              <li>${_(u'Periódico: ')}<a href="https://static.scielo.org/indicators/${locale}/A01b_${locale}.xls">A01b_${locale}.xls</a></li>
              <li>${_(u'Assunto: ')}<a href="https://static.scielo.org/indicators/${locale}/A01c_${locale}.xls">A01c_${locale}.xls</a></li>
              <li>${_(u'País de afiliação do autor: ')}<a href="https://static.scielo.org/indicators/${locale}/A01d_${locale}.xls">A01d_${locale}.xls</a></li>
            </ul>
            <b>${_(u'País de Afiliação do Autor por: ')}</b>
            <ul>
              <li>${_(u'Ano de publicação: ')}<a href="https://static.scielo.org/indicators/${locale}/A02a_${locale}.xls">A02a_${locale}.xls</a></li>
              <li>${_(u'Periódico: ')}<a href="https://static.scielo.org/indicators/${locale}/A02b_${locale}.xls">A02b_${locale}.xls</a></li>
              <li>${_(u'País de publicação da revista: ')}<a href="https://static.scielo.org/indicators/${locale}/A02c_${locale}.xls">A02c_${locale}.xls</a></li>
              <li>${_(u'Assunto: ')}<a href="https://static.scielo.org/indicators/${locale}/A02d_${locale}.xls">A02d_${locale}.xls</a></li>
            </ul>
            <b>${_(u'Número de Co-autores por: ')}</b>
            <ul>
              <li>${_(u'Periódico: ')}<a href="https://static.scielo.org/indicators/${locale}/A03a_${locale}.xls">A03a_${locale}.xls</a></li>
              <li>${_(u'Assunto: ')}<a href="https://static.scielo.org/indicators/${locale}/A03b_${locale}.xls">A03b_${locale}.xls</a></li>
            </ul>
          </div>
        </div>
      </div>
      <!-- collapseTwo -->
      <div class="panel panel-default">
        <div class="panel-heading" role="tab" id="headingTwo">
          <h4 class="panel-title">
            <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
              ${_(u'Indicadores de Coleção')}
            </a>
          </h4>
        </div>
        <div id="collapseTwo" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingTwo">
          <div class="panel-body">
            <b>${_(u'Periódico por:')}</b>
            <ul>
              <li>${_(u'Ano de publicação: ')}<a href="https://static.scielo.org/indicators/${locale}/B01a_${locale}.xls">B01a_${locale}.xls</a></li>
              <li>${_(u'Assunto: ')}<a href="https://static.scielo.org/indicators/${locale}/B01b_${locale}.xls">B01b_${locale}.xls</a></li>
              <li>${_(u'Indicadores gerais: ')}<a href="https://static.scielo.org/indicators/${locale}/B01c_${locale}.xls">B01c_${locale}.xls</a></li>
            </ul>
          </div>
        </div>
      </div>
      <!-- collapseThree -->
      <div class="panel panel-default">
        <div class="panel-heading" role="tab" id="headingThree">
          <h4 class="panel-title">
            <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
              ${_(u'Indicadores de Citação')}
            </a>
          </h4>
        </div>
        <div id="collapseThree" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingThree">
          <div class="panel-body">
            <b>${_(u'Ano de Citação por:')}</b>
            <ul>
              <li>${_(u'Idade do documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C01a_${locale}.xls">C01a_${locale}.xls</a></li>
              <li>${_(u'Tipo de documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C01b_${locale}.xls">C01b_${locale}.xls</a></li>
            </ul>
            <b>${_(u'Periódico Citante por:')}</b>
            <ul>
              <li>${_(u'Idade do documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C02a_${locale}.xls">C02a_${locale}.xls</a></li>
              <li>${_(u'Tipo de documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C02b_${locale}.xls">C02b_${locale}.xls</a></li>
            </ul>
            <b>${_(u'Assunto do Periódico Citante por:')}</b>
            <ul>
              <li>${_(u'Idade do documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C03a_${locale}.xls">C03a_${locale}.xls</a></li>
              <li>${_(u'Tipo de documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C03b_${locale}.xls">C03b_${locale}.xls</a></li>
              <li>${_(u'Periódico SciELO citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C03c_${locale}.xls">C03c_${locale}.xls</a></li>
            </ul>
            <b>${_(u'País de Afiliação do Autor Citante por:')}</b>
            <ul>
              <li>${_(u'Idade do documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C04a_${locale}.xls">C04a_${locale}.xls</a></li>
              <li>${_(u'Tipo de documento citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C04b_${locale}.xls">C04b_${locale}.xls</a></li>
              <li>${_(u'Periódico SciELO citado: ')}<a href="https://static.scielo.org/indicators/${locale}/C04c_${locale}.xls">C04c_${locale}.xls</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</%block>
