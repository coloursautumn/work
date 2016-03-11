$( document ).ready(function() {
    $('#id_Kod').prop('readonly', false);

	var a,L,epl=$("#id_Naimenovanie"); 
	function epl3(){a=epl.val();$("#id_NaimenovaniePolnoe").val(a)};epl3(); 
	$("#id_Naimenovanie").click(function (){setTimeout('epl3()',100)}); 
epl.bind('mouseout mousemove keydown keypress keyup',function(e){epl3()});
});