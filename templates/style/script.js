document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('.header_bottom_list li');
    const borderLine = document.querySelector('.border_line');

    listItems.forEach(item => {
        item.addEventListener('click', function() {
            // すべてのリストアイテムからactiveクラスを削除
            listItems.forEach(li => {
                li.classList.remove('active');
                li.querySelector('p').style.color = 'black'; // テキストカラーを黒に戻す
            });
            // クリックされたリストアイテムにactiveクラスを追加
            this.classList.add('active');
            this.querySelector('p').style.color = 'white'; // クリックされたアイテムのテキストカラーを白に
            // border_lineにactiveクラスを追加
            borderLine.classList.add('active');
        });
    });
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