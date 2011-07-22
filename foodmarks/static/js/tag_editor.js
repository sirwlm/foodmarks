var tags = {};

function addTag(key, value){
    key = escapeHTML(key);
    value = escapeHTML(value);
    var normalizedKey = key.toLowerCase();
    
}

$(document).ready(function(){
	$('#new-key').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    $('#current-tags').append('<li><span class="tag-key">' + escapeHTML($('#new-key').val()) + '</span><span class="tag-value">' + escapeHTML($('#new-value').val()) + '</span></li>');
		    $('#new-key').val('');
		    $('#new-value').val('');
		    break;
		}
	    });	 


	$('#new-value').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    $('#current-tags').append('<li><span class="tag-key">' + escapeHTML($('#new-key').val()) + '</span><span class="tag-value">' + escapeHTML($('#new-value').val()) + '</span></li>');
		    $('#new-key').val('');
		    $('#new-value').val('');
		    break;
		}
	    });	      
    });