var DOCUMENTATION_OPTIONS = {
    URL_ROOT:    './',
    VERSION:     '0.3.0',
    COLLAPSE_INDEX: false,
    FILE_SUFFIX: '.html',
    HAS_SOURCE:  false
};

$(window).on('load',function () {
    //document.title = "{{ title }}"
    UUI.Navigation.init();
    UUI.Global_Search.init();

    $('.news').height($('#main-tiles').height())
});