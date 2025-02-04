$(document).ready(function () {å
    $('.tab_item').click(function(){
        $('.tab_item').removeClass('active');
        $(this).addClass('active');
    });

    $('.fitness_list').click(function(){
        $('.fitness_after').show();
        $('.fitness_list').hide();
    });
    $('.genre_active').click(function(){
        $('.fitness_after').hide();
        $('.fitness_list').show();
    });
    $('.nutrition_list').click(function(){
        $('.nutrition_after').show();
        $('.nutrition_list').hide();
    });
    $('.genre_active').click(function(){
        $('.nutrition_after').hide();
        $('.nutrition_list').show();
    });
});