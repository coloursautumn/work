$( document ).ready(function() {
	$('#id_VidScheta').parent().append('<select id="VidScheta"><option value="1" selected="selected">----------</option><option value="2">Расчетный</option><option value="3" >Депозитный</option><option value="4" >Ссудный</option><option value="5" >Иной</option></select>')

	$('#VidScheta').change(function() {
  		$('#id_VidScheta').val($('#VidScheta :selected').text())
	});

	$( "#id_ValyutaDenezhnyhSredstv" ).closest( "p" ).append( '<button id="ValyutaDenezhnyhSredstv">+</button></p>' );
	$("#ValyutaDenezhnyhSredstv").on( "click", function() {
        window.open("/Valyuty/new/");
    });
});