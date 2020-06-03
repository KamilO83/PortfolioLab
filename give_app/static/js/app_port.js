document.addEventListener("DOMContentLoaded", function() {
    $("#donation").submit(function (e) {

        e.preventDefault();
        var serializedData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: '/form/',
            data: serializedData,
            success: function (response) {
                $("#donation").trigger('reset');
            },
            error: function (response) {
                alert(response["responseJSON"]["error"]);
            }
        });
    });
});