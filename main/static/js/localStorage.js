$( document ).ready(function() {
	var dontclear = false;

    /*$(document).one('click', function() {
        alert('window_focus.val()');

    })*/
    
    $(window).focus(function() {
        $.each($('.form').find('input'), function(){
            
            if ((this.id)=='id_Kod') {
            
            }else if ( $(this).attr('type') == 'checkbox') {
            localStorage.setItem( this.id , $(this).prop( "checked" ));
            }else{
                localStorage.setItem( this.id , $(this).val());
            }
            
        });
        $.each($('.form').find('select'), function(){
            if($(this.id) != 'id_Kod'){
            localStorage.setItem( this.id , $(this).val());
            }
        });
        location.reload();
    }).blur(function() {
        window.localStorage.clear();
    });

    $.each($('.form').find('input'), function(){
        if ( $(this).attr('type') == 'checkbox'  && localStorage.getItem( this.id )=='true') {
            $(this).attr('checked',true);
        }else if($(this).val() != localStorage.getItem( this.id ) && localStorage.getItem( this.id )){
            $(this).val(localStorage.getItem( this.id ));
            }
    });
    $.each($('.form').find('select'), function(){
        if($(this).val() != localStorage.getItem( this.id ) && localStorage.getItem( this.id )){
            $(this).val(localStorage.getItem( this.id ));
        }    
    });


/*
	$('.reload_window').on('click', function() {
        $.each($('.form').find('input'), function(){
        	
        	if ((this.id)=='id_Kod') {
    		
    		}else if ( $(this).attr('type') == 'checkbox') {
    		localStorage.setItem( this.id , $(this).prop( "checked" ));
    		}else{
            	localStorage.setItem( this.id , $(this).val());
    		}
            
        });
        $.each($('.form').find('select'), function(){
        	if($(this.id) != 'id_Kod'){
            localStorage.setItem( this.id , $(this).val());
            }
        });
        dontclear = true;
        location.reload();
    });

    $.each($('.form').find('input'), function(){
    	if ( $(this).attr('type') == 'checkbox'  && localStorage.getItem( this.id )=='true') {
    		$(this).attr('checked',true);
    	}else if($(this).val() != localStorage.getItem( this.id ) && localStorage.getItem( this.id )){
	    	$(this).val(localStorage.getItem( this.id ));
			}
    });
    $.each($('.form').find('select'), function(){
    	if($(this).val() != localStorage.getItem( this.id ) && localStorage.getItem( this.id )){
            $(this).val(localStorage.getItem( this.id ));
        }    
    });
    $(window).on('unload', function(){
         if (dontclear == false){
            window.localStorage.clear();
         };
    });*/
    
});