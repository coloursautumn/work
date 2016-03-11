$(document).ready(function(){

	$('#id_NaAvans').attr('disabled', true)
    $('#id_Organizatsiya option').last().attr('selected', 'selected');

	$('#id_NaAvans').attr('disabled', true);

    $("#Organizatsiyab").on( "click", function() {
        window.open("/Organizatsii/new/");
    });
    $("#Kontragen").on( "click", function() {
        window.open("/Kontragenty/new/");
    });
    $("#DogovorKontragent").on( "click", function() {
        window.open("/DogovoryKontragentov/new/");
    });


	$(document).on('change', '#id_DokumentOsnovanieRealizatsiyaTovarovUslug', function(){
		$.ajax({
            type: "POST",
            url: '/sysDoc/getSummaDocumentaForSchetaFacturyVidanniyRTU/',
            data: {"idDocumenta":$(this).val()},
            success: function(data)
            {	
            	$('#id_Organizatsiya').val('');
                $('#id_Kontragent').val('');
                $('#id_DogovorKontragenta').val('');
                $('.summaDoc').text('');
                console.log(data['SummaDokumenta']);
                $('.summaDoc').text(Number(data['SummaDokumenta']).toFixed(2));
                $('#id_Organizatsiya').val(data['Organizatsiya']);
                $('#id_Kontragent').val(data['Kontragent']);
                $('#id_DogovorKontragenta').val(data['DogovorKontragenta']);
            }
        });
	})

    $(document).on('change', '#id_DokumentOsnovanieVozvratTovarovPostavschiku', function(){
        $.ajax({
            type: "POST",
            url: '/sysDoc/getSummaDocumentaForSchetaFacturyVidanniyVTP/',
            data: {"idDocumenta":$(this).val()},
            success: function(data)
            {   
                $('#id_Organizatsiya').val('');
                $('#id_Kontragent').val('');
                $('#id_DogovorKontragenta').val('');
                $('.summaDoc').text('');
                console.log(data['SummaDokumenta']);
                $('.summaDoc').text(Number(data['SummaDokumenta']).toFixed(2));
                $('#id_Organizatsiya').val(data['Organizatsiya']);
                $('#id_Kontragent').val(data['Kontragent']);
                $('#id_DogovorKontragenta').val(data['DogovorKontragenta']);
            }
        });
    })
})