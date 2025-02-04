$(document).ready(function () {
    $('.tab_item').click(function(){
        $('.tab_item').removeClass('active');
        $(this).addClass('active');
    });
    // $('.Incomplete ul').click(function(){
    //     if($('.Incomplete ul').click){
    //         $('.click_detail').show();
    //     }else{
    //         $('body').click(function(){
    //             $('.click_detail').hide();
    //         });
    //     }
        
    // });

    $(document).ready(function(){
        $('.Incomplete ul').click(function(event){
            event.stopPropagation(); // クリックイベントが body に伝播するのを防ぐ
            $('.click_detail').show();
        });
    
        $('body').click(function(){
            $('.click_detail').hide();
        });
    });
});