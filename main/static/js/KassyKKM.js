$( document ).ready(function() {
	$('label[for=id_FormirovatNefiskalnyeCHeki]').remove();
    $('#id_FormirovatNefiskalnyeCHeki').remove();
    
    $( "#id_Vladelets" ).closest( "p" ).append( '<button id="Vladelets">+</button></p>' );
	$("#Vladelets").on( "click", function() {
        window.open("/Organizatsii/new/");
    });
});