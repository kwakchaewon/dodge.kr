function registUsr(){

//    id, 비밀번호, 이름, 이메일, 전화번호, 생년월일 미기재 시
    if (!$('#container__id').val())
    {
    alert('아이디를 입력해주세요.');
    return;
    }
    if (!$('#container__pw').val())
    {
    alert('비밀번호를 입력해주세요.');
    return;
    }
    if (!$('#container__email').val())
    {
    alert('이메일을 입력해주세요.');
    return;
    }
    if (!$('#container__phonenum').val())
    {
    alert('전화번호를 입력해주세요.');
    return;
    }
    if (!$('#container__birth').val())
    {
    alert('생년월일을 입력해주세요.');
    return;
    }

    // 비밀번호 확인불가시
    if ($('#container__pw').val() != $('#container__chkpw').val())
    {
    alert('비밀번호가 일치하지 않습니다')
    return;
    }

    $('#register_form').submit();

    }
