var wilco = {};

$("#checklist").live("pageinit", function() {
	wilco.initChecklist("checklistItems");
});

$("#carlist").live("pageinit", function() {
	wilco.initChecklist("carlistItems");
});

$("#petlist").live("pageinit", function() {
	wilco.initChecklist("petlistItems");
});

$("#checklist ul.prepare-checks li").live("click", function() {
	wilco.setChecked($(this),"checklistItems");
});

$("#carlist ul.prepare-checks li").live("click", function() {
	wilco.setChecked($(this),"carlistItems");
});

$("#petlist ul.prepare-checks li").live("click", function() {
	wilco.setChecked($(this),"petlistItems");
});

wilco.setChecked = function($t, store) {
	var iconSpan = $t.find("span.ui-icon-shadow"),
		chk = $t.find("input")[0];
	if (wilco.saveTimer) clearTimeout(wilco.saveTimer);
	if (chk.checked) {
		$(chk).removeAttr("checked");
		iconSpan.removeClass("ui-icon-check ui-icon");
	} else {
		chk.checked = "true";
		iconSpan.addClass("ui-icon-check ui-icon");
	}
	wilco.saveTimer = setTimeout(function() {
		wilco.saveChecklist(store);
	}, 1000);
};

wilco.initChecklist = function(store) {
	var lists = $("ul.prepare-checks");
	lists.find("div.ui-checkbox").hide();
	$("span.ui-icon-shadow").removeClass("ui-icon-check ui-icon");
	if (localStorage && localStorage[store]) {
		var checkedItems = localStorage[store].split(","),
			i = 0,
			chk;
		for ( ; i < checkedItems.length; i++ ) {
			console.log(checkedItems[i]);
			chk = $("input[value=" + checkedItems[i] + "]");
			chk.attr("checked","true");
			chk.closest("li").find("span.ui-icon-shadow").addClass("ui-icon-check ui-icon");
		}
	}
};

wilco.saveChecklist = function(store) {
	var chks = $("input:checked"),
		items = [],
		i = 0;
	for ( ; i < chks.length; i++ ) {
		items.push(chks[i].value);
	}
	localStorage[store] = items;
};

$( '#ready' ).live( 'pageinit',function(event,data){
    var theList = doT.template($("#ready-list").html());
  $.get("/section/2/",function(res){
      $("#ready-list").html(theList(res));
  })
});