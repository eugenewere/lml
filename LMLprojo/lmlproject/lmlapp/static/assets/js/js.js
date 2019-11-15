
var disability = document.getElementsByClassName('des')[0];
    function openDisability() {
        disability.style.display="block";
        disability.setAttribute('required','required');
    }
    function closeDisability() {
        disability.style.display="none";
    }





    // $(document).ready(function() {
    //     $("#submitbutton").attr('disabled',function () {
    //          $(this).on("click", function () {
    //             alert("Accept to terms and conditions to proceed");
    //         });
    //
    //          $('#termscheck:first-child').on('click', function () {
    //             if($(this).checked === true){
    //                 $('#submitbutton').removeAttr("disabled");
    //             }else if($(this).checked === false){
    //                 $("#submitbutton").attr('disabled','disabled');
    //                 alert("Accept to terms and conditions to proceed");
    //             }
    //
    //          })
    //         // if (typeof attr !== typeof undefined && attr !== false) {
    //         //     // ...
    //         // }
    //     });
    // });

// function openSubmit() {
//     var submitbutton = document.getElementsByClassName('submitbutton')[0];
//     var termscheck = document.getElementsByClassName('termscheck')[0];
//     var attr = submitbutton.getAttributeNode("disabled");
//
//
//     if(termscheck.checked === true){
//         submitbutton.removeAttribute("disabled");
//     }else {
//         submitbutton.setAttribute("disabled", "disabled");
//
//     }
// }

