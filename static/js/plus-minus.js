//plugin bootstrap minus and plus
//http://jsfiddle.net/laelitenetwork/puJ6G/
$('.btn-number').click(function(e){
    e.preventDefault();

    // let fieldName = $(this).attr('data-field');
    let type      = $(this).attr('data-type');
    let input = $(this).closest('div').find('input');
    let currentVal = parseInt(input.val());
    if (!isNaN(currentVal)) {
        if(type === 'minus') {

            if(currentVal > input.attr('min')) {
                input.val(currentVal - 1).change();
            }
            if(input.val() === input.attr('min')) {
                $(this).attr('disabled', true);
            }

        } else if(type === 'plus') {

            if(currentVal < input.attr('max')) {
                input.val(currentVal + 1).change();
            }
            if(input.val() === input.attr('max')) {
                $(this).attr('disabled', true);
            }

        }
    } else {
        input.val(0);
    }
});


$('.input-number').focusin(function(){
   $(this).data('oldValue', $(this).val());
}).change(function() {

    let minValue =  parseInt($(this).attr('min'));
    let maxValue =  parseInt($(this).attr('max'));
    let valueCurrent = parseInt($(this).val());

    if(valueCurrent >= minValue) {
        $(this).closest('div').find('button[data-type="minus"]').removeAttr('disabled')
    } else {
        alert('Sorry, the minimum value was reached');
        $(this).val($(this).data('oldValue'));
    }
    if(valueCurrent <= maxValue) {
        $(this).closest('div').find('button[data-type="plus"]').removeAttr('disabled')
    } else {
        alert('Превышено максимальное значение');
        $(this).val($(this).data('oldValue'));
    }
    let count = $(this).val();
    let id = $(this).attr('data-id');

    $.ajax({
        method: "POST",
        url: URL_QUANTITY,
        dataType: 'json',
        data: {'id': id, 'count': count},
        success: function (data) {
            console.log(data);
            $('.cost').text(': ' + data['total_price'] + ' руб.');
            $('td[data-id='+id+']').text(data['book_total_price'] + ' руб.');
            $('#total-price').text(data['total_price'] + ' руб.');
        }
    })
}).keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode === 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
