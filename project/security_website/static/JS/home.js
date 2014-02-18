$(document).ready(function(){
  

  $("#register").click(function(){ 
	var url ="http://"+location.host+"/register/";
    location.assign(url);
  });
  $("#logout").click(function(){
	 var url ="http://"+location.host+"/logout/";
	 location.assign(url);
	 });


});
