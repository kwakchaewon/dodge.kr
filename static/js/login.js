function login(){
    $('#loginform').submit();
}


function keycode(){
    if(window.event.keyCode == 13){
        login();
    }
}