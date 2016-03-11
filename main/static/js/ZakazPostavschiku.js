$( document ).ready(function() {


    $("#TipTSenb").on( "click", function() {
        window.open("/TipyTSenNomenklatury/new/");
    });


    $("#Organizatsiyab").on( "click", function() {
        window.open("/Organizatsii/new/");
    });


    $("#Kontragen").on( "click", function() {
        window.open("/Kontragenty/new/");
    });


    $("#DogovorKontragent").on( "click", function() {
        window.open("/DogovoryKontragentov/new/");
    });

    $("#Skladb").on( "click", function() {
        window.open("/Sklady/new/");
    });

    $("#Nomenklatura").on( "click", function() {
        window.open("/Nomenklatura/new/");
    });

    $("#EdinitsaIzmereniya").on( "click", function() {
        window.open("/EdinitsyIzmereniya/new/");
    });

    $(".FizLitsa").on( "click", function() {
        window.open("/FizicheskieLitsa/new/");
    });

    $('#KontactListso').on( "click", function() {
        window.open("/KontaktnyeLitsaKontragentov/new/");
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
    resultat();

    $('.save').click(function(){
        $('#id_SummaDokumenta').val($('#summaObs').text());
    })
 
    $('#id_Organizatsiya option').last().attr('selected', 'selected');
   
    $("#id_Kontragent").on( "change", function() {
        $.ajax({
            type: "POST",
            url: '/getIdDocKontragentaPostavshika/',
            data: {id:$('#id_Kontragent option:selected').val()},
            success: function(data)
            {
                if( $("#id_DogovorKontragenta").val()!=data){
                    $("#id_DogovorKontragenta").val(data);
                    if(data!=''){
                        $('#id_SdelkaZakazPokupatelya').attr('disabled', false);
                        $('#id_DogovorKontragenta').attr('disabled', false);
                        $('#id_DogovorKontragenta').parent().show();
                        $('#id_SdelkaZakazPokupatelya').parent().show();
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
                                $.each($('#id_SdelkaZakazPokupatelya').find('option'),function(){
                                    if($(this).val() in array){
                                       
                                    }else{
                                        $(this).hide();
                                    }
                                })
                            }
                        });
                    }else{
                        $('#id_SdelkaZakazPokupatelya').val('');
                        $('#id_SdelkaZakazPokupatelya').attr('disabled', true);
                        $('#id_DogovorKontragenta').attr('disabled', true);
                    }
                }
            }
        });
    });
 
    $.each($('body').find('.Kolichestvo input'),function(){
        pereschet($(this));
    });

    function ser(el)
        {
            var serialized = $(el).serialize();
            if (!serialized) // not a form
                serialized = $(el).find('input[name],select[name],textarea[name]').serialize();
            return decodeURIComponent(serialized.replace(/\+/gi, " "));
        }

    $(document).on('change', '#id_TipTSen', function(){
        $.each($('#myTabContent').find('.nomenklatura select'),function(){
            var el = $(this);
            $.ajax({
                type: "POST",
                url: '/getTovarOptionsSTipTSen/',
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
                    pereschet(el);
                    resultat();
                },
                error:function(data)  
                {   
                    $(el).closest('tr').find('#id_EdinitsaIzmereniya option').eq(1).attr('selected', 'selected');
                    $(el).closest('tr').find('#id_Koeffitsient').val('');
                    $(el).closest('tr').find('#id_TSena').val('');
                    $(el).closest('tr').find('#id_Kolichestvo').val('');
                    $(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val('');
                    $(el).closest('tr').find('#id_StavkaNDS').eq(1).attr('selected', 'selected');
                    $(el).closest('tr').find('#id_SummaNDS').val('');
                    $(el).closest('tr').find('td').eq(12).val('');
                    pereschet(el);
                    resultat();
                },
            });

            
        });
        
        

    });

    $(document).on('change', '#id_Nomenklatura', function(){
        var el = $(this);
            $.ajax({
                type: "POST",
                url: '/getTovarOptionsSTipTSen/',
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
                    pereschet(el);
                    resultat();
                },
                error:function(data)  
                {   
                    $(el).closest('tr').find('#id_EdinitsaIzmereniya option').eq(1).attr('selected', 'selected');
                    $(el).closest('tr').find('#id_Koeffitsient').val('');
                    $(el).closest('tr').find('#id_TSena').val('');
                    $(el).closest('tr').find('#id_Kolichestvo').val('');
                    $(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val('');
                    $(el).closest('tr').find('#id_StavkaNDS').eq(1).attr('selected', 'selected');
                    $(el).closest('tr').find('#id_SummaNDS').val('');
                    $(el).closest('tr').find('td').eq(12).val('');
                    pereschet(el);
                    resultat();
                },
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
            $(el).closest('tr').find('#id_Summa').val(proizved-(proizved*(Number($(el).closest('tr').find('#id_ProtsentSkidkiNatsenki').val())/100)));
        }
        else{
            $(el).closest('tr').find('#id_Summa').val(proizved);
        }
        
        $(el).closest('tr').find('.SummaBezSkidki').val(proizved);
         
 
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
        $(el).closest('tr').find('#id_TSena').closest('td').next().val(proizved);

        $(el).closest('tr').find('#id_SummaNDS').closest('td').next().text(Number($(el).closest('tr').find('#id_Summa').val()).toFixed(2));
 
 
        sumObs = 0;
        $.each($('body').find('.Summa input'), function(){
            sumObs += Number($(this).val());
        });
        $('#summaObs').text(sumObs.toFixed(2));
 
        ndsObs = 0;
        $.each($('body').find('.SummaNDS input'), function(){
            ndsObs += Number($(this).val());
        });
        $('#ndsObs').text(ndsObs.toFixed(2));

    }
});