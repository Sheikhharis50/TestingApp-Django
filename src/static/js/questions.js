$(document).ready(function () {
    $('.select-all').change(function (e) {
        e.preventDefault();
        $('.checkbox-item').prop('checked', $(this).prop("checked"));
    });
    $('.page-next').click(function (e) { 
        e.preventDefault();
        
    });
});