$('menu-btn').on('click', function() {
    e.preventDefault(e);
    $('.menu').toggleClass('menu_active');
    $('.content').toggleClass('content_active');
})