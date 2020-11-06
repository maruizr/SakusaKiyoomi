$(function () {

    $("#formulario").validate({

        rules: {
            nombre: "required",
            email: {
                required: true,
                email: true
            },
            telefono: "required",
            fecha: "required",

        }, //rules

        messages: {
            nombre: {
                required: 'Ingresa nombre',
                nombre: 'No puede estar vacio'
            },
            email: {
                required: 'Ingresa tu correo electronico',
                email: 'Formato de correo no valido',

            },
            
            comentario:{
                required: 'Deje su recomendación',
                comentario:'Se necesita su recomendación'
            },

        } //messages

    }); //$('#formulario').validate
    
    

}); //function