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

    });
