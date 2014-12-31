var template = document.querySelector("template[is='auto-binding']");
template.topics = [
    {
        name: "Plate Tectonics", pages: [
            {name: "Volcanoes", hash: "volcanoes"},
            {name: "Earthquakes", hash: "earthquakes"}
        ]
    }
];
template.addEventListener("template-bound", function (e){
    this.route = this.route || "home";
});

// Prevent selection of submenus
template.ignoreSubmenu = function (e){
    if (e.detail.isSelected && e.detail.item.localName == "core-item")
        this.route = e.detail.item.hash;
};