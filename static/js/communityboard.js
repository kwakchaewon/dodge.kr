function searchBoard(){
    var searchType = document.getElementById('search__select').value;
    var searchWord = document.getElementById('searchword__input__value').value;
    alert(searchType);
    alert(searchWord);
    location.href= "?searchType=" + searchType +"&searchWord="+searchWord;
}