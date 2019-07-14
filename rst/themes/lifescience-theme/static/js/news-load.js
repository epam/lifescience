var currentPage = 0;
var articles = [];
var firstDisabledPage;
var newsContent = document.getElementsByClassName("news-content")[0];
for (var i = 0; i < newsContent.children.length; i++) {
    if (newsContent.children[i].localName == 'div' && newsContent.children[i].classList.contains('news-article')) {
        articles.push(newsContent.children[i]);
        if (articles.indexOf(newsContent.children[i]) >= 3)
            newsContent.children[i].classList.toggle('invisible');
    }
}
firstDisabledPage = (articles.length / 3).toFixed();
for (i = firstDisabledPage; i < 3; i++) {
    $('#pagination-' + i).toggleClass('disable');
}

function paginationClick(number, offset) {
    if (number == currentPage) return;
    if (number == null) number = currentPage + offset;

    $('#pagination-' + currentPage).toggleClass('active');
    $('#pagination-' + number).toggleClass('active');
    for (var i = 0; i < articles.length; i++) {
        if (i >= currentPage * 3 && i < currentPage * 3 + 3
            || i >= number * 3 && i < number * 3 + 3)
            articles[i].classList.toggle('invisible')
    }
    if (number == 0 || currentPage == 0) $('#prev-page').toggleClass('disable');
    if (number == firstDisabledPage-1 || currentPage == firstDisabledPage-1) $('#next-page').toggleClass('disable');
    currentPage = number;
}