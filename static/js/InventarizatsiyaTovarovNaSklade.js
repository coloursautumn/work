$(document).ready(function(){
	$('td.seriya').hide();
	$('td.seriya').prop('disabled', true);
	
	$('.zapolnit').on('click', function(){
		if($('#nomenklatura').is(':checked')){
			switch($('#nomenklatura').closest('p').find('#filter').val()){
				case 'ravno':{
					$.ajax({
			            type: "POST",
			            url: '//',
			            data: {id:$('#nomenklatura').closest('p').find('#id_Nomenklatura').val()},
			            success: function(data)
			            {
			                
			            }
			        });
				}
				case 'neRavno':{
					$.ajax({
			            type: "POST",
			            url: '//',
			            data: {nid:$('#nomenklatura').closest('p').find('#id_Nomenklatura').val()},
			            success: function(data)
			            {
			                
			            }
			        });
				}
			}
		}

		if($('#nomenklaturnayaGruppa').is(':checked')){
			switch($('#nomenklaturnayaGruppa').closest('p').find('#filter').val()){
				case 'ravno':{
					$.ajax({
			            type: "POST",
			            url: '//',
			            data: {id:$('#nomenklaturnayaGruppa').closest('p').find('#id_Nomenklatura').val()},
			            success: function(data)
			            {
			                
			            }
			        });
				}
				case 'neRavno':{
					$.ajax({
			            type: "POST",
			            url: '//',
			            data: {nid:$('#nomenklaturnayaGruppa').closest('p').find('#id_Nomenklatura').val()},
			            success: function(data)
			            {
			                
			            }
			        });
				}
			}
		}
	});

	$('#id_UchityvatSerii').on('click', function(){
		if($('#id_UchityvatSerii').is(':checked')){
			$('td.seriya').show();
			$('td.seriya').prop('disabled', false);
		}
		else{
			$('td.seriya').hide();
			$('td.seriya').prop('disabled', true);
		}
	});

})