// $('.extra-field-box').each(function() {
//     var $wrapp = $('.multi-box', this);
// 		$(".add-field", $(this)).click(function() {
//
// 			$('.dublicat-box:first-child', $wrapp).clone(true,true).appendTo($wrapp).find('input').val('').find('select').val('').focus();
// 			// alert($('.dublicat-box:first-child', $wrapp).clone(true,true).appendTo($wrapp).find('input').val('').find('select').val('').focus());
// 			// console.log($('.dublicat-box:first-child', $wrapp).clone(true,true).appendTo($wrapp).find('input').val('').find('select').val('').focus())
// 		});
//     	$('.dublicat-box .remove-field', $wrapp).on('click', function() {
//         if ($('.dublicat-box', $wrapp).length > 1)
//             $(this).parent('.dublicat-box').remove();
// 		});
// 	});

    function showItem(qualifications) {
    console.log(qualifications);
    console.log(qualifications[3]);
    console.log(qualifications.value);
    console.log(qualifications[3].value);

        // var qualifications = document.getElementsByClassName("qualifications");






        for(i=0; i<qualifications.length; i++){

            let phd = document.getElementsByClassName("phd");
            for(p=0; p<phd.length; p++){

                let masters = document.getElementsByClassName("masters");
                for(m=0; m<masters.length; m++){

                    let diploma = document.getElementsByClassName("diploma");
                    for(d=0; d<diploma.length; d++){

                        let certificate = document.getElementsByClassName("certificate");
                        for(c=0; c<certificate.length; c++){

                            let bachelor = document.getElementsByClassName("bachelor");
                            for(b=0; b<bachelor.length; b++){

                               let university = document.getElementsByClassName("uni");
                                for(u=0; u<university.length; u++){

                                     let date = document.getElementsByClassName("date");
                                    for(g=0; g<date.length; g++){

                                        let reg_no = document.getElementsByClassName("reg_no");
                                        for(r=0; r<reg_no.length; r++) {
                                            // console.log(qualifications[i].selected=== 'Phd');
                                            // console.log(qualifications[i].selected);
                                            // console.log(qualifications[i].value);
                                            if (qualifications.value === 'Phd') {
                                                phd[p].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (masters[m].style.display === "block" || diploma[d].style.display === "block" || certificate[c].style.display === "block" || bachelor[b].style.display === "block") {
                                                    masters[m].style.display = "none";
                                                    diploma[d].style.display = "none";
                                                    certificate[c].style.display = "none";
                                                    bachelor[b].style.display = "none";
                                                }
                                            }
                                            else if (qualifications.value === 'Masters') {
                                                masters[m].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (phd[p].style.display === "block" || diploma[d].style.display === "block" || certificate[c].style.display === "block" || bachelor[b].style.display === "block") {
                                                    phd[p].style.display = "none";
                                                    certificate[c].style.display = "none";
                                                    diploma[d].style.display = "none";
                                                    bachelor[b].style.display = "none";
                                                }
                                            }
                                            else if (qualifications.value === "Bachelor") {
                                                bachelor[b].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (phd[p].style.display === "block" || diploma[d].style.display === "block" || certificate[c].style.display === "block" || masters[m].style.display === "block") {
                                                    phd[p].style.display = "none";
                                                    certificate[c].style.display = "none";
                                                    diploma[d].style.display = "none";
                                                    masters[m].style.display = "none";
                                                }
                                            }
                                            else if (qualifications.value === "Diploma") {
                                                diploma[d].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (phd[p].style.display === "block" || masters[m].style.display === "block" || certificate[c].style.display === "block" || bachelor[b].style.display === "block") {
                                                    phd[p].style.display = "none";
                                                    certificate[c].style.display = "none";
                                                    masters[m].style.display = "none";
                                                    bachelor[b].style.display = "none";
                                                }
                                            }
                                            else if (qualifications.value === "Certificate") {
                                                certificate[c].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (phd[p].style.display === "block" || masters[m].style.display === "block" || diploma[d].style.display === "block" || bachelor[b].style.display === "block") {
                                                    phd[p].style.display = "none";
                                                    diploma[d].style.display = "none";
                                                    masters[m].style.display = "none";
                                                    bachelor[b].style.display = "none";
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

// for(i=0; i<qualifications.length; i++) {
//      if (qualifications[i].value === 'Phd') {
//         phd[p].style.display = "block";
//         date[g].style.display = "block";
//         university[u].style.display = "block";
//         reg_no[r].style.display = "block";
//         if (masters[m].style.display === "block" || diploma[d].style.display === "block" || certificate[c].style.display === "block" || bachelor[b].style.display === "block") {
//             masters[m].style.display = "none";
//             diploma[d].style.display = "none";
//             certificate[c].style.display = "none";
//             bachelor[b].style.display = "none";
//         }
//     }
// }


function showPHD(qualifications) {
        console.log(qualifications.item().id);
        for(i=0; i<qualifications.length; i++){
            let phd = document.getElementsByClassName("phd");
            for(p=0; p<phd.length; p++){
                let masters = document.getElementsByClassName("masters");
                for(m=0; m<masters.length; m++){
                    let diploma = document.getElementsByClassName("diploma");
                    for(d=0; d<diploma.length; d++){
                        let certificate = document.getElementsByClassName("certificate");
                        for(c=0; c<certificate.length; c++){
                            let bachelor = document.getElementsByClassName("bachelor");
                            for(b=0; b<bachelor.length; b++){
                               let university = document.getElementsByClassName("uni");
                                for(u=0; u<university.length; u++){
                                     let date = document.getElementsByClassName("date");
                                    for(g=0; g<date.length; g++){
                                        let reg_no = document.getElementsByClassName("reg_no");
                                        for(r=0; r<reg_no.length; r++) {
                                            // console.log(qualifications[i].selected=== 'Phd');
                                            // console.log(qualifications[i].selected);
                                            // console.log(qualifications[i].value);
                                            if (qualifications.value === 'Phd') {
                                                phd[p].style.display = "block";
                                                date[g].style.display = "block";
                                                university[u].style.display = "block";
                                                reg_no[r].style.display = "block";
                                                if (masters[m].style.display === "block" || diploma[d].style.display === "block" || certificate[c].style.display === "block" || bachelor[b].style.display === "block") {
                                                    masters[m].style.display = "none";
                                                    diploma[d].style.display = "none";
                                                    certificate[c].style.display = "none";
                                                    bachelor[b].style.display = "none";
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
}









// var clonebutton1 = document.getElementById('clonebutton1');
// var clonebutton2 = document.getElementById('clonebutton2');

    function showEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

         for(i=0; i<employer.length; i++){
            employer[i].style.display="block";
            // employer[i].setAttributeNode('required')[i]
            // employer[i].getElementsByTagName('textarea')[i].setAttribute('required','required');

         }

         // for(x=0; x<employer.length; x++){
         //    employer[x].getElementsByTagName('input')[x].setAttribute('required','required');
         // }
        clonebutton1.style.display = "block";
        clonebutton2.style.display = "block";
    }
    function hideEmployment() {
        var clonebutton1 = document.getElementById('clonebutton1');
        var clonebutton2 = document.getElementById('clonebutton2');
        var employer = document.getElementsByClassName('employerwrapper');

        for(i=0; i<employer.length; i++){
            employer[i].style.display="none";

        }
         clonebutton1.style.display = "none";
         clonebutton2.style.display = "none";
    }


function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();
         var disclaimer= document.getElementById("disclaimer");
            reader.onload = function (element) {
                $('.blah').attr('src', element.target.result).css('visibility', 'visible');
                disclaimer.style.visibility = "hidden";
            };
            reader.readAsDataURL(input.files[0]);
            }
        }




(function ($) {
    // USE STRICT
    "use strict";
    $(".animsition").animsition({
      inClass: 'fade-in-left',
      outClass: 'fade-out-right',
      inDuration: 900,
      outDuration: 900,
      linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"]):not([class^="not_a_link"]) textarea:not([class^="form-control"])',
      loading: true,
      loadingParentElement: 'html',
      loadingClass: 'Loader-bg',
      loadingInner: '<div class="loader">' +
                          '<span></span>' +
                          '<span></span>' +
                          '<span></span>' +
                          '<span></span>' +
                      '</div>',
      timeout: false,
      touchSupport  :   true,
      timeoutCountdown: 5000,
      onLoadEvent: true,
      browser: ['animation-duration', '-webkit-animation-duration'],
      overlay: false,
      overlayClass: 'animsition-overlay-slide',
      overlayParentElement: 'body',
      transition: function (url) {
        window.location.href = url;
      }
    });


  })(jQuery);

function fixIds(elem, cntr) {
    $(elem).id.each(function() {
        this.id = this.id.replace(/\d+$/, "") + cntr;
        console.log(this.id);
    })
}

$('.extra-field-box').each(function() {
    var $wrapp = $('.multi-box', this);
		$(".add-field", $(this)).click(function() {
			$('.dublicat-box:last-child', $wrapp).clone(true,true).appendTo($wrapp).find('input').val('').find('select').val('').focus();

            var table=  $('.duplicate:first-child').find('select').id;
            var new_id = table + 1;
            table = new_id;
            // var x =table.id = + "1";
            // table.attr('id ', table.id+1)
		});
    	$('.dublicat-box .remove-field', $wrapp).on('click', function() {
        if ($('.dublicat-box', $wrapp).length > 1)
            $(this).parent('.dublicat-box').remove();
		});
	});







