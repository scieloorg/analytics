## coding: utf-8
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
 <html>
  <header>
    <title>${_(u'SciELO Estatísticas')} (Beta)</title>
    <link rel="stylesheet" href="/static/bootstrap-3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/bootstrap-3.2.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="/static/bootstrap-3.2.0/css/bootstrap-tokenfield.min.css">
    <link rel="stylesheet" href="/static/bootstrap-3.2.0/css/tokenfield-typeahead.min.css">
    <link rel="stylesheet" href="/static/jquery-ui-1.11.4/jquery-ui.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="stylesheet" href="/static/daterangepicker/daterangepicker.css" />
    <script src="/static/jquery-1.11.1/jquery-1.11.1.min.js"></script>
    <script src="/static/jquery-ui-1.11.4/jquery-ui.min.js"></script>
    <script type="text/javascript">var switchTo5x=true;</script>
    <script type="text/javascript" src="http://w.sharethis.com/button/buttons.js"></script>
    <script type="text/javascript">stLight.options({publisher: "1eab5827-c9f3-406e-a65d-b1fdf08ae141", doNotHash: true, doNotCopy: true, hashAddressBar: false, onhover: false});</script>
    <script src="/static/clipboard/clipboard.min.js"></script>
  </header>
  <body>
    <%include file="google_analytics.mako"/>
    <div class="row">
      <nav class="navbar navbar-inverse navbar-fixed-top logo_analytics" role="navigation">
        <div class="container-fluid">
          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-right" style="padding-right: 30px;">
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">${_(u'Coleções')} <span class="caret"></span></a>
                <ul class="dropdown-menu" role="menu">
                  % for acron, info in sorted(collections.items(), key=lambda x: x[1]['name']):
                    <li role="presentation"><a role="menuitem" tabindex="-1" href="?collection=${acron}">${info['name']}</a></li>
                  % endfor
                </ul>
              </li>
              <li>
                <button type="submit" class="btn navbar-btn" data-toggle="modal" data-target="#journal_selector_modal">${_(u'selecionar periódico')}</button>
              </li>
            </ul>
          </div> <!-- collapse -->
        </div> <!-- container-fluid -->
      </nav>
    </div>
    <div class="row">
      <div class="header-col level1">
        <div class="container-fluid">
            <span id="collection_name">${selected_collection['name']}</span>
        </div>
      </div>
    </div>
    <div class="row">
      % if selected_journal:
      <div class="header-col level2">
        <div class="container-fluid">
            ${selected_journal} (${selected_journal_code})
            <a href="${request.route_url('index_web')}?journal=clean" class="remove_session">
              <span class="glyphicon glyphicon-remove-circle navbar-right"/>
            </a>
        </div>
      </div>
      % endif
    </div>
    <div class="row">
      % if selected_document:
      <div class="header-col level3">
        <div class="container-fluid">
            ${selected_document.original_title()}
            <a href="${request.route_url('index_web')}?document=clean" class="remove_session">
              <span class="glyphicon glyphicon-remove-circle navbar-right"/>
            </a>
        </div>
      </div>
      % endif
    </div>
    <div class="row">
      <nav class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
          <%include file="navbar.mako" />
        </div> <!-- div container-fluid -->
      </nav>
    </div> <!-- div row -->
    <div class="row container-fluid" style="padding-left: 40px; padding-right: 40px;">
      <%block name="central_container_without_filters" />
      <%block name="central_container_for_article_filters" />
      <%block name="central_container_for_journal_filters" />
      <%block name="central_container_for_bibliometric_filters" />
    </div><!-- div row -->
    <div class="row" style="padding-left: 40px; padding-right: 40px; margin-top: 100px;">
      <div class="panel panel-info">
          <div class="panel-heading">${_(u'Ferramenta em desenvolvimento disponível em versão Beta Test.')}</div>
          <div class="panel-body">
              ${_(u'Esta ferramenta esta em desenvolvimento e foi publicada com o objetivo de realizar testes de uso e performance. Todos os indicadores carregados são reais e estão sendo atualizados e inseridos gradativamente. Problemas de lentidão e indisponibilidade do serviços são esperados nesta fase.')}
          </div>
      </div>
    </div>
    <div class="row container-fluid footer">
      <div class="col-md-4">
        <p>
          <strong>
            SciELO - Scientific Electronic Library Online <br>
            <a href="http://www.fapesp.br" target="_blank">FAPESP</a>
            <a href="http://www.cnpq.br" target="_blank">CNPq</a>
            <a href="http://www.bireme.org">BIREME</a>
            <a href="http://www.fapunifesp.edu.br" target="_blank">FapUnifesp</a>
          </strong>
        </p>
        <p>
          Avenida Onze de Junho, 269 - Vila Clementino 04041-050 São Paulo</p>
          <p>Tel.: +55 11 5083-3639/59 - Email: <a href="mailto:scielo@scielo.org">scielo@scielo.org</a>
        </p>
      </div>
      <div class="col-md-3">
        <h4>${_(u'Ajuda')}</h4>
        <ul>
          <li><a href="http://github.com/scieloorg/analytics/issues/new">${_(u'Reportar error')}</a></li>
          <li><a href="http://groups.google.com/group/scielo-discuss" target="_blank">${_(u'Lista de discussão')}</a></li>
        </ul>
      </div>
      <div class="col-md-3">
        <h4>${_(u'Desenvolvimento')}</h4>
        <ul>
          <li><a href="http://www.github.com/scieloorg/" target="_blank">GitHub</a></li>
          <li><a href="http://groups.google.com/group/scielo-dev" target="_blank">${_(u'Lista de desenvolvimento')}</a></li>
        </ul>
      </div>
      <div class="col-md-2">
        <form id="form_languages" method="POST">
          <select id="lang_options" name="_LOCALE_">
            <option value="pt" ${'selected=""' if locale == 'pt' else ''}>Português</option>
            <option value="en" ${'selected=""' if locale == 'en' else ''}>English</option>
            <option value="es" ${'selected=""' if locale == 'es' else ''}>Español</option>
            <option value="es_MX" ${'selected=""' if locale == 'es_MX' else ''}>Español (México)</option>
          </select>
        </form>
      </div>
    </div>
    <div class="row container-fluid">
      <center>
        <%include file="use_license.mako"/>  
      </center>
    </div>
    <%include file="journal_selector_modal.mako"/>
    <%include file="share.mako"/>
    <script src="/static/bootstrap-3.2.0/js/bootstrap.min.js"></script>
    <script src="/static/moment/moment.min.js"></script>
    <script src="/static/highcharts/highstock.js"></script>
    <script src="/static/highcharts/modules/no-data-to-display.js"></script>
    <script src="/static/highcharts/modules/heatmap.js"></script>
    <script src="/static/highcharts/modules/exporting.js"></script>
    <script src="/static/highcharts/modules/export-data.js"></script>
    <script src="/static/highcharts/maps/modules/map.js"></script>
    <script src="/static/highcharts/mapdata/custom/world.js"></script>
    <script src="/static/daterangepicker/daterangepicker.js"></script>
    <script src="/static/jquery-1.11.1/plugins/jquery.number.min.js"></script>
    <script src="/static/bootstrap-3.2.0/js/bootstrap-tokenfield.min.js"></script>
    <script>$('.collapse').collapse()</script>
    <script type="text/javascript">
      Highcharts.setOptions({
        colors: ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099', '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395', '#22AA99', '#AAAA11', '#6633CC', '#E67300', '#8B0707', '#651067'],
        lang: {
          decimalPoint: '.', 
          thousandsSep: ',',
          months: ['${_(u'Janeiro')}', '${_(u'Fevereiro')}', '${_(u'Março')}', '${_(u'Abril')}', '${_(u'Maio')}', '${_(u'Junho')}', '${_(u'Julho')}', '${_(u'Agosto')}', '${_(u'Setembro')}', '${_(u'Outubro')}', '${_(u'Novembro')}', '${_(u'Dezembro')}'],
          shortMonths: ['${_(u'Jan')}','${_(u'Fev')}','${_(u'Mar')}','${_(u'Abr')}','${_(u'Mai')}','${_(u'Jun')}','${_(u'Jul')}','${_(u'Ago')}','${_(u'Set')}','${_(u'Out')}','${_(u'Nov')}','${_(u'Dez')}']
        }
      });
    </script>
    <script>
      $('#lang_options').change(
        function(){
          $('#form_languages').submit();
        });
    </script>
    <!-- Início de JS de filtros de ano de publicação-->
    <script>
    var re_py_range_replace = new RegExp(' ', 'g');
    $(function() {
      $( "#slider-range" ).slider({
        range: true,
        min: ${publication_years[0]},
        max: ${publication_years[-1]},
        values: [${py_range[0]},${py_range[1]}],
        slide: function( event, ui ) {
          $( "#year-range" ).val( ui.values[0] + " - " + ui.values[1] );
        }
      });
      $( "#year-range" ).val( $( "#slider-range" ).slider( "values", 0 ) +
        " - " + $( "#slider-range" ).slider( "values", 1 ) );
    });
    $("#apply-py-range").click(function(){
      window.open("?py_range=" + $("#year-range").val().replace(re_py_range_replace, ''), name="_self");
    })
    </script>
    <!-- Fim de JS de filtros de ano de publicação-->
    <!-- Início de JS de filtros de scopo de área temática-->
    <script>
    $("#apply-sa-scope").click(function() {
      $("#sa-scope-form").submit();
    })      
    </script>
    <!-- Fim de JS de filtros de scopo de área temática-->
    <!-- Início de JS de filtros de scopo de idioma-->
    <script>
    $("#apply-la-scope").click(function() {
      $("#la-scope-form").submit();
    })      
    </script>
    <!-- Fim de JS de filtros de scopo de idioma-->
    <script>
      $('[data-toggle="popover"]').popover();
      $('[data-toggle="tooltip"]').tooltip();
    </script>
    <%block name="extra_js" />
  </body>
</html>