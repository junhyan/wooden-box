<!doctype html>
<html>
<head>
	<meta charset="utf-8" />
	<title>Editor</title>
	<link rel="stylesheet" href="/static/css/themes/default/default.css" />
	<link rel="stylesheet" href="/static/js/plugins/code/prettify.css" />
	<script charset="utf-8" src="/static/js/kindeditor-all-min.js"></script>
	<script charset="utf-8" src="/static/js/lang/zh-CN.js"></script>
	<script charset="utf-8" src="/static/js/plugins/code/prettify.js"></script>
	<script>
		KindEditor.ready(function(K) {
			var editor1 = K.create('textarea[name="content1"]', {
			    cssPath : '/static/js/plugins/code/prettify.css',	
                themesPath: '/static/css/themes/',
                uploadJson:'/upload/media',
			
			});


		});
	</script>
</head>
<body>
	<form name="example" method="post" action="">
		<textarea name="content1" style="width:700px;height:200px;"></textarea>
		<br />
        <input type="submit" name="submit"  id="to-html" value="html" >
	</form>
</body>
</html>

