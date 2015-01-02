var template = document.querySelector("template[is='auto-binding']");

template.topics = [];
getTopics(function (topics){
    template.topics = topics;
});

template.tolower = function (str){
    return str.toLowerCase();
};

/*template.addEventListener("template-bound", function (e){
    router.go("/home");
});*/

// Prevent selection of submenus
/*template.ignoreSubmenu = function (e){
    this._router = this._router || document.querySelector("app-router");
    if (e.detail.isSelected && e.detail.item.localName == "core-item")
        this._router
            .go(e.detail
                .item
                .firstChild
                .attributes
                .getNamedItem("href")
                .value
                .slice(2)
            );
};*/