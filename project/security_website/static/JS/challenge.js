$(document).ready(function(){
  

  $("#register").click(function(){ 
	var url ="http://"+location.host+"/register/";
    location.assign(url);
  });
  $("#logout").click(function(){
	 var url ="http://"+location.host+"/logout/";
	 location.assign(url);
	 });
  $("#web").click(function(){
	  var url ="http://"+location.host+"/clg/web/";
	  location.assign(url);
  });
  $("#startnew").click(function(){
	  var url ="http://"+location.host+"/clg/web_start/";
	  location.assign(url);
	  });
  $("#getback").click(function(){
	  var url ="http://"+location.host+"/clg/web_restart/";
	  location.assign(url);
	  });
});

