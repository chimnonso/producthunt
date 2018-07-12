// $('.button').click(function () {
//     console.log("hello");
//     // var prod_id;
//     // prod_id = $(this).attr("data-upvote");
//     // $.get('/products/upvote/', { product_id: prod_id }, function (data) {
//     //     $('#upvoteCount').html(data);
//     //     // $('#likes').hide();
//     // });
//     console.log("Hello");
// });

$(document).ready(function () {
    $(".btn-upvote").click(function() {
        var prod_id;
        prod_id = $(this).attr("data-prodid");
        $.get('/products/upvote/', { product_id: prod_id }, function (data) {
            // console.log(data)
            $(".upvote_count").html(data);
            $('.btn-upvote').attr("disabled", true);
            // console.log($(this).attr("disabled"));
        });
        
    });

    $("#demo1").click(function(){
        $(this).attr("disabled", true);
        console.log("Hello");
        $(this).html("Added here")
    })
    
})