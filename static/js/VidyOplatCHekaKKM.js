function kredit_hide(){
	$('label[for=id_BankKreditor], input#id_BankKreditor').hide();
    $('#id_BankKreditor').hide();
    $('label[for=id_DogovorVzaimoraschetovBankaKreditora], input#id_DogovorVzaimoraschetovBankaKreditora').hide();
    $('#id_DogovorVzaimoraschetovBankaKreditora').hide();
    $('label[for=id_ProtsentBankovskoyKomissii], input#id_ProtsentBankovskoyKomissii').hide();
    $('#id_ProtsentBankovskoyKomissii').hide();
}

function kredit_show(){
	$('label[for=id_BankKreditor], input#id_BankKreditor').show();
    $('#id_BankKreditor').show();
    $('label[for=id_DogovorVzaimoraschetovBankaKreditora], input#id_DogovorVzaimoraschetovBankaKreditora').show();
    $('#id_DogovorVzaimoraschetovBankaKreditora').show();
    $('label[for=id_ProtsentBankovskoyKomissii], input#id_ProtsentBankovskoyKomissii').show();
    $('#id_ProtsentBankovskoyKomissii').show();
}

$( document ).ready(function() {
	kredit_hide();
	if ($('#id_TipOplaty :selected').text() == "Банковский кредит") {
        kredit_show();
    }
});

$('select[name=TipOplaty]').change(function () {
    if ($('#id_TipOplaty :selected').text() == "Банковский кредит") {
        kredit_show();
    } else {
        kredit_hide();
    }
});