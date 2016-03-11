$.each($('body').find('.selection select'), function(){
        if($(this).val()==''){
            $(this).toggle();
        }
    });
    $.each($('div.selection'), function(){
        var god = 0;
        $.each($(this).find('select'), function(){
            if($(this).val()!=''){
                god = 1;
            }
        });
        if(god==1){
            $(this).closest('.selection').find('.dropdown').toggle();
        }
    });
    $( document ).ready(function() {

        $('.token, .nt').children().prop('readonly', true);

        

        $.each($('td.selection'), function(){
            var god = 0;
            $.each($(this).find('select'), function(){
                if($(this).val()!=''){
                    god = 1;
                }
            });
            if(god==0){
                $(this).append($('.addTovar div').parent().html());
            }
        });

        


        $(".tovar select, .tovar input").on( "click", function() {
            if($(this).closest('tr').attr('class')=='tovar'){
                $(this).closest('tr').addClass('new');
            }
        });

        $(".del").on( "click", function() {
            $(this).parent().find('table #del').toggle();
        });

        $(".add").on("click", function () {
            $(this).parent().find('tbody').append($("."+$(this).attr('id')).find('tbody').html());
            $(".new td ul.dropdown-menu li a").on("click", function () {
                $(this).closest('.dropdown').parent().append($('.' + $(this).closest('div').attr('id')).find("." + $(this).attr('class')).html());
                $(this).closest('td').find('select').show();
                $(this).closest('div').remove();
            });
        });

        $(".selection ul.dropdown-menu li a").on( "click", function() {
                $(this).closest('.dropdown').parent().find('.'+$(this).attr('class')+' select').toggle();
                $(this).closest('.dropdown').toggle();
            });

        /**
        * Serializes form or any other element with jQuery.serialize
        * @param el
        */
        function ser(el)
        {
            var serialized = $(el).serialize();
            if (!serialized) // not a form
                serialized = $(el).find('input[name],select[name],textarea[name]').serialize();
            return serialized;
        }


        $(".save").on("click", function() {
            var arr = [];
            arr.push($(this).parent().attr('id'));
            arr.push($('#id_obj').text());
            arr.push($('#name_obj').text());
            $.each($(this).parent().find('.new'), function(){
                arr.push('id_subobj='+$(this).find('div#id_subobj').text()+'&'+ser(this));
            });
            $.ajax({
                type: "POST",
                url: '/saveSubobj/',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(arr),
                success: function(data)
                {
                    
                }
            });
            $(this).parent().find('.new').removeClass('new');
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
                    location.reload(true);
                }
            });
        });
    });