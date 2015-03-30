$(document).ready(function () {
	$("div#wrapper").click(function() {
		var container = $('div#container');
		container.html("clicked!");

		$.ajax({
			url: "data.json",
			type: "GET"
		})
		.done(function(objList){
			$.each(objList, function(i, obj)
			{
				container.append(
					$("<" +obj.tag + ">")
					.addClass(obj.class)
					.html(obj.content);
				);
			});
		});
	});
});