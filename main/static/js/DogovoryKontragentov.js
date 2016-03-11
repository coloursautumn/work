$( document ).ready(function() {
    univer('#id_Vladelets','idKontragenty');
    univer('#id_Organizatsiya','kassa');

    function univer(id_polya, cookie_name){
        if($(id_polya).val()=='' && $.cookie(cookie_name)){
            $(id_polya).val($.cookie(cookie_name));
            $.removeCookie(cookie_name, { path: '/DogovoryKontragentov' });
            $.each($(id_polya).find('option'),function(){
                if($(this).val() != $.cookie(cookie_name)){
                    $(this).hide();
                }
            })
        }
    }
	$( "#id_Organizatsiya" ).closest( "p" ).append( '<button type="button" class="add-contact-form-button simple_add_button_organisation" >+</button>' );


    $(".simple_add_button_organisation").on( "click", function() {
        window.open("/Organizatsii/new/");
    });

    $( "#id_Roditel" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
    $("#Roditel").on( "click", function() {
        window.open("/DogovoryKontragentov/new/");
    });
    

    $( "#id_Vladelets" ).closest( "p" ).append( '<button type="button" class="add-contact-form-button simple_add_button_kontragent" >+</button>' );


    $(".simple_add_button_kontragent").on( "click", function() {
        window.open("/Kontragenty/new/");
    });

    $( "#id_ValyutaVzaimoraschetov" ).closest( "p" ).append( '<button type="button" class="add-contact-form-button simple_add_button_valiuta" >+</button>' );


    $(".simple_add_button_valiuta").on( "click", function() {
        window.open("/Valyuty/new/");
    });
    var a,L,epl=$("#id_Naimenovanie"); 
    function epl3(){a=epl.val();$("#id_NaimenovaniePolnoe").val(a)};epl3(); 
    $("#id_Naimenovanie").click(function (){setTimeout('epl3()',100)}); 
    epl.bind('mouseout mousemove keydown keypress keyup',function(e){epl3()});


});
