$( document ).ready(function() {
    $("#Organizatsiya").on( "click", function() {
        window.open("/Organizatsii/new/");
    });
    $("#TipTSen").on( "click", function() {
        window.open("/TipyTSenNomenklatury/new/");
    });
    $("#KassaKKM").on( "click", function() {
        window.open("/KassyKKM/new/");
    });
    $("#Sklad").on( "click", function() {
        window.open("/Sklady/new/");
    });
    $("#Podrazdelenie").on( "click", function() {
        window.open("/Podrazdeleniya/new/");
    });
    $("#Nomenklatura").on( "click", function() {
        window.open("/Nomenklatura/new/");
    });
    $("#ed").on( "click", function() {
        window.open("/EdinitsyIzmereniya/new/");
    });
    $("#id_OtrazhatVBuhgalterskomUchete").on( "click", function() {
        if($(this).is(":checked")){
            $('#id_OtrazhatVNalogovomUchete').prop('disabled', false);
        }
        else{
            $('#id_OtrazhatVNalogovomUchete').prop('disabled', true);
            $('#id_OtrazhatVNalogovomUchete').prop('checked', false);
        }
    });
    if($('#id_OtrazhatVBuhgalterskomUchete').is(":checked")){
        $('#id_OtrazhatVNalogovomUchete').prop('disabled', false);
    }
    else{
        $('#id_OtrazhatVNalogovomUchete').prop('disabled', true);
        $('#id_OtrazhatVNalogovomUchete').prop('checked', false);
    }



    $.each($('body').find('.Kolichestvo input'),function(){
        pereschet($(this));
    });

    $(document).on('change', '#id_TipTSen', function(){

        $.each($('#myTabContent').find('.nomenklatura select'),function(){
            var el = $(this);
            $.ajax({
                type: "POST",
                url: '/getTovarOptions/',
                data: {"TipyTSen":$('#id_TipTSen').val(), "Nomenklatura":$(this).val()},
                success: function(data)
                {
                    $('.formTovary').append(data);
                    $(el).closest('tr').find('#id_EdinitsaIzmereniya').val($('.formTovary').find('#id_EdinitsaIzmereniya').val());
                    $(el).closest('tr').find('#id_Koeffitsient').val($('.formTovary').find('#id_Koeffitsient').val());
                    $(el).closest('tr').find('#id_TSena').val($('.formTovary').find('#id_TSena').val());
                    $(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val($('.formTovary').find('#id_ProtsentSkidkiNatsenki').val());
                    $(el).closest('tr').find('#id_StavkaNDS').val($('.formTovary').find('#id_StavkaNDS').val());
                    $('.formTovary').empty();
                }
            });
        });
    });

    function resultat(){
        sumObs = 0;
        $.each($('body').find('.Summa input'), function(){
            sumObs += Number($(this).val());
        });
        $('#summaObs').text(sumObs.toFixed(2));
        ndsObs = 0;
        $.each($('body').find('.SummaNDS input'), function(){
            ndsObs += Number($(this).val());
        });
        $('#id_SummaDokumenta').val($('#summaObs').text());
        $('#ndsObs').text(ndsObs.toFixed(2));
    }

    $(".save").on("click", function() {
        resultat();
    });

    $.each($('tbody #id_Nomenklatura'), function(){
        kol = $(this).closest('tr').find('#id_Kolichestvo').first().val();
        tsen = $(this).closest('tr').find('#id_TSena').first().val();

        if($(this).closest('tr').find('#id_Koeffitsient').first().val()!=''){
            koef = $(this).closest('tr').find('#id_Koeffitsient').first().val();
        }else{
            koef = 1;
        }

        proizved =  Number(kol)*Number(tsen);

        $(this).closest('tr').find('.SummaBezSkidki').val(proizved.toFixed(2));
        $(this).closest('tr').find('#id_SummaNDS').closest('td').next().text(Number($(this).closest('tr').find('#id_Summa').val()).toFixed(2));

        
    });
    resultat();

    $(document).on('change', '#id_Nomenklatura', function(){
        var el = $(this);
            $.ajax({
                type: "POST",
                url: '/getTovarOptions/',
                data: {"TipyTSen":$('#id_TipTSen').val(), "Nomenklatura":$(this).val()},
                success: function(data)
                {
                    $('.formTovary').append(data);
                    $(el).closest('tr').find('#id_EdinitsaIzmereniya').val($('.formTovary').find('#id_EdinitsaIzmereniya').val());
                    $(el).closest('tr').find('#id_Koeffitsient').val($('.formTovary').find('#id_Koeffitsient').val());
                    $(el).closest('tr').find('#id_TSena').val($('.formTovary').find('#id_TSena').val());
                    $(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val($('.formTovary').find('#id_ProtsentSkidkiNatsenki').val());
                    $(el).closest('tr').find('#id_StavkaNDS').val($('.formTovary').find('#id_StavkaNDS').val());
                    $('.formTovary').empty();
                }
            });
    })
   
    $(document).on('change', '#id_Kolichestvo, #id_StavkaNDS, td.selection div',  function() {
 
 
        pereschet(this);

    });
 
 
    function pereschet(el){
        kol = $(el).closest('tr').find('#id_Kolichestvo').first().val();
        tsen = $(el).closest('tr').find('#id_TSena').first().val();

        if($(el).closest('tr').find('#id_Koeffitsient').first().val()!=''){
            koef = $(el).closest('tr').find('#id_Koeffitsient').first().val();
        }else{
            koef = 1;
        }

        proizved =  Number(kol)*Number(tsen);

        if($(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val()!=''){
            $(el).closest('tr').find('#id_Summa').val((proizved-(proizved*(Number($(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val())/100)).toFixed(2)));
        }
        else{
            $(el).closest('tr').find('#id_Summa').val(proizved.toFixed(2));
        }
        
        $(el).closest('tr').find('.SummaBezSkidki').val(proizved.toFixed(2));
         
 
        var stavkaN = 0;
       
        if(stavkaN = $(el).closest('tr').find('#id_StavkaNDS option:selected').text().split('%')[0]){
            stavkaN = Number(stavkaN);
        }
        else{
            stavkaN = Number($(el).closest('tr').find('#id_StavkaNDS option:selected').text());
        }
       
        $(el).closest('tr').find('#id_SummaNDS').val(Number(($(el).closest('tr').find('#id_Summa').val())/
            Number('1.'+stavkaN)*
            Number('0.'+stavkaN)).toFixed(2));
 

        // $(el).closest('tr').find('#id_SummaNDS').closest('td').next().text(proizved);
        $(el).closest('tr').find('#id_TSena').closest('td').next().val(proizved.toFixed(2));

        $(el).closest('tr').find('#id_SummaNDS').closest('td').next().text(Number($(el).closest('tr').find('#id_Summa').val()).toFixed(2));
 
    }
});