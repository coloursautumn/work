$( document ).ready(function() {
	$( "#id_Vladelets" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
	$("#Roditel").on( "click", function() {
		window.open("/Nomenklatura/new/");
	});
});