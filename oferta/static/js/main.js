$(window).scroll(function() {
    var top = $(document).scrollTop();
    if (top < 200) $("#stay").removeClass('fixed-header');
    else $("#stay").addClass('fixed-header');
});

$('#myModal').on('shown.bs.modal', function() {
    $('#myInput').trigger('focus')
})