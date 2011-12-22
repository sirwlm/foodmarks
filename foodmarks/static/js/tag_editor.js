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
    var cleanedTags = {};
    for(var key in tags){
	var originalValues = tags[key]['values']
	var values = {};
	for(var value in originalValues){
	    values[value] = {'id': originalValues[value]['id'],
			     'deleted': originalValues[value]['deleted']};
	}
	cleanedTags[key] = values;
	}

    return JSON.stringify(cleanedTags);
}

function normalize(val){
    return val.toLowerCase().replace(/\s/g, '').replace(':', '');
}

function createValueTagDict(value){
    var valueElem = document.createElement('span');
    valueElem.className = 'tag-value';
    valueElem.title = value;

    var remove = document.createElement('span');
    remove.className = 'tag-remove';
    remove.appendChild(document.createTextNode('X'));

    valueElem.appendChild(document.createTextNode(value));
    valueElem.appendChild(remove);
    return {'elem': valueElem,};
}

function addTag(key, value, id){
    if(key in tags){
	if(value in tags[key]['values']){
	    $(tags[key]['row']).show();
	    var valueDict = tags[key]['values'][value];
	    valueDict['deleted'] = false;
	    $(valueDict['elem']).show().effect('highlight', {}, 3000);
	}else{
	    var valueTagDict = createValueTagDict(value);
	    tags[key]['values'][value] = valueTagDict;
	    if(id != null) valueTagDict['id'] = id;
	    tags[key]['valueCol'].appendChild(valueTagDict['elem']);
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

	var valueTagDict = createValueTagDict(value);
	if(id != null) valueTagDict['id'] = id;
	valueCol.appendChild(valueTagDict['elem']);

	tags[key] = {
	       'row': row,
	       'keyCol': keyCol,
	       'valueCol': valueCol,
	       'values': {}
	};
	tags[key]['values'][value] = valueTagDict;
	document.getElementById('current-tags').appendChild(row);
	$(keyCol).effect('highlight', {}, 3000);
	$(valueTagDict['elem']).effect('highlight', {}, 3000);
    }
}

$(document).ready(function(){
	$('#tag-loader').hide();

	$('#new-key').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    var key = normalize($.trim(escapeHTML($('#new-key').val())));
		    var value = normalize($.trim(escapeHTML($('#new-value').val())));
		    if(key != ''){
			addTag(key, value);
			$('#new-key').val('');
			$('#new-value').val('');
		    }
		    break;
		}
	    });

	$('#new-value').keydown(function(e){
		switch(parseInt(e.keyCode)){
		case 13:
		    e.preventDefault();
		    var key = normalize($.trim(escapeHTML($('#new-key').val())));
		    var value = normalize($.trim(escapeHTML($('#new-value').val())));

		    if(value != ''){
			if(key == ''){
			    $('#tag-loader').show();
			    $.get('/tag/category', {'value': value},
				  function(data){
				      if(data['status'] == 'OK' && data['categories'].length != 0)
					  $('#new-key').val(data['categories'][0]);
				      $('#tag-loader').hide();
				  });
			}else {
			    addTag(key, value);
			    $('#new-key').val('');
			    $('#new-value').val('').focus();
			}
		    }
		    break;
		}
	    });

	$('#edit-tags').on('click', '.tag-remove', function(event){
		var row = $(this).closest('tr');
		var key = normalize(row.find('.key').html());
		var valueElem = $(this).closest('.tag-value');
		var value = normalize(valueElem.attr('title'));
		tags[key]['values'][value]['deleted'] = true;
		valueElem.hide();
		if(row.find('.tag-value:visible').length == 0)
		    row.hide();
		event.stopPropagation();
	    });
    });