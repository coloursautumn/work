$( document ).ready(function() {
	if($('#id_VidTipaTSeny option:selected').text()=="Базовый"){
		$('#id_SposobRaschetaTSeny, #id_BazovyyTipTSen, #id_ProtsentSkidkiNatsenki').prop('disabled', true);
	}else{
		$('#id_SposobRaschetaTSeny, #id_BazovyyTipTSen, #id_ProtsentSkidkiNatsenki').prop('disabled', false);
	}
	$( "#id_VidTipaTSeny" ).change(function() {
		if($('#id_VidTipaTSeny option:selected').text()=="Базовый"){
			$('#id_SposobRaschetaTSeny, #id_BazovyyTipTSen, #id_ProtsentSkidkiNatsenki').prop('disabled', true);
		}else{
			$('#id_SposobRaschetaTSeny, #id_BazovyyTipTSen, #id_ProtsentSkidkiNatsenki').prop('disabled', false);
		}
	});

    $( "#id_ValyutaTSeny" ).closest( "p" ).append( '<button id="ValyutaTSeny"">+</button>' );
    $("#ValyutaTSeny").on( "click", function() {
        window.open("/Valyuty/new/");
    });
    $( "#id_BazovyyTipTSen" ).closest( "p" ).append( '<button id="BazovyyTipTSen"">+</button>' );
    $("#BazovyyTipTSen").on( "click", function() {
        window.open("/TipyTSenNomenklatury/new/");
    });


});