## coding: utf-8
<div id="share-this">
  <label>share</label>
  <ul>  
    <li id="share-this-url-btn" data-toggle="tooltip" data-placement="bottom" title="copy link" data-clipboard-text="${share_this_url}">
      <a href="#"><span class="glyphicon glyphicon-link"></span></a>
    </li>
    <li data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar por email')}"><span class='st_email' st_url="${share_this_url}"></span></li>
    <li data-toggle="tooltip" data-placement="bottom" 
    title="${_(u'compartilhar no Facebook')}">
      <span class='st_facebook' st_url="${share_this_url}"></span>
    </li>
    <li data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar no Twitter')}">
      <span class='st_twitter' st_url="${share_this_url}"></span>
    </li>
    <li data-toggle="tooltip" data-placement="bottom" title="${_(u'compartilhar no LinkedIn')}">
      <span class='st_linkedin' st_url="${share_this_url}"></span>
    </li>
  </ul>
</div>
<script>
  new Clipboard('#share-this-url-btn');
</script>