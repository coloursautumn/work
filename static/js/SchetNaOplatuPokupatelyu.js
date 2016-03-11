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
    $("#SdelkaZakazPostavschiku_button").on( "click", function() {
        window.open("/ZakazPostavschiku/new/");
    });
    $("#nomen").on( "click", function() {
        window.open("/Nomenklatura/new/");
    });
    $("#edinizmer").on( "click", function() {
        window.open("/EdinitsyIzmereniya/new/");
    });
    $("#Podrazdelen").on( "click", function() {
        window.open("/Podrazdeleniya/new/");
    });
    $("#sklady_button").on( "click", function() {
        window.open("/Sklady/new/");
    });
    $("#Nomenklatura").on( "click", function() {
        window.open("/Nomenklatura/new/");
    });

    $("#EdinitsaIzmereniya").on( "click", function() {
        window.open("/EdinitsyIzmereniya/new/");
    });
    $( "#id_KontaktnoeLitsoKontragentaKontaktnyeLitsaKontragentov" ).closest( "p" ).append( '<button id="DobavKontLiKontragenta">+</button>' );
    $("#DobavKontLiKontragenta").on( "click", function() {
        $.cookie('idKontragent', String($('#id_KontragentKontragenty').val()), {path: '/KontaktnyeLitsaKontragentov'});
        window.open("/KontaktnyeLitsaKontragentov/new/");

    });
    $( "#id_ZakazPokupatelya" ).closest( "p" ).append( '<button id="ZakazPokupatelyab">+</button>' );
    $("#ZakazPokupatelyab").on( "click", function() {
        $.cookie('idKontragent', String($('#id_KontragentKontragenty').val()), {path: '/ZakazPokupatelya'});
        window.open("/ZakazPokupatelya/new/");

    });


/*	if($("#id_KontragentKontragenty").val()==''){
        $('#id_DogovorKontragenta').closest('p').hide();
        $('#id_SdelkaZakazPokupatelya').closest('p').hide();
    }else{
        $('#id_KontragentKontragenty').attr('disabled', true);
        $('#id_SdelkaZakazPokupatelya').attr('disabled', true);
        $('#id_DogovorKontragenta').attr('disabled', true);
    }*/
 
    $('#id_Organizatsiya option').last().attr('selected', 'selected');
    

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

    function ajaxkontragentWithKontactL() {
        $.ajax({
            type: "POST",
            url: '/getIdDocKontragentaDima/',
            data: {id:$('#id_KontragentKontragenty option:selected').val()},
            success: function(data)
            {
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
                        url: '/getContactsDlyaKontragenta/',
                        data: {id:$('#id_KontragentKontragenty option:selected').val()},
                        success: function(data)
                        {   
                            
                            var array = [];
                            $.each(data.split('?'), function(){
                                array.push(this)
                            })
                            $.each($('#id_KontaktnoeLitsoKontragentaKontaktnyeLitsaKontragentov').find('option'),function(){
                                if(($.inArray($(this).val(), array))>-1){
                                    console.log($(this).val(),$.inArray($(this).val()), array)
                                }else{
                                    $(this).hide();
                                    console.log($(this).val(),$.inArray($(this).val()), array)
                                }
                                
                            })
                            /*$.each($('#id_KontaktnoeLitsoKontragentaKontaktnyeLitsaKontragentov').find('option'),function(){
                                el=$(this);
                                el.hide();
                                $.each(data.split('?'), function(){
                                    if(el.val()== this && this!=''){    
                                        el.show();
                                    }
                                })
                                
                            })*/
                        }
                    });
                    $.ajax({
                            type: "POST",
                            url: '/getSdelkaDlyaKontragenta/',
                            data: {id:$('#id_KontragentKontragenty option:selected').val()},
                            success: function(data)
                            {
                                console.log(data);
                                $.each($('#id_ZakazPokupatelya').find('option'),function(){
                                el=$(this);
                                el.hide();
                                $.each(data.split('?'), function(){
                                    if(el.val()== this && this!=''){    
                                        el.show();
                                    }
                                })
                                
                            })
                            }
                        });
                }else{

                    $('#id_DogovorKontragenta').attr('disabled', true);
                }
            }
        });
    }

    ajaxkontragentWithKontactL();

    $("#id_KontragentKontragenty").on( "change", function() {
        ajaxkontragentWithKontactL();
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
 
 
 
        schet = 0;
        $.each($('td.selection div'), function(){
            if($(this).is(':hidden')){
                schet ++;
            }
        })
        if(schet!=8){
            $(this).closest('tr').find('.selection').next().text('Из документа партии')
        }
 
 
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
        $('.summaObs').text(sumObs.toFixed(2));
 
        ndsObs = 0;
        $.each($('body').find('.SummaNDS input'), function(){
            ndsObs += Number($(this).val());
        });
        $('#ndsObs').text(ndsObs.toFixed(2));
    }
});