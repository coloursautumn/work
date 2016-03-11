$( document ).ready(function() {
    $('#id_KodAdresnogoElementa').prop('readonly', true);

    $( "#id_Roditel" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
	$("#Roditel").on( "click", function() {
        window.open("/Regiony/new/");
    });
});