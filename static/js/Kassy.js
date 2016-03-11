$( document ).ready(function() {
    if($('#id_Vladelets').val()=='' && $.cookie('kassa')){
        $('#id_Vladelets').val($.cookie('kassa'));
        $.removeCookie("kassa", { path: '/Kassy' });
        $.each($('#id_Vladelets').find('option'),function(){
            if($(this).val() != $.cookie('kassa')){
                $(this).hide();
            }
        })
    }



	$( "#id_ValyutaDenezhnyhSredstv" ).closest( "p" ).append( '<button id="ValyutaDenezhnyhSredstv">+</button></p>' );
	$("#ValyutaDenezhnyhSredstv").on( "click", function() {
        window.open("/Valyuty/new/");
    });

    $( "#id_Roditel" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
	$("#Roditel").on( "click", function() {
        window.open("/Kassy/new/");
    });

    $( "#id_Vladelets" ).closest( "p" ).append( '<button id="Vladelets">+</button></p>' );
	$("#Vladelets").on( "click", function() {
        window.open("/Organizatsii/new/");
    });
});