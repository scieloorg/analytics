## coding: utf-8
<%inherit file="base.mako"/>

<%block name="central_container_for_article_filters">
  <div class="col-md-3">
    <div class="panel panel-default" id="filters-menu">
        <div class="panel-heading">
          <div class="panel-title"><b>${_(u'Filtros para documentos')}</b></div>
        </div>
        <div class="panel-body">
          <div class="row" id="filters-submenu">
            <div class="col-md-8">
              <h5>${_(u'Ano de publicação')}</h5>
            </div>
            <div class="col-md-4" style="text-align: right;">
              <h5><a href="#" id="apply-py-range">${_(u"aplicar")}</a></h5>
            </div>
          </div>
          <hr class="dashed-hr">
          <form id="py-range">
            <p>
              <label for="year_range">${_(u'período')}:</label>
              <input type="text" id="year-range" readonly style="border:0; color:#f6931f; font-weight:bold;">
            </p>
            <div id="slider-range"></div>
          </form>
          <hr class="continuous-hr">
          <div class="row" id="filters-submenu">
            <div class="col-md-8">
              <h5>${_(u'Área temática')}</h5>
            </div>
            <div class="col-md-4" style="text-align: right;">
              <h5><a href="#" valign="right" id="apply-sa-scope">${_(u"aplicar")}</a></h5>
            </div>
          </div>
          <hr class="dashed-hr">
          <form id="sa-scope-form" target="_self">
            % for subject_area in sorted(subject_areas):
            <div class="checkbox">
              <label>
                <input type="checkbox" name="sa_scope" value="${subject_area}" ${'checked' if subject_area in sa_scope else ''}> ${subject_area}
              </label>
            </div>
            % endfor
          </form>
          <hr class="continuous-hr">
          <div class="row" id="filters-submenu">
            <div class="col-md-8">
              <h5>${_(u'Idioma')}</h5>
            </div>
            <div class="col-md-4" style="text-align: right;">
              <h5><a href="#" valign="right" id="apply-la-scope">${_(u"aplicar")}</a></h5>
            </div>
          </div>              
          <hr class="dashed-hr">
          <form id="la-scope-form" target="_self">
            % for iso, language in sorted(languages, key=lambda x: x[1]):
            <div class="checkbox" id="la-scope">
              <label>
                <input type="checkbox" name="la_scope" value="${iso}" ${'checked' if iso in la_scope else ''}> ${language}
              </label>
            </div>
            % endfor
          </form>
          <hr class="continuous-hr">
        </div>
    </div>
  </div>
  <div class="col-md-9">
    <%block name="central_container" />
  </div>
</%block>