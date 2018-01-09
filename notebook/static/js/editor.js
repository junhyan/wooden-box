KindEditor.ready(function(K) {
    var editor = K.create('textarea[name="content"]', {
                    cssPath : '/static/js/plugins/code/prettify.css',   
                    themesPath: '/static/css/themes/',
                    uploadJson:'/upload/media',
                    width : '100%',
                    height: '700px',
                    });
    $(document).ready(function()
    {
        var domain = window.location.href;
        domain = domain.replace(window.location.pathname,"");
        $('#add_note').click(function(){
            editor.sync();
            $.ajax({
                 url: domain+'/add_note',
        	     dataType: 'json',
        		 type: 'POST',
        		 contentType:'application/json;charset=UTF-8',
        		 data: JSON.stringify({
        		        topic : $('#topic').val(),
                        time : '2018-1-1',
        		        author : get_cookie('author'),         	
        		        content : $('#content').val(),
        		        note_type : $('#type').val(),
        		        username : get_cookie('username'),         	
        		       	token : get_cookie('token'),           	
        		        })
        		        })
        		        .done(function (data, status, headers, config) {
        		           	alert("yes");
        		         })
        		        .fail(function (data, status, headers, config) {
        		            	
        		        });           
   
            });
    
        $('#new-type').click(function(){
            $('#type').toggle();
            $('#new-type-text').toggle();
            $('#new-type').toggle();
            $('#save-type').toggle();
        });

        $('#save-type').click(function(){
            $.ajax({
                 url: domain+'/add_type',
        	     dataType: 'json',
        		 type: 'POST',
        		 contentType:'application/json;charset=UTF-8',
        		 data: JSON.stringify({
        		        note_type : $('#new-type-text').val(),
        		        username : get_cookie('username'),         	
        		       	token : get_cookie('token'),           	
        		        })
        	     })
        	     .done(function (data, status, headers, config) {
                        $('#new-type-text').toggle();
                        $('#type').toggle();
                        $('#save-type').toggle();
                        $('#new-type').toggle();
                        $('#type').val(data.note_type);
                        $('#type').append("<option value='"+data.note_type+"'>"+data.note_type+"</option>");
                        $("#type").find("option[value='"+data.note_type+"']").attr("selected",true);
        	     })
        	     .fail(function (data, status, headers, config) {
        		            	
        	     });           
   
        });

        $.ajax({
             url: domain+'/get_types/'+get_cookie('username'),
       	     dataType: 'json',
        	 type: 'GET',
       		 contentType:'application/json;charset=UTF-8',
       		  })
       		  .done(function (datas, status, headers, config) {
                   $.each(datas, function(i, data){
                        $('#type').append("<option value='"+data.note_type+"'>"+data.note_type+"</option>");
		           });
              })
        	  .fail(function (data, status, headers, config) {
                  $('#type').append("<option value=''>无类型</option>");
        		            	
        	  });           
   
    });//document
});
