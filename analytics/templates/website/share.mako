## coding: utf-8
<div id="share-this">
  <form class="form-inline">
    <div class="form-group">
      <div class="input-group">
        <div class="input-group-addon"><span class="glyphicon glyphicon-share"></span></div>
        <input type="text" class="form-control" id="share-this-url" value="${share_this_url}">
        <div class="input-group-addon btn btn-default" id="share-this-url-btn" data-toggle="tooltip" data-placement="bottom" title="copy link" data-clipboard-target="#share-this-url">
          <span class="glyphicon glyphicon-link"></span>
        </div>
        <div class="input-group-addon btn btn-default" data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar por email')}"><span class='st_email' st_url="${share_this_url}"></span></div>
        <div class="input-group-addon btn btn-default" data-toggle="tooltip" data-placement="bottom" 
        title="${_(u'compartilhar no Facebook')}"><span class='st_facebook' st_url="${share_this_url}"></span></div>
        <div class="input-group-addon btn btn-default" data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar no Twitter')}"><span class='st_twitter' st_url="${share_this_url}"></span></div>
        <div class="input-group-addon btn btn-default" data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar no LinkedIn')}"><span class='st_linkedin' st_url="${share_this_url}"></span></div>
        <div class="input-group-addon"></div>
      </div>
    </div>
  </form>
  <div>
    
  </div>
</div>
<script>
  new Clipboard('#share-this-url-btn');

  $("#share-this").hover(function() {
    $("#share-this").css("transition", 'transform .5s ease-in-out');
    $("#share-this").css("transform", 'translate3d(-450px, 0px, 0px)');
  }, function () {
    $("#share-this").css("transition", 'transform .5s ease-in-out');
    $("#share-this").css("transform", 'translate3d(0px, 0px, 0px)');
  }
  )
</script>