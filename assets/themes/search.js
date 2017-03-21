var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

$( document ).ready(function() {
    var query = getUrlParameter('q');
    var searchInput = $('#searchInput');
    var runSearch = function(query) {
        $.each(search_data, function(k, v) {
            var keys = ['title', 'category', 'tags', 'content'];
            for (var k2 in keys){
                var idx = v[keys[k2]].indexOf(query);
                if (idx > -1) {
                    $($('.posts li')[k]).addClass('active');
                    // $($('.posts li')[k]).fadeIn();
                    return true
                };
                $($('.posts li')[k]).removeClass('active');
            };
        });
    };
    runSearch(query);
    $('.posts li.active').show();
    if ($('.posts li.active').length == 0){
        $('.posts .no-matches').show();
    } else {
        $('.posts .no-matches').hide();
    };
    searchInput.val(query);
    searchInput.on('keyup', function(){
        if($(this).val()){
            runSearch($(this).val());
            $('.posts li.active').fadeIn(150);
            $('.posts li:not(.active)').fadeOut(150);
            if ($('.posts li.active').length == 0){
                $('.posts .no-matches').fadeIn(150);
            } else {
                $('.posts .no-matches').fadeOut(150);
            };
        }
    });
    // console.log($('.posts li')[result]);
    // $('.posts li')[result].fadeIn();
});
