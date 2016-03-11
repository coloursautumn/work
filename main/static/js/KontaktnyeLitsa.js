function nameKon(){
    $('#id_Naimenovanie').val($('#id_Familiya').val() + " " + $('#id_Imya').val() + " " + $('#id_Otchestvo').val())
}


$('#id_Imya').change(function () {
    nameKon();
});

$('#id_Familiya').change(function () {
    nameKon();
});

$('#id_Otchestvo').change(function () {
    nameKon();
});