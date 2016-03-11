$( document ).ready(function() {
	
	if($("#id_Kontragent").val()==''){
		$('#id_DogovorKontragenta').parent().hide();
		$('#id_SdelkaZakazPostavschiku').parent().hide();
	}

	$('#id_Organizatsiya option').last().attr('selected', 'selected');
	
    $( "#id_Organizatsiya" ).closest( "p" ).append( '<button id="Organizatsiya">+</button>' );
    $("#Organizatsiya").on( "click", function() {
        window.open("/Organizatsii/new/");
    });
   	$( "#id_BankovskiySchetOrganizatsii" ).closest( "p" ).append( '<button id="BankovskiySchetOrganizatsii">+</button>' );
    $("#BankovskiySchetOrganizatsii").on( "click", function() {
        window.open("/BankovskieScheta/new/");
    });
   	$( "#id_FizLitso" ).closest( "p" ).append( '<button id="FizLitso">+</button>' );
    $("#FizLitso").on( "click", function() {
        window.open("/FizicheskieLitsa/new/");
    });
   	$( "#id_Kontragent" ).closest( "p" ).append( '<button id="Kontragent">+</button>' );
    $("#Kontragent").on( "click", function() {
        window.open("/Kontragenty/new/");
    });
   	$( "#id_DogovorKontragenta" ).closest( "p" ).append( '<button id="DogovorKontragenta">+</button>' );
    $("#DogovorKontragenta").on( "click", function() {
        window.open("/DogovoryKontragentov/new/");
    });
   	$( "#id_Podrazdelenie" ).closest( "p" ).append( '<button id="Podrazdelenie">+</button>' );
    $("#Podrazdelenie").on( "click", function() {
        window.open("/Podrazdeleniya/new/");
    });
    

	function ajaxkontragent(){
		$.ajax({
			type: "POST",
			url: '/getIdDocKontragentaPostavshika/',
			data: {id:$('#id_Kontragent option:selected').val()},
			success: function(data)
			{
				$("#id_DogovorKontragenta").val(data);
				if(data!=''){
					$('#id_SdelkaZakazPostavschiku').attr('disabled', false);
					$('#id_DogovorKontragenta').attr('disabled', false);
					$('#id_DogovorKontragenta').parent().show();
					$('#id_SdelkaZakazPostavschiku').parent().show();
					$.each($('#id_DogovorKontragenta').find('option'),function(){
						if($(this).val() != data){
							$(this).hide();
						}
					})
					$.ajax({
						type: "POST",
						url: '/getSdelkaDlyaPostavshika/',
						data: {id:$('#id_Kontragent option:selected').val()},
						success: function(data)
						{
							var array = [];
							$.each(data.split('?'), function(){
								array.push(this)
							})
							$.each($('#id_SdelkaZakazPostavschiku').find('option'),function(){
								if($(this).val() in array){
									
								}else{
									$(this).hide();
								}
							})
						}
					});
				}else{
					$('#id_SdelkaZakazPostavschiku').val('');
					$('#id_SdelkaZakazPostavschiku').attr('disabled', true);
					$('#id_DogovorKontragenta').attr('disabled', true);
				}
			}
		});
	};

	ajaxkontragent();
	
	$("#id_Kontragent").on( "change", function() {
		ajaxkontragent();
	});
});