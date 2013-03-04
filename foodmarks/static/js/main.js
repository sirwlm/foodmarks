function escapeHTML(text){
    return $('<div/>').text(text).html();
}

function changeBoxStatus(actions, newStatus){
    var recipeId = actions.find('.recipe-id').val();
    var ribbonId = actions.find('.ribbon-id').val();
    $.post('/action/',
	   {recipeId: recipeId, ribbonId: ribbonId,
		   action: 'changeBoxStatus',
		   newStatus: newStatus,
		   'csrfmiddlewaretoken': csrfToken},
	   function(data){
	       if(data['status'] == 'OK'){
		   actions.find('.add-to-box').toggleClass('hide', newStatus);
		   actions.find('.remove-from-box').toggleClass('hide', !newStatus);
		   actions.find('.ribbon-id').val(data['ribbonId']);
	       }else{
		   alert('There was an error processing this action.');
	       }
	   });
}

$(document).ready(function(){
	$('.add-to-box').on('click', function(e){
		changeBoxStatus($(this).closest('.actions'), true);
		return false;
	    });

	$('.remove-from-box').on('click', function(e){
		changeBoxStatus($(this).closest('.actions'), false);
		return false;
	    });

	$(".delete-ribbon").click(function(){
		var agree = confirm('Are you sure you want to delete this bookmark? If no one else has bookmarked it, the recipe will also be deleted.');
		if(agree){
		    var actions = $(this).closest('.actions');
		    var recipeId = actions.find('.recipe-id').val();
		    var ribbonId = actions.find('.ribbon-id').val();
		    $.ajax({
			    type: 'POST',
				url: '/action/',
				data: {recipeId: recipeId, ribbonId: ribbonId,
				    action: 'deleteRibbon',
				    'csrfmiddlewaretoken': csrfToken},
				async: false,
				success:
			    function(data){
			    }});
		    window.location.reload();

		}
		return false;

	    });

    });

