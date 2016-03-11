$( document ).ready(function() {
    if($("#id_VestiUchetPoSeriyam").is(":checked")) {
        $('#id_VestiPartionnyyUchetPoSeriyam').parent().show();
        $('#id_NomerGTD').parent().show();
        $('#id_StranaProishozhdeniya').parent().show();
        $('#NomerGTD').parent().show();
    }
    else {
        $('#id_VestiPartionnyyUchetPoSeriyam').parent().hide();
        $('#id_NomerGTD').parent().hide();
        $('#id_StranaProishozhdeniya').parent().hide();
        $('#NomerGTD').parent().hide();

        
    }

    $('#id_BazovayaEdinitsaIzmereniya').find('option:nth-child(2)').attr("selected", "selected");

    $( "#id_VestiUchetPoSeriyam" ).on( "click", function() {
        if($(this).is(":checked")) {
            $('#id_VestiPartionnyyUchetPoSeriyam').parent().show();
            $('#id_NomerGTD').parent().show();
            $('#id_StranaProishozhdeniya').parent().show();
            $('#NomerGTD').parent().show();
        }
        else {
            $('#id_VestiPartionnyyUchetPoSeriyam').parent().hide();
            $('#id_NomerGTD').parent().hide();
            $('#id_StranaProishozhdeniya').parent().hide();
            $('#NomerGTD').parent().hide();
        }
    });

    $("#NomerGTD").on( "click", function() {
        window.open("/NomeraGTD/new/");
    });
    $("#StatyaZatrat").on( "click", function() {
        window.open("/StatiZatrat/new/");
    });
    $("#Valuta").on( "click", function() {
        window.open("/Valyuty/new/");
    });
    $("#EdinitsaIzmereniy").on( "click", function() {
        window.open("/EdinitsyIzmereniya/new/");
    });
    $("#VidNomenklatury").on( "click", function() {
        window.open("/VidyNomenklatury/new/");
    });







    $(".saveTseny").on("click", function() {
        var arr = [];
        arr.push('idDocUst='+$('#id_UstanovkaTSenNomenklatury :selected').val());
        arr.push('idNomenklatury='+$('#id_obj').text());
        $.each($(this).parent().find('.cost'), function(){
            arr.push(ser(this)+'&');
        });
        $.ajax({
            type: "POST",
            url: '/saveTsenyNomenklatury/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(arr),
            success: function(data)
            {

            }
        });
    });

    $(".saveObj").on( "click", function() {
        var arr = [];
        arr.push($('#name_obj').text());
        arr.push($('#id_obj').text());
        arr.push(ser($('body').find('.form')));
        $.ajax({
            type: "POST",
            url: '/saveObj/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(arr),
            success: function(data)
            {   
                if($('#edinitsy table').find('tr').size()<2){
                    var brr = [];
                    brr.push($('#id_obj').text());
                    brr.push($('#id_BazovayaEdinitsaIzmereniya').val());
                    $.ajax({
                        type: "POST",
                        url: '/newEdinitsuForNomenklatura/',
                        contentType: 'application/json; charset=utf-8',
                        data: JSON.stringify(brr),
                        success: function(data)
                        {   
                            
                        }
                    });  
                }
                // location.reload(true);
            }
        });
    });


    function ser(el)
        {
            var serialized = $(el).serialize();
            if (!serialized) // not a form
                serialized = $(el).find('input[name],select[name],textarea[name]').serialize();
            return decodeURIComponent(serialized.replace(/\+/gi, " "));
        }

    $(".addEdinitsu").on( "click", function() {
        var arr = [];
        arr.push($('#name_obj').text());
        arr.push($('#id_obj').text());
        arr.push(ser($('body').find('.form')));
        $.ajax({
            type: "POST",
            url: '/saveObj/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(arr),
            success: function(data)
            {
                
            }
        });

        var date = new Date();
        date.setTime(date.getTime() + (60 * 15 * 1000));
        $.cookie('idNomenklatury', String($('#id_obj').text()), {path: '/EdinitsyIzmereniya'})
        location.href = "/EdinitsyIzmereniya/new/"

    });
    $(".delEdinitsu").on( "click", function() {
        var arr = [];
        arr.push($('#id_obj').text());
        $.ajax({
            type: "POST",
            url: '/delEdinitsuIzmereniya/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(arr),
            success: function(data)
            {
                // location.reload(true);
            }
        });
    });
    
    $('td #Tsena').on('click',function(){
        $(this).closest('tr').toggleClass('cost');
        if(!$(this).closest('tr').find('td:first input').is(':checked')){
            $(this).closest('tr').find('td:first input').prop('checked',true);
        }else{
            $(this).closest('tr').find('td:first input').prop('checked',false);
        }
    });

});
var a,L,epl=$("#id_Naimenovanie"); 
function epl3(){a=epl.val();$("#id_NaimenovaniePolnoe").val(a)};epl3(); 
$("#id_Naimenovanie").click(function (){setTimeout('epl3()',100)}); 
epl.bind('mouseout mousemove keydown keypress keyup',function(e){epl3()});