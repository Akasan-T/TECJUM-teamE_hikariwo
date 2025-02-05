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

    $('.Incomplete ul').click(function(event){
        event.stopPropagation(); // クリックイベントが body に伝播するのを防ぐ
        $('.click_detail').show();
    });

    $('body').click(function(){
        $('.click_detail').hide();
    });

    $('.genre_list_all li').click(function(event){
        event.stopPropagation();
        $('.click_genre').show();
    });
    $('body').click(function(){
        $('.click_genre').hide();
    });

    function setClock() {
        const now = new Date();
        const seconds = now.getSeconds();
        const minutes = now.getMinutes();
        const hours = now.getHours();
    
        const secDegrees = ((seconds / 60) * 360) + 90;
        const minDegrees = ((minutes / 60) * 360) + ((seconds / 60) * 6) + 90;
        const hourDegrees = ((hours % 12) / 12) * 360 + ((minutes / 60) * 30) + 90;
    
        const secHand = document.querySelector('.sec-hand');
        const minHand = document.querySelector('.min-hand');
        const hourHand = document.querySelector('.hour-hand');
    
        // 秒針が0秒に戻るときにtransitionを無効にする
        if (seconds === 0) {
            secHand.style.transition = 'none';
        } else {
            secHand.style.transition = 'all 0.05s ease-in-out';
        }
    
        secHand.style.transform = `rotate(${secDegrees}deg)`;
        minHand.style.transform = `rotate(${minDegrees}deg)`;
        hourHand.style.transform = `rotate(${hourDegrees}deg)`;
    }
    
    setInterval(setClock, 1000);
    setClock(); // 初期化
});