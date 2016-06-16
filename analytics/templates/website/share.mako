## coding: utf-8
<div id="share-this">
  <form class="form-inline">
    <div class="form-group">
      <div class="input-group">
        <div class="input-group-addon glyphicon glyphicon-share" aria-hidden="true"></div>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="exampleInputAmount" placeholder="Amount" value="${current_url}" width="500px"/>
        </div>
      </div>
    </div>
  </form>
</div>
<script>
  $("#share-this").hover(function(e) {
    $("#share-this").css("right", 0);
  })
  $("#share-this").mouseout(function(e) {
    $("#share-this").css("right", -80);
  })
</script>