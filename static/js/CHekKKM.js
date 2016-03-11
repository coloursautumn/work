$( document ).ready(function() {

    $('h1:focus').css('color','red');
    $('#id_Organizatsiya option').last().attr('selected', 'selected');
   
    function resultat(){
        sumObs = 0;
        $.each($('body').find('.summa input'), function(){
            sumObs += Number($(this).val());
        });
        $('#vsego').text(sumObs.toFixed(2));
        $('#id_SummaDokumenta').val($('#vsego').text())
    }
    resultat();

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
                }
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
            }
        });
    })

    $(document).on('change','td.kolichestvo input, td.koeffitsient input, td.protsentSkidkiNatsenki input, td.summaOplaty input, #summaOpl', function(){
        pereschet(this);

    }); 
    

    if ($('#Oplata').find('table tr').size() > 1){
        $('#addOplatu').hide();
    }
    
    $('.chet').on('click',function(){
        if ($('#vsego').text() != ''){
            $('#Oplata').find('.summaOplaty:first input').val($('#vsego').text());
            $('#summaOpl').text($('#vsego').text());
        }
        $('#sdacha').text('0');
    });

    function pereschet(el){
        if ($('td.kolichestvo input, td.koeffitsient input, td.tsena input').val() != ''){
            var kolvo = $(el).closest('tr').find('td.kolichestvo input').val();
            var koef = $(el).closest('tr').find('td.koeffitsient input').val();
            var tsena = $(el).closest('tr').find('td.tsena input').val();
            var protsent = $(el).closest('tr').find('td.protsentSkidkiNatsenki input').val();
            var summ = kolvo * koef * tsena;
            summ = summ.toFixed(2);
            $(el).closest('tr').find('.summaBezSkidky input').val(summ);
            
            if (protsent == ''){
                $(el).closest('tr').find('.summa input').val(summ.toFixed(2));
            }
            else{
                $(el).closest('tr').find('.summa input').val((summ-(summ*(protsent/100))).toFixed(2));
            }
        }

        var summaObs = 0;
        var obsSummaOplaty = 0;

        $.each($('body').find('td.summa input'), function(){
            
            if($(this).val() != ''){
                summaObs += Number($(this).val());
            }
        });

        $.each($('body').find('td.summaOplaty input'), function(){
            
            if($(this).val() != ''){
                obsSummaOplaty += Number($(this).val());
            }
        });

        $('#vsego').text(summaObs.toFixed(2));
        $('#summaOpl').text(obsSummaOplaty.toFixed(2));

        

        if (obsSummaOplaty > summaObs){
            $('#sdacha').text(Number(obsSummaOplaty-summaObs).toFixed(2));
        }
        else{
                $('#sdacha').text(0);
        }
    }


    $('.save').click(function(){
        $('#id_SummaDokumenta').val($('#summaObs').text());
    })
    
    $(".add").on("click", function () {

        if ($('#Oplata').find('table tr').size() > 1){
            $('#addOplatu').hide();
        }
    });


});