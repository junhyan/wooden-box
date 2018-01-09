$(document).ready(function()
{

    $(window).resize(function() {
        var width = $(this).width();
        var height = $(this).height();
        if(width<1000)
                $('#nav').hide();
        else
                $('#nav').show();
    });

    var template=function(data, i){ 
    return '<div class="content" id="content'+i+'">'+                                                                        
                                '<div id="topic"><h1>'+data.topic+'</h1><p><font>'+data.author+'</font><font>'+data.time+'</font></p></div>'+                                                                   
                                '<font size="5">'+
                                    '<div id="note">'+ data.content+
                                    '</div>'+
                                '</font>'+
                         '</div>';
    }
    $.ajax({
         url: '/get_notes/'+get_cookie('username'),
         dataType: 'json',
      	 type: 'GET',
    	 contentType:'application/json;charset=UTF-8',
         })
       	 .done(function (datas, status, headers, config) {
              var lists='';
              $.each(datas, function(i, data){
		            var content=template(data,i);
                    lists += content;
                  
                    $(document).on("click","#content"+i,function(){
                            var div = document.getElementById("content"+i);
                            if(div.style.height=='auto')
                                div.style.cssText = "height:300px";
                            else
                                div.style.cssText = "height:auto";
                    });
                   
                    $(document).on("mouseover","#content"+i,function(){
                            var div = document.getElementById("content"+i);
                            div.style.cssText = "background:#FAF9F7";
                    });
                    $(document).on("mouseleave","#content"+i,function(){
                            var div = document.getElementById("content"+i);
                            div.style.backgroundColor= "white";
                    });
                    
              });
              $('#lists').html(lists);
         })
         .fail(function (data, status, headers, config) {
        		            	
          });           
   
    $('#login').click(function(){
        $('#login-div').toggle();
    });
    $('#login-internal').click(function(){
        $.ajax({
        		   url: '/login',
        		   dataType: 'json',
        		   type: 'POST',
        		   contentType:'application/json;charset=UTF-8',
        		   data: JSON.stringify({
        		            	username : $('#username').val(),
        		            	passwd: $('#password').val()           	
        		            })
        		           	})
        		            .done(function (data, status, headers, config) {
        		                add_cookie('author',data.name);	
        		                add_cookie('username',data.username);	
        		                add_cookie('token',data.token);	
                                $('#new-note').show();
                                $('#login-div').hide();
        		            })
        		            .fail(function (data, status, headers, config) {
        		            	
        		            });           
   
    });
});//document
