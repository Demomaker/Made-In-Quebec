const madeIn = require("made-in");
 
// Some cool JS stuff made in Romania
madeIn("Quebec", {
   token: "..."
}, (err, data) => {
    console.log(err || data.map(c => c.full_name).join("\n"));
    // IonicaBizau/git-stats
    // IonicaBizau/scrape-it
    // skidding/cosmos
    // victorstanciu/dbv
    // skidding/dragdealer
    // flaviusmatis/simplePagination.js
    // cthackers/adm-zip
    // ghinda/jotted
    // alessioalex/ClientManager
    // IonicaBizau/image-to-ascii
    // IonicaBizau/medium-editor-markdown
    // balajmarius/adi.js
    // ...
});