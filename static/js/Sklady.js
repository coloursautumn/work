$( document ).ready(function() {

    $( "#id_TipTSenRoznichnoyTorgovli" ).closest( "p" ).append( '<button id="TipTSenRoznichnoyTorgovli"">+</button>' );
    $("#TipTSenRoznichnoyTorgovli").on( "click", function() {
        window.open("/TipyTSenNomenklatury/new/");
    });

    $( "#id_Podrazdelenie" ).closest( "p" ).append( '<button id="Podrazdelenie">+</button>' );
    $("#Podrazdelenie").on( "click", function() {
        window.open("/Podrazdeleniya/new/");
    });

    $( "#id_Roditel" ).closest( "p" ).append( '<button id="Roditel">+</button>' );
    $("#Roditel").on( "click", function() {
        window.open("/FizicheskieLitsa/new/");
    });
});

$("#id_VidSklada").change(function() {
    if($('#id_VidSklada :selected').text() == 'НТТ'){
        $('#id_RaschetRoznichnyhTSenPoTorgovoyNatsenke').prop('disabled', false);
        $('#id_NomerSektsii').prop('disabled', true);
    }
    else{
        $('#id_RaschetRoznichnyhTSenPoTorgovoyNatsenke').prop('disabled', true);
        $('#id_RaschetRoznichnyhTSenPoTorgovoyNatsenke').prop('checked', false);
        $('#id_NomerSektsii').prop('disabled', false);
    }
});
