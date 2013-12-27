
$( document ).ready(function() {
	
	$("#spawn-detected").hide();
		
	$( "#refresh" ).click(function() {
		location.reload();
	});
	
	update_spawns();
	
	setInterval(function(){update_spawns()},3000);
});