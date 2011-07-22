function escapeHTML(text){
    return $('<div/>').text(text).html();
}