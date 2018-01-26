$(document).ready(function()
{
    var domain = window.location.href;
    domain = domain.replace(window.location.pathname,"");
    $('#add_user').click(function(){
        		
        $.ajax({
        		   url: domain+'/add_user',
        		   dataType: 'json',
        		   type: 'POST',
        		   contentType:'application/json;charset=UTF-8',
        		   data: JSON.stringify({
        		          	name : $('#name').val(),
        		          	username : $('#username').val(),
        		           	email : $('#email').val(),
        		           	mobile: $('#mobile').val(),           	
        		           	passwd: $('#passwd').val(),           	
        		           	token:  get_cookie('token'),           	
        		            })
        		           	})
        		            .done(function (data, status, headers, config) {
                                alert(data.name);
        		            })
        		            .fail(function (data, status, headers, config) {
        		            	
        		            });           
   
    });



});//document



function changePassword(){
	var confirePassword = $("#password2").val();
    var value = $("#password").val();
    if(confirePassword != value) {  
    	$('.errors-container').html("密码输入不一致"); 
    }   
	else if($("#password").val()==''){
		$('.errors-container').html("密码不能为空"); 
	}else if($("#oldPassword").val()==''){
		$('.errors-container').html("请输入旧密码"); 
	}else if($("#oldPassword").val()!=getCookieValue("userPass")){
		$('.errors-container').html("旧密码输入不正确"); 
	}else{
	    $.ajax({
	            url: 'http://172.31.34.180/littleVCloud/userController/modifyUser.do',
	            dataType: 'json',
	            type: 'PUT',
	            contentType:'application/json;charset=UTF-8',
	            data: JSON.stringify({
	            	userId : getCookieValue("userId"),
	            	password : $('#password').val()	            	           	
	            })
	           	})
	            .success(function (data, status, headers, config) {	            	
					addCookie("userPass",data.password,7,"/");
	            	window.location.href = 'login.jsp';
	            })
	            .error(function (data, status, headers, config) {
	            	$('.errors-container').html("密码修改失败"); 
	            });
	    
	}
}
