function searchBoard(){
    var target = document.getElementById('search__select').value;
    var query = document.getElementById('searchword__input__value').value;
    location.href= "?target=" + target +"&query="+query;
}

function insertSearchUp(){
    if(window.event.keyCode == 13){
        searchBoard();
    }
}