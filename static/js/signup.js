// 회원가입 버튼 클릭시
function registUsr(){

    // 아이디 미기재 시
    if (!$('#container__id').val())
    {
    alert('아이디를 입력해주세요.');
    $('#idcheck__result').html(
    "<font color='red'>아이디를 입력해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }

    // 아이디 중복 확인 안했을 시
    if ($('#idcheck__result').find("font").text() =='' || $('#idcheck__result').find("font").text() == '아이디를 중복을 확인해주세요.')
    {
    alert('아이디 중복을 확인해주세요.');
    $('#idcheck__result').html(
    "<font color='red'>아이디를 중복을 확인해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }

    // 아이디 중복시
    if ($('#idcheck__result').find("font").text() =='이미 존재하는 아이디입니다.')
    {
    alert('아이디 중복을 확인해주세요.');
    return;
    }


    // 비밀번호 미기재 시
    if (!$('#container__pw').val())
    {
    $('#password__result').html(
    "<font color='red'>비밀번호를 입력해주세요.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
    alert('비밀번호를 입력해주세요.');
    return;
    }

    // 이름 미기재 시
    if (!$('#container__name').val())
    {
    $('#namecheck__result').html(
    "<font color='red'>이름을 입력해주세요.</font><input type='hidden' name='namecheck__result' id='namecheck__result' value=0/>");
    alert('이름을 입력해주세요.');
    return;
    }

    // 이메일 미기재 시
    if (!$('#email__id').val() || !$('#email__domain').val())
    {
    $('#emailcheck__result').html(
    "<font color='red'>이메일을 입력해주세요.</font><input type='hidden' name='emailcheck__result' id='emailcheck__result' value=0/>");
    alert('이메일을 입력해주세요.');
    return;
    }

    // 전화번호 미기재 시
    if (!$('#container__phonenum').val())
    {
    $('#phonenumcheck__result').html(
    "<font color='red'>전화번호를 입력해주세요.</font><input type='hidden' name='phonenumcheck__result' id='phonenumcheck__result' value=0/>");
    alert('전화번호를 입력해주세요.');
    return;
    }

    // 생년월일 미기재 시
    if (!$('#container__birth').val())
    {
    $('#birthcheck__result').html(
    "<font color='red'>생년월일을 입력해주세요.</font><input type='hidden' name='birthcheck__result' id='birthcheck__result' value=0/>");
    alert('생년월일을 입력해주세요.');
    return;
    }

   // 비밀번호 불일치 시
    if ($('#container__pw').val() != $('#container__chkpw').val())
    {
    alert('비밀번호가 일치하지 않습니다.');
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
    if (!$('#container__id').val()){
    $('#idcheck__result').html(
    "<font color='red'>아이디를 입력해주세요.</font><input type='hidden' name='idcheck__result' id='idcheck__result' value=0/>");
    return;
    }

    $.ajax({
    type: "POST",
    url: "userIdCheck",

    data: {
        'username' : $('#container__id').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
    },
        success : function(response){
            $('#idcheck__result').html(response);
        },
    });
}


// 패스워드 입력 또는 변경 시
function inputPasswordChange(){

    if($('#container__pw').val() == $('#container__chkpw').val()){
        $('#passwordcheck__result').html(
        "<font color='green'>사용 가능한 비밀번호입니다.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
        return;
        }
    else
    {
        $('#passwordcheck__result').html(
        "<font color='red' display='block'>비밀번호를 확인해주세요.</font><input type='hidden' name='passwordcheck__result' id='passwordcheck__result' value=0/>");
        return;
    }
}


    // 이름  변경 시
    function inputNameChange(){
    }


    // 전화번호  변경 시
    function inputPhonenumChange(){
    }


    // 이메일  변경 시
    function inputEmailChange(){
    }


    // 생년월일  변경 시
    function inputBirthChange(){
    }