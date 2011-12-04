$(document).on("pagebeforechange", function(e, data) {
	var page = data.toPage.split("#")[1],
		tmpl = doT.template(page, undefined, undefined),
		$.get("someurl",function(res) {
			$("#"+page).html(tmpl(res));
		});

});