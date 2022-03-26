function searchBoard(){
    var searchType = document.getElementById('search__select').value;
    var searchWord = document.getElementById('searchword__input__value').value;
    location.href= "?searchType=" + searchType +"&searchWord="+searchWord;
}

function insertSearchUp(){
    if(window.event.keyCode == 13){
        searchBoard();
    }
}