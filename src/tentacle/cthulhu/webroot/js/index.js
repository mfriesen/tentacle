
$( document ).ready(function() {
	
	$.expr[':'].containsIgnoreCase = function (n, i, m) {
        return jQuery(n).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    
	$("#spawn-detected").hide();
		
	$( "#refresh" ).click(function() {
		location.reload();
	});
	
	update_spawns();
	
	setInterval(function(){update_spawns()},3000);

    $("#filter-text").keyup(function(){
		//hide all the rows
		$("#filter-tbody").find("tr").hide();

		// split the current value of searchInput
		var data = this.value.split(" ");
		// create a jquery object of the rows
		var jo = $("#filter-tbody").find("tr");
          
		// Recusively filter the jquery object to get results.
		$.each(data, function(i, v){
			jo = jo.filter("*:containsIgnoreCase('"+v+"')");
		});
		//show the rows that match.
		jo.show();
		//Removes the placeholder text  
      }).focus(function(){
          this.value="";
          $(this).css({"color":"black"});
          $(this).unbind('focus');
      }).css({"color":"#C0C0C0"});	
});