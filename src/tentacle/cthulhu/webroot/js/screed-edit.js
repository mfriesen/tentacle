var step_count = -1;

$( document ).ready(function() {
	
	// count number of current steps
	step_count = $(".screed-step-count").length - 1;
	
	$( "#screed-step-add" ).click(function() {
		step_count++;
		$(".screed-step:last").after('\
		<div id="screed-step-' + step_count + '" class="screed-step">\
			<div class="input-group">\
				<span class="input-group-addon screed-step-count">' + step_count + '</span>\
				<div class="form-control screed-step-text" style="white-space:pre" contenteditable></div>\
				<span class="input-group-addon"><button type="button" alt="screed-step-' + step_count + '" class="btn btn-danger btn-sm screed-step-delete">Delete</button></span>\
			</div>\
			<div class="input-group">&nbsp;</div>\
		</div>');
	});
	
	// handle delete button
	$(document).on({
   		click: function() { 
   			var id = $(this).attr("alt");
   			$("#" + id).remove();
   			
   			// reset step counter
   			$(".screed-step-count").each(function(index) {
				$(this).text(index);
				step_count = index;
			}); 
   		}
	},'.screed-step-delete');
	
	$("#screed-save").click(function(e) {
		e.preventDefault();
		
		data = $('#steps-form').serialize();

		$(".screed-step-text").each(function(k, v) {
			data += "&steps=" + $(v).html();
		});
		
		$.post("/screed/edit", data, function(data) {
			var loc = window.location;
			window.location = loc.protocol + "//" + loc.hostname + (loc.port && ":"+loc.port) + "/screed/edit?id=" + data; 
		});
	});
});

