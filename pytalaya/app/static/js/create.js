$(document).ready(function() {
    $("#id_password").attr("disabled", "disabled");
    $("#id_private").click(function() {
    var checked_status = this.checked;
    if (checked_status == true) {
       $("#id_password").removeAttr("disabled");
    } else {
       $("#id_password").attr("disabled", "disabled");
    }
    });
});
