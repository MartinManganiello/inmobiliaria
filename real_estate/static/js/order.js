function get_order(){
    new Ajax.Request('/propiedades/', { 
    method: 'post',
    parameters: $H({'filter_by':$('id_filter_by').getValue()}),
    onSuccess: function(transport) {
        var e = $('id_color')
        if(transport.responseText)
            e.update(transport.responseText)
    }
    }); // end new Ajax.Request
}