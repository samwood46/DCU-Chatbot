let was_open;  // for storing whether the settings menu was open

/* open the navigation menu */
function openNav() {
    menucheck();
    if(was_open == true) {
        setTimeout(function () {
            document.getElementById("myNav").style.width = "100%";
        }, 500);
    }else{
    document.getElementById("myNav").style.width = "100%";
    }
}


/* Close nav menu when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
    document.getElementById("myNav").style.width = "0%";
    setTimeout(menucheck,500)
}

//check if settings menu is open
function menucheck() {
    if(document.getElementById("mySettings").style.visibility === "visible"){
      document.getElementById("mySettings").style.visibility = "hidden";
      was_open= true;
    }
    else if (was_open === true) {
        document.getElementById("mySettings").style.visibility = "visible";
        was_open = false;
    }
}

//open up the chat setttings and have update loop while open
function openSettings() {
        document.getElementById("mySettings").style.visibility = "visible";
    document.getElementById("mySettings").style.width = "100%";

    setInterval(update,300)
}

//change colour hex to rgb
function hexChanger(x) {
  var value = x.match(/[A-Za-z0-9]{2}/g);
  value = value.map(function(v) { return parseInt(v, 16) });
  return "rgb(" + value.join(",") + ")"
}

//update the chat settings
function update() {
        let usrn = document.getElementById("usersn").checked;
        if (usrn === false) {
            css_getclass('.username').style.visibility = "hidden";
            css_getclass('.botname').style.visibility = "hidden";

        }else if(usrn === true){
            css_getclass('.username').style.visibility = "visible";
            css_getclass('.botname').style.visibility = "visible";
        }

        let bot_bg_colour = hexChanger(document.getElementById("botcol").value);
        let  curr_bot_bg = css_getclass('.botText').style.backgroundColor;
        if (bot_bg_colour !== curr_bot_bg) {
            css_getclass('.botText').style.backgroundColor = bot_bg_colour;
        }

        let user_bg_colour = hexChanger(document.getElementById("usercol").value);
        let curr_user_bg = css_getclass('.botText').style.backgroundColor;
        if (user_bg_colour !== curr_user_bg) {
            css_getclass('.userText').style.backgroundColor = user_bg_colour;
        }

        let botFontSize = document.getElementById("bot_font_sz").value;
        let currBotFontSz= css_getclass('.botText').style.fontSize;
        if (botFontSize !== currBotFontSz) {
            css_getclass('.botText').style.fontSize = botFontSize;
        }

        let userFontSize = document.getElementById("user_font_sz").value;
        let currUserFontSz = css_getclass('.userText').style.fontSize;
        if (userFontSize !== currUserFontSz) {
            css_getclass('.userText').style.fontSize = userFontSize;
            document.getElementById("textInput").style.fontSize = userFontSize;
        }

        let  Font = document.getElementById("fonts").value;
        let currFont = css_getclass('.userText').style.fontFamily;
        if (Font !== currFont) {
            css_getclass('.userText').style.fontFamily = Font;
            css_getclass('.botText').style.fontFamily = Font;
        }


}

//close the settings menu
function closeSettings(){
    document.getElementById("mySettings").style.width = "0%";
    document.getElementById("mySettings").style.visibility = "hidden";
}

//used to get class css styles
function cssStyles() {
    let rules = {};
    for (let i=0; i<document.styleSheets.length; ++i) {
        let cssStyles = document.styleSheets[i].cssRules;
        for (let j=0; j<cssStyles.length; ++j)
            rules[cssStyles[j].selectorText] = cssStyles[j];
    }
    return rules;
}

//get css elements by class name rather than ID
function css_getclass(name) {
    let rules = cssStyles();
    if (!rules.hasOwnProperty(name))
        throw 'No such class property exists!';
    return rules[name];
}
