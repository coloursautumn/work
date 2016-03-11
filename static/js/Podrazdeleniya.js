$( document ).ready(function() {

    $( "#id_Roditel" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
    $("#Roditel").on( "click", function() {
        window.open("/Podrazdeleniya/new/");
    });
});