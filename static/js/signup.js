// 회원가입 버튼 클릭시
function registUsr(){

    // #container__id 값
    var idValue = $('#container__id').val()
    // 아이디 조건 정규표현식 (5~20자 영어 소문자, 숫자 조합)
    var idPattern= new RegExp('^[a-z0-9]{5,20}$');

    // #container__pw 값
    var pwVal = $('#container__pw').val()
    // #container__chkpw 값
    var chkpwVal = $('#container__chkpw').val()
    // 패스워드드 조건정규표현식 (8~20자 영문, 숫자, 특수문자 조합)
    var pwPattern= new RegExp('^[a-zA-Z0-9!@#$%^&*()?_~]{8,20}$');



    // 아이디 미기재 시
    if (!$('#container__id').val())
    {
    alert('아이디를 입력해주세요.');
    $('#container__id').focus();
    $('#idcheck__result').html(
    "<font color='red'>아이디를 입력해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }


    // 아이디 중복 확인 안했을 시
    if ($('#idcheck__result').find("font").text() =='' || $('#idcheck__result').find("font").text() == '아이디를 중복을 확인해주세요.')
    {
    alert('아이디 중복을 확인해주세요.');
    $('#container__id').focus();
    $('#idcheck__result').html(
    "<font color='red'>아이디를 중복을 확인해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }

    // 아이디 조건 (5~20자 영어 소문자, 숫자 조합)에 맞지 않을시
    if(!idPattern.test(idValue)){
    alert('아이디는 5~20자의 소문자 및 숫자로 사용 가능합니다.');
    $('#container__id').focus();
    return;
    }

    // 아이디 중복시
    if ($('#idcheck__result').find("font").text() =='이미 존재하는 아이디입니다.')
    {
    alert('아이디 중복을 확인해주세요.');
    $('#container__id').focus();
    return;
    }

    // 비밀번호 미기재 시
    if (!pwVal)
    {
    alert('비밀번호를 입력해주세요.');
    $('#container__pw').focus();
    $('#password__result').html(
    "<font color='red'>비밀번호를 입력해주세요.</font><input type='hidden' name='password__result' id='password__result' value=0/>");
    return;
    }

    // 비밀번호 조건(8~20자 영문, 숫자, 특수문자 조합)에 맞지 않을시
    if(!pwPattern.test(pwVal)){
        alert('비밀번호는 8~20자의 영문,숫자,특수문자로 사용 가능합니다.');
        $('#container__pw').focus();
        $('#password__result').html(
        "<font color='red'>비밀번호는 8~20자의 영문,숫자,특수문자로 사용 가능합니다.</font><input type='hidden' name='password__result' id='password__result' value=0/>");
        return;
    }

    // 비밀번호와 비밀번호 확인이 다를 시
    if(pwVal != chkpwVal){
        alert('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
        $('#container__chkpw').focus();
        $('#passwordcheck__result').html(
        "<font color='red' display='block'>비밀번호와 일치하지 않습니다.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
        return;
    }

    // 이름 미기재 시
    if (!$('#container__name').val())
    {
    alert('이름을 입력해주세요.');
    $('#container__name').focus();
    $('#namecheck__result').html(
    "<font color='red'>이름을 입력해주세요.</font><input type='hidden' name='namecheck__result' id='namecheck__result' value=0/>");
    return;
    }

    // 이메일 아이디 미기재 시
    if (!$('#email__id').val())
    {
    alert('이메일을 입력해주세요.');

    $('#emailcheck__result').html(
    "<font color='red'>이메일을 입력해주세요.</font><input type='hidden' name='emailcheck__result' id='emailcheck__result' value=0/>");
    return;
    }

    // 이메일 도메인 미 기재시
    if(!$('#email__domain').val())
    {
    alert('이메일을 입력해주세요.');
    $('#email__domain').focus();
    $('#emailcheck__result').html(
    "<font color='red'>이메일을 입력해주세요.</font><input type='hidden' name='emailcheck__result' id='emailcheck__result' value=0/>");
    return;
    }


    // 전화번호 미기재 시
    if (!$('#container__phonenum').val())
    {
    alert('전화번호를 입력해주세요.');
    $('#container__phonenum').focus();
    $('#phonenumcheck__result').html(
    "<font color='red'>전화번호를 입력해주세요.</font><input type='hidden' name='phonenumcheck__result' id='phonenumcheck__result' value=0/>");
    return;
    }

    // 생년월일 미기재 시
    if (!$('#container__birth').val())
    {
    alert('생년월일을 입력해주세요.');
    $('#container__birth').focus();
    $('#birthcheck__result').html(
    "<font color='red'>생년월일을 입력해주세요.</font><input type='hidden' name='birthcheck__result' id='birthcheck__result' value=0/>");
    return;
    }

   // 비밀번호 불일치 시
    if (pwVal != chkpwVal)
    {
    alert('비밀번호가 일치하지 않습니다.');
    $('#container__chkpw').focus();
    return;
    }

    $('#register_form').submit();
}


// 취소 버튼 클릭시
function cancel(){
    $(location).attr('href','login')
}


// 아이디 입력 또는 변경 시
function inputIdChange(){

    // #container__id 값
    var idValue = $('#container__id').val()
    // 아이디 조건 정규표현식 (5~20자 영어 소문자, 숫자 조합)
    var idPattern= new RegExp('^[a-z0-9]{5,20}$');

    // 아이디 조건에 부합하지 않을 시 (5~20자 영어 소문자+ 숫자 조합)
    if(!idPattern.test(idValue)){
    $('#idcheck__result').html(
    "<font color='red'>아이디는 5~20자의 소문자 및 숫자로 사용 가능합니다.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }


    // 아이디 미 입력시
    if (!idValue){
    $('#idcheck__result').html(
    "<font color='red'>아이디를 입력해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }

    $.ajax({
    type: "POST",
    url: "userIdCheck",

    data: {
        'username' : idValue,
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
    },
        success : function(response){
            $('#idcheck__result').html(response);
        },
    });
}


// 비밀번호 입력 또는 변경 시
function inputPasswordChange(){

    // #container__pw 값
    var pwVal = $('#container__pw').val()
    // #container__chkpw 값
    var chkpwVal = $('#container__chkpw').val()

    // 패스워드 조건정규표현식 (8~20자 영문, 숫자, 특수문자 조합)
    var pwPattern= new RegExp('^[a-zA-Z0-9!@#$%^&*()?_~]{8,20}$');

    if(pwPattern.test(pwVal)){
        $('#password__result').html(
        "<font color='green'>사용 가능한 비밀번호입니다.</font><input type='hidden' name='password__result' id='password__result' value=0/>");
        return;
    }
    else{
        $('#password__result').html(
        "<font color='red'>비밀번호는 8~20자의 영문,숫자,특수문자로 사용 가능합니다.</font><input type='hidden' name='password__result' id='password__result' value=0/>");

        return;
    }
}


// 비밀번호 확인 입력 또는 변경시
    function inputChkpwChange(){

    // #container__pw 값
    var pwVal = $('#container__pw').val()
    // #container__chkpw 값
    var chkpwVal = $('#container__chkpw').val()

    if(pwVal == chkpwVal){
        $('#passwordcheck__result').html(
        "<font color='green' display='block'>비밀번호와 일치합니다.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
        return;
    }
    else{
        $('#passwordcheck__result').html(
        "<font color='red' display='block'>비밀번호와 일치하지 않습니다.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
        return;
    }
    }


    // 이름 입력 또는 변경 시
    function inputNameChange(){

    // #container__name 값
    var nameVal = $('#container__name').val()

    if(!nameVal){
        $('#namecheck__result').html(
        "<font color='red' display='block'>이름을 입력해주세요.</font><input type='hidden' name='namecheck__result' id='namecheck__result' value=0/>");
        return;
    }
    else{
        $('#namecheck__result').html(
        "<font color='green' display='block'>이름 입력완료</font><input type='hidden' name='namecheck__result' id='namecheck__result' value=0/>");
        return;
    }

    }


    // 전화번호 입력 또는 변경 시
    function inputPhonenumChange(){

    // #container__phonenum 값
    var phonenumVal = $('#container__phonenum').val()

    if(!phonenumVal){
        $('#phonenumcheck__result').html(
        "<font color='red' display='block'>전화번호를 입력해주세요.</font><input type='hidden' name='phonenumcheck__result' id='phonenumcheck__result' value=0/>");
        return;
    }
    else{
        $('#phonenumcheck__result').html(
        "<font color='green' display='block'>전화번호 입력완료</font><input type='hidden' name='phonenumcheck__result' id='phonenumcheck__result' value=0/>");
        return;
    }
    }


    // 이메일 입력 또는 변경 시
    function inputEmailChange(){

    // #container__pw 값
    var emailidVal = $('#email__id').val()
    var domainVal = $('#email__domain').val()

    if(!emailidVal || !domainVal){
        $('#emailcheck__result').html(
        "<font color='red' display='block'>이메일을 입력해주세요.</font><input type='hidden' name='emailcheck__result' id='emailcheck__result' value=0/>");
        return;
    }
    else{
        $('#emailcheck__result').html(
        "<font color='green' display='block'>이메일 입력완료</font><input type='hidden' name='emailcheck__result' id='emailcheck__result' value=0/>");
        return;
    }
    }


    // 생년월일  입력 또는 변경 시
    function inputBirthChange(){

    // #container__birth 값
    var birthVal = $('#container__birth').val()

    if(!birthVal){
        $('#birthcheck__result').html(
        "<font color='red' display='block'>생년월일을 입력해주세요.</font><input type='hidden' name='birthcheck__result' id='birthcheck__result' value=0/>");
        return;
    }
    else{
        $('#birthcheck__result').html(
        "<font color='green' display='block'>생년월일 입력완료</font><input type='hidden' name='birthcheck__result' id='birthcheck__result' value=0/>");
        return;
    }
    }