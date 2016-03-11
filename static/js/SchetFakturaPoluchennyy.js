$(document).ready(function(){
	$('#id_NaAvans').attr('disabled', true)

    $( "#id_DokumentOsnovaniePostuplenieTovarovUslug" ).closest( "div" ).append( '<button id="DokumentOsnovaniePostuplenieTovarovUslug">+</button>' );
    $("#DokumentOsnovaniePostuplenieTovarovUslug").on( "click", function() {
        window.open("/PostuplenieTovarovUslug/new/");
    });
    $( "#id_Kontragent" ).closest( "p" ).append( '<button id="Kontragent">+</button>' );
    $("#Kontragent").on( "click", function() {
        window.open("/Kontragenty/new/");
    });

    $( "#id_DogovorKontragenta" ).closest( "p" ).append( '<button id="DogovorKontragenta">+</button>' );
    $("#DogovorKontragenta").on( "click", function() {
        window.open("/DogovoryKontragentov/new/");
    });

	$(document).on('change', '#id_DokumentOsnovaniePostuplenieTovarovUslug', function(){
		$.ajax({
            type: "POST",
            url: '/sysDoc/getSummaDocumentaForSchetaFactury/',
            data: {"idDocumenta":$(this).val()},
            success: function(data)
            {	
            	$('#id_Organizatsiya').val('');
                $('#id_Kontragent').val('');
                $('#id_DogovorKontragenta').val('');
                $('.summaDoc').text('');
                
                $('.summaDoc').text(Number(data['SummaDokumenta']).toFixed(2));
                $('#id_Organizatsiya').val(data['Organizatsiya']);
                $('#id_Kontragent').val(data['Kontragent']);
                $('#id_DogovorKontragenta').val(data['DogovorKontragenta']);
            }
        });
	})
})