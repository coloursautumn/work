$( document ).ready(function() {

/*    $( "#id_KontaktnoeLitso option" ).last().attr('selected', 'selected');*/
    
    /*if (localStorage.getItem('id_UdostovereniyaLichnosti') != null){
        $("#id_UdostovereniyaLichnosti").val(localStorage.getItem('id_UdostovereniyaLichnosti')); 
    }
    if (localStorage.getItem('id_Kommentariy') != null){
        $("#id_Kommentariy").val(localStorage.getItem('id_Kommentariy')); 
    }
    if (localStorage.getItem('id_Dolzhnost') != null){
        $("#id_Dolzhnost").val(localStorage.getItem('id_Dolzhnost')); 
    }*/

    /*$.ajax({
            type: "POST",
            url: '/getDateOfBirthKontLitsa/',
            data: {id:$('#id_KontaktnoeLitso option:selected').val()},
            success: function(data)
            {
                var array = [];
                $.each(data.split('?'), function(){
                    array.push(this)
                    })
                
                if( $("#id_DataRozhdeniya").val()!=array[0] && $(array[0])!= 'None'){
                    $("#id_DataRozhdeniya").val(array[0]); 

                    }  
                if( $("#id_Kontakty").val()!=array[2] && $(array[2])!= 'None'){
                    $("#id_Kontakty").val(array[2]); 
                    } 
                if( (array[1]) == "Мужской"){
                    $( "#id_Pol option" ).eq(1).attr('selected', 'selected');                  
                }else if ((array[1])== "Женский"){
                    $( "#id_Pol option" ).eq(2).attr('selected', 'selected');
                }else {
                    $( "#id_Pol option" ).eq(0).attr('selected', 'selected');
                }


            },
            error:function(data)  
            {   

                console.log('error')    
            },
        })*/


    univer('#id_Vladelets','idKontragent');


    function univer(id_polya, cookie_name){
        if($(id_polya).val()=='' && $.cookie(cookie_name)){
            $(id_polya).val($.cookie(cookie_name));
            $.removeCookie(cookie_name, { path: '/KontaktnyeLitsaKontragentov' });
            $.each($(id_polya).find('option'),function(){
                if($(this).val() != $.cookie(cookie_name)){
                    $(this).hide();
                }
            })
        }
    }
    

    if($('#id_DataRozhdeniya').val() != ''){
        $('#id_NapominatODneRozhdeniya').prop('disabled', false);
    }
    else{
        $('#id_NapominatODneRozhdeniya').prop('disabled', true);
        $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', true);
    }

    if($('#id_NapominatODneRozhdeniya').is(':checked')){
        $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', false);
    }
    else{
        $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', true);
    }

    $("#id_DataRozhdeniya").change(function() {
        if($('#id_DataRozhdeniya').val() != ''){
    	    $('#id_NapominatODneRozhdeniya').prop('disabled', false);
        }
        else{
    	    $('#id_NapominatODneRozhdeniya').prop('disabled', true);
    	    $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', true);
        }
    });

    $("#id_NapominatODneRozhdeniya").change(function() {
        if($('#id_NapominatODneRozhdeniya').is(':checked')){
    	    $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', false);
        }
        else{
    	    $('#id_KolichestvoDneyDoNapominaniya').prop('disabled', true);
        }
    });

/*    $( "#id_KontaktnoeLitso" ).closest( "p" ).append( '<button type="button" class="btn btn-primary add-contact-form-button"  data-toggle="modal" data-target="#add-contact">+</button>' );
*/    
    $('#id_Kod').prop('readonly', true);
/*    $('p #id_Kod').prop('readonly', true);

*/
    $( "#id_KontaktnoeLitso" ).closest( "p" ).append( '<button type="button" class="add-contact-form-button simple_add_button_contact" >+</button>' );


    $(".simple_add_button_contact").on( "click", function() {
                window.open("/KontaktnyeLitsa/new/");
    });

    $( "#id_Vladelets" ).closest( "p" ).append( '<button type="button" class="add-contact-form-button simple_add_button_contragent" >+</button>' );

    $(".simple_add_button_contragent").on( "click", function() {
        window.open("/Kontragenty/new/");
    });


    function ser(el) {
        var serialized = $(el).serialize();
        if (!serialized) // not a form
            serialized = $(el).find('input[name],select[name],textarea[name]').serialize();
        return decodeURIComponent(serialized.replace(/\+/gi, " "));
    }

    function sendAjax(data) {
        $.ajax({
            type: "POST",
            url: '/saveObj/',
            contentType: 'application/json; charset=utf-8',
            data: data,
            success: function(data)
            {
                location.reload(true);
            }
        });
    }

    $(".saveObj").on("click", function() {
        var arr = [];
        arr.push(window.location.href.toString().split('/')[3]);
        arr.push($(this).data('id'));
        //arr.push($('#id_Kod').val().substr(2));
        arr.push(ser($('body').find('.form')));
        sendAjax(JSON.stringify(arr));
        window.localStorage.clear();
        /*location.reload();*/
        return false;
        /*window.close();*/
    });

    $('.new-contact-btn').on('click', function() {
        var arr = [];
        arr.push('KontaktnyeLitsa');
        arr.push($('#id_new_contact').text());
        arr.push(ser($('body').find('.add-contact-form')));
        sendAjax(JSON.stringify(arr));

    });


    /*$(".add-contact-form-button").one( "click", function() {
        $.ajax({
            type: "POST",
            url: '/addKontaktnogoLitsaForForm/',
            success: function(data)
            {
                if(data!=''){
                    console.log(data)
                    $( "#add_form_plase" ).append( '{{data.as_p}}' );

                    $('.add-contact-form #id_Kod').val('DL'+ data);
                    $('#id_new_contact').text(data);
                }   
            },
            error:function(data)  
            {   
                console.log('error')    
            },
        });
    });

    function nameKon(){
    $('#id_Naimenovanie').val($('#id_Familiya').val() + " " + $('#id_Imya').val() + " " + $('#id_Otchestvo').val())
    }


    $('#id_Imya').keyup(function () {
        nameKon();
    });

    $('#id_Familiya').keyup(function () {
        nameKon();
    });

    $('#id_Otchestvo').keyup(function () {
        nameKon();
    });*/


    $("#id_KontaktnoeLitso").on( "change", function() {
        /*localStorage.setItem( 'id_KontaktnoeLitso' , this.value);*/
        console.log(this.value)
        $.ajax({
            type: "POST",
            url: '/getDateOfBirthKontLitsa/',
            data: {id:$('#id_KontaktnoeLitso option:selected').val()},
            success: function(data)
            {
                var array = [];
                $.each(data.split('?'), function(){
                    array.push(this)
                    })
                
                if( $("#id_DataRozhdeniya").val()!=array[0] && $(array[0])!= 'None'){
                    $("#id_DataRozhdeniya").val(array[0]); 
                    /*localStorage.setItem( 'id_DataRozhdeniya' , array[0] );*/
                    } 
                if( (array[1]) == "Мужской"){
                    $( "#id_Pol option" ).eq(1).attr('selected', 'selected');                  
                }else if ((array[1])== "Женский"){
                    $( "#id_Pol option" ).eq(2).attr('selected', 'selected');
                }else {
                    $( "#id_Pol option" ).eq(0).attr('selected', 'selected');
                }
                if( $("#id_Kontakty").val()!=array[2] && $(array[2])!= 'None'){
                    $("#id_Kontakty").val(array[2]); 
                } 
                /*localStorage.setItem( 'id_Kontakty' , array[2] );*/


            },
            error:function(data)  
            {   

                console.log('error')    
            },
        })
    });

    /*$("input").on( "keyup", function() {
        localStorage.setItem( this.id , $(this).val());
    });
    $("input").on( "change", function() {
        localStorage.setItem( this.id , $(this).val());
    });*/

    /*$("#id_KontaktnoeLitso").on("change") , function(){
        localStorage.setItem( '#id_KontaktnoeLitso' , this.value);
        console.log(this.value)
        localStorage.setItem( 'id_DataRozhdeniya' , $('#id_DataRozhdeniya').val());
    };*/
    /*console.log( $('#id_KontaktnoeLitso').val())
    console.log($('#id_DataRozhdeniya').first().val())*/


    /*$('.reload_window').on('click', function() {
            localStorage.setItem( 'id_UdostovereniyaLichnosti' , $('#id_UdostovereniyaLichnosti').val());
            localStorage.setItem( 'id_Dolzhnost' , $('#id_Dolzhnost').val());
            localStorage.setItem( 'id_Kommentariy' , $('#id_Kommentariy').val());
            location.reload();
    });
    $('.close_window').on('click', function() {
        window.localStorage.clear();
        window.close();   

    });*/
        
});

    

    


/*
onclick="window.location.href='/page2'"
*/

/*    $("#dobKL").on( "click", function() {
        window.open("/KontaktnyeLitsa/new/");
    });*/

/*    function ser(el) {
        var serialized = $(el).serialize();
        if (!serialized) // not a form
            serialized = $(el).find('input[name],select[name],textarea[name]').serialize();
        return decodeURIComponent(serialized.replace(/\+/gi, " "));
    }
*/

