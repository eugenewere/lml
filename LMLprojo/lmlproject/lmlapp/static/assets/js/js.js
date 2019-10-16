




var yesscheckbox = document.getElementById('yes');
var nocheckbox = document.getElementById('no');
var disability = document.getElementById('disability');
    function openDisability() {
        disability.style.display="block";
    }
    function closeDisability() {
        disability.style.display="none";
    }


var phd = document.getElementById("phd");
var masters = document.getElementById("masters");
var diploma = document.getElementById("diploma");
var certificate = document.getElementById("certificate");
    function showPhd(){
        phd.style.display="block";
        if( masters.style.display==="block" ||  diploma.style.display==="block" || certificate.style.display==="block"){
                masters.style.display="none";
                diploma.style.display="none";
                certificate.style.display="none";
        }
    }
    function showMasters(){
        masters.style.display="block";
         if( phd.style.display==="block" ||  diploma.style.display==="block" || certificate.style.display==="block"){
                phd.style.display="none";
                certificate.style.display="none";
                diploma.style.display="none";
        }
    }
    function showDiploma(){
        diploma.style.display="block";
         if( phd.style.display==="block" ||  masters.style.display==="block" || certificate.style.display==="block"){
                phd.style.display="none";
                certificate.style.display="none";
                 masters.style.display="none";
        }
    }
    function showCertificate(){
        certificate.style.display="block";
        if( phd.style.display==="block" ||  masters.style.display==="block" || diploma.style.display==="block"){
                phd.style.display="none";
                diploma.style.display="none";
                masters.style.display="none";
        }
    }

var employer = document.getElementById('employer');
    function showEmployment() {
        employer.style.display="block";
    }
    function hideEmployment() {
        employer.style.display="none";
    }








function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
            reader.onload = function (e) {
                $('.blah').attr('src', e.target.result).css('visibility', 'visible');
            };
            reader.readAsDataURL(input.files[0]);
            }
        }










