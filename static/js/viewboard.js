function insertComment(){

    $.ajax({
    type: "POST",
    url: insertCommentHref,

    data: {
        'content' : $('#comment__textarea').val(),
        'username': username,
        'boardId': boardId,
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
    },
        success : function(response){
        let str = '<tr><td>'+response.content+'</td><td>'+response.username+'</td><td>'+response.registered_date+'</td></tr>';
        $('#commentTable>tbody:first').append(str);
        $('#comment__textarea').val("");
        },
    });
}