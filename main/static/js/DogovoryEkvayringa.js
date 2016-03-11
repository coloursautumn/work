$( document ).ready(function() {
	$( "#id_DogovorVzaimoraschetov" ).closest( "p" ).append( '<button id="Roditel">+</button></p>' );
	$("#Roditel").on( "click", function() {
		window.open("/DogovoryKontragentov/new/");
	});
	$( "#id_Ekvayrer" ).closest( "p" ).append( '<button id="Roditel2">+</button></p>' );
	$("#Roditel2").on( "click", function() {
		window.open("/Kontragenty/new/");
	});
});