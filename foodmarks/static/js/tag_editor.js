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

function createValueTagDict(value){
    var valueElem = document.createElement('span');
    valueElem.setAttribute('class', 'tag-value');
    valueElem.appendChild(document.createTextNode(value));
    return {'elem': valueElem, 'original': value};
}

function addTag(key, value){
    key = $.trim(escapeHTML(key));
    value = $.trim(escapeHTML(value));
    var normalizedKey = key.toLowerCase().replace(/\s/g, '');
    var normalizedValue = value.toLowerCase().replace(/\s/g, '');

    if(normalizedKey in tags){
	if(normalizedValue in tags[normalizedKey]['values']){
	    $(tags[normalizedKey]['values'][normalizedValue]['elem']).effect('highlight', {}, 3000);
	}else{
	    var valueTagDict = createValueTagDict(value);
	    tags[normalizedKey]['values'][normalizedValue] = 
		valueTagDict;
	    tags[normalizedKey]['valueCol'].appendChild(valueTagDict['elem']);
	    $(valueTagDict['elem']).effect('highlight', {}, 3000);
	}
    }else{
	var row = document.createElement('tr');
	var keyCol = document.createElement('td');
	keyCol.appendChild(document.createTextNode(key));
	row.appendChild(keyCol);
	var valueCol = document.createElement('td');
	row.appendChild(valueCol);

	var valueTagDict = createValueTagDict(value);
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
    });