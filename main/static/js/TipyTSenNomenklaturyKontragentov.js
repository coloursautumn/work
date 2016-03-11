$( document ).ready(function() {

	$( "#id_ValyutaTSeny" ).closest( "p" ).append( '<button id="ValyutaTSeny">+</button></p>' );
	$("#ValyutaTSeny").on( "click", function() {
        window.open("/Valyuty/new/");
    });

    $( "#id_TipTSenNomenklatury" ).closest( "p" ).append( '<button id="TipTSenNomenklatury">+</button></p>' );
	$("#TipTSenNomenklatury").on( "click", function() {
        window.open("/TipyTSenNomenklatury/new/");
    });

    $( "#id_Vladelets" ).closest( "p" ).append( '<button id="Vladelets">+</button></p>' );
	$("#Vladelets").on( "click", function() {
        window.open("/Kontragenty/new/");
    });
});