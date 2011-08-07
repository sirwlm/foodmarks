/*
  {'mainingredient': { 'original' : 'Main Ingredient', 
	      'row': ,
	      'keyCol': ,
	      'valueCol': ,
	      'values': { 'redpepper': {
		  'elem': DOMELEM,
		      'original': 'Red Pepper'
		      }
		  ]
	      }
  }
 */

var tags = {};

function generateTagJsonString(){
    return JSON.stringify(tags);
}

function normalize(val){
    return val.toLowerCase().replace(/\s/g, '');
}

function createValueTagDict(value, normalizedValue){
    var valueElem = document.createElement('span');
    valueElem.className = 'tag-value';
    valueElem.setAttribute('title', normalizedValue);

    var remove = document.createElement('span');
    remove.className = 'tag-remove';
    remove.appendChild(document.createTextNode('X'));
    
    valueElem.appendChild(document.createTextNode(value));
    valueElem.appendChild(remove);
    return {'elem': valueElem, 'original': value};
}

function addTag(key, value){
    key = $.trim(escapeHTML(key));
    value = $.trim(escapeHTML(value));
    var normalizedKey = normalize(key);
    var normalizedValue = normalize(value);

    if(normalizedKey in tags){
	if(normalizedValue in tags[normalizedKey]['values']){
	    $(tags[normalizedKey]['values'][normalizedValue]['elem']).effect('highlight', {}, 3000);
	}else{
	    var valueTagDict = createValueTagDict(value, normalizedValue);
	    tags[normalizedKey]['values'][normalizedValue] = 
		valueTagDict;
	    tags[normalizedKey]['valueCol'].appendChild(valueTagDict['elem']);
	    $(valueTagDict['elem']).effect('highlight', {}, 3000);
	}
    }else{
	var row = document.createElement('tr');
	var keyCol = document.createElement('td');
	keyCol.className = 'key';
	keyCol.appendChild(document.createTextNode(key));
	row.appendChild(keyCol);
	var valueCol = document.createElement('td');
	row.appendChild(valueCol);

	var valueTagDict = createValueTagDict(value, normalizedValue);
	valueCol.appendChild(valueTagDict['elem']);

	tags[normalizedKey] = {'original': key,
			       'row': row,
			       'keyCol': keyCol,
			       'valueCol': valueCol,
			       'values': {}
	};
	tags[normalizedKey]['values'][normalizedValue] = valueTagDict;
	document.getElementById('current-tags').appendChild(row);
	$(keyCol).effect('highlight', {}, 3000);
	$(valueTagDict['elem']).effect('highlight', {}, 3000);

    }
}

$(document).ready(function(){
	$('#new-key').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    addTag($('#new-key').val(), $('#new-value').val());		    
		    $('#new-key').val('');
		    $('#new-value').val('');
		    break;
		}
	    });	 

	$('#new-value').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    addTag($('#new-key').val(), $('#new-value').val());
		    $('#new-value').val('');
		    break;
		}
	    });

	$('.tag-remove').live('click', function(event){
		var row = $(this).closest('tr');
		var key = normalize(row.find('.key').html());
		var valueElem = $(this).closest('.tag-value');
		var value = normalize(valueElem.attr('title'));
		delete tags[key]['values'][value];
		
		var valuesLeft = false;
		for(var val in tags[key]['values']){
		    valuesLeft = true;
		    break;
		}
		
		if(!valuesLeft){
		    document.getElementById('current-tags').removeChild(tags[key]['row']);
		    delete tags[key];
		}
		valueElem.remove();
		event.stopPropagation();
	    });
    });