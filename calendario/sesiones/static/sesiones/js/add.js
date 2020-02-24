function addSessionGroup(idGroup) {
    alert(idGroup);
    var token = csrftoken;

    $.ajax({
        url: "addSessionGroup/",
        dataType: 'json',
        data: {
            idGroup: idGroup,
            body: body,
            type: type,
            name: name,
            'csrfmiddlewaretoken': token
        },
        type: "POST",
        success: function (response) {
            alert("Sesión agregada");
        },
        error: function (data) {
            // Código de error alert(data.status);
            // Mensaje de error alert(data.responseJSON.error);
        }
    });
